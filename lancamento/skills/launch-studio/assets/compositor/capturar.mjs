#!/usr/bin/env node
// launch-studio · capturar.mjs
// Captura a composição (cena.html) fotograma a fotograma em PNG, com Playwright e o browser que já existe.
// Captures the composition frame by frame as PNG, using Playwright and an already-installed browser.
//
// Uso (dentro de launch-output/work, com `npm i playwright-core` feito aí):
//   node compositor/capturar.mjs --formato 9x16 --fps 30 --lingua pt --saida frames-9x16
//
// Opções:
//   --cena <ficheiro>     composição (por defeito: cena.html ao lado deste script)
//   --formato 9x16|1x1|16x9|4x5
//   --fps 30              fotogramas por segundo
//   --escala 1            0.5 = metade da resolução (rascunhos)
//   --lingua pt|en
//   --inicio 0 --fim <s>  só um intervalo (por defeito, o vídeo todo)
//   --tempos 1.0,2.6      só estes instantes (para verificar), com nomes 000-1.00s.png
//   --guias               desenha as zonas seguras
//   --legendas            grava as legendas na imagem
//   --browser <caminho>   Chrome, Brave, Edge ou Chromium a usar
//   --saida <pasta>
//
// Depois: ffmpeg -framerate 30 -i <pasta>/%05d.png -i audio-final.wav -c:v libx264 -crf 18 -pix_fmt yuv420p \
//         -c:a aac -b:a 192k -shortest -movflags +faststart ../video/launch-9x16.mp4

import { createRequire } from "node:module";
import { pathToFileURL, fileURLToPath } from "node:url";
import fs from "node:fs";
import os from "node:os";
import path from "node:path";

const AQUI = path.dirname(fileURLToPath(import.meta.url));
const TAMANHOS = { "9x16": [1080, 1920], "1x1": [1080, 1080], "16x9": [1920, 1080], "4x5": [1080, 1350] };

function lerArgs(argv) {
  const a = { cena: path.join(AQUI, "cena.html"), formato: "9x16", fps: 30, escala: 1, lingua: "pt",
              saida: null, tempos: null, guias: false, legendas: false, browser: null, inicio: 0, fim: null };
  for (let i = 0; i < argv.length; i++) {
    const k = argv[i].replace(/^--/, "");
    const v = argv[i + 1];
    if (k === "guias" || k === "legendas") { a[k] = true; continue; }
    if (!(k in a)) { console.error(`Opção desconhecida: --${k}`); process.exit(2); }
    if (["fps", "escala", "inicio", "fim"].includes(k)) a[k] = Number(String(v).replace(",", "."));
    else if (k === "tempos") a.tempos = String(v).split(/[,;\s]+/).filter(Boolean).map(x => Number(x)); // 0.8,2.6,5.1
    else a[k] = v;
    i++;
  }
  if (!TAMANHOS[a.formato]) { console.error(`Formato desconhecido: ${a.formato} (usa ${Object.keys(TAMANHOS).join(", ")})`); process.exit(2); }
  a.saida = a.saida || `frames-${a.formato}`;
  return a;
}

function carregarPlaywright() {
  for (const base of [process.cwd(), AQUI]) {
    const req = createRequire(path.join(base, "noop.js"));
    for (const nome of ["playwright-core", "playwright"]) {
      try { return { pw: req(nome), nome }; } catch { /* tenta o seguinte */ }
    }
  }
  console.error("Não encontrei o Playwright. Nesta pasta, corre: npm i playwright-core   (≈8 MB; usa o browser que já tens)");
  process.exit(1);
}

function encontrarBrowser(pedido) {
  if (pedido) return pedido;
  const casa = os.homedir();
  const listas = {
    darwin: [
      "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
      "/Applications/Brave Browser.app/Contents/MacOS/Brave Browser",
      "/Applications/Microsoft Edge.app/Contents/MacOS/Microsoft Edge",
      "/Applications/Chromium.app/Contents/MacOS/Chromium",
      `${casa}/Applications/Google Chrome.app/Contents/MacOS/Google Chrome`,
      `${casa}/Applications/Brave Browser.app/Contents/MacOS/Brave Browser`
    ],
    win32: [
      "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe",
      "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe",
      "C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe",
      "C:\\Program Files\\BraveSoftware\\Brave-Browser\\Application\\brave.exe"
    ],
    linux: ["/usr/bin/google-chrome", "/usr/bin/chromium", "/usr/bin/chromium-browser", "/usr/bin/microsoft-edge", "/usr/bin/brave-browser"]
  };
  return (listas[process.platform] || []).find(p => fs.existsSync(p)) || null;
}

const a = lerArgs(process.argv.slice(2));
const { pw, nome } = carregarPlaywright();
const executavel = encontrarBrowser(a.browser);
if (!executavel && nome === "playwright-core") {
  console.error("Não encontrei Chrome, Brave, Edge nem Chromium. Indica um com --browser <caminho>,");
  console.error("ou (com autorização, ~150–250 MB) instala o do Playwright: npm i playwright && npx playwright install chromium");
  process.exit(1);
}

const [W, H] = TAMANHOS[a.formato];
const browser = await pw.chromium.launch({
  headless: true,
  ...(executavel ? { executablePath: executavel } : {}),
  args: ["--hide-scrollbars", "--force-color-profile=srgb", "--disable-lcd-text", "--allow-file-access-from-files"]
});
const page = await browser.newPage({ viewport: { width: W, height: H }, deviceScaleFactor: a.escala });
page.on("console", m => { if (["warning", "error"].includes(m.type())) console.error(`[página] ${m.text()}`); });
page.on("pageerror", e => console.error(`[página] erro: ${e.message}`));

const url = pathToFileURL(path.resolve(a.cena)).href +
  `?captura=1&formato=${a.formato}&lingua=${encodeURIComponent(a.lingua)}` +
  (a.guias ? "&guias=1" : "") + (a.legendas ? "&legendas=1" : "");
await page.goto(url, { waitUntil: "load" });
await page.evaluate(() => window.pronto);
const duracao = await page.evaluate(() => window.duracao());

let tempos;
if (a.tempos && a.tempos.length) {
  tempos = a.tempos;
} else {
  const fim = a.fim ?? duracao;
  const n = Math.round((fim - a.inicio) * a.fps);
  tempos = Array.from({ length: n }, (_, i) => a.inicio + i / a.fps);
}

fs.mkdirSync(a.saida, { recursive: true });
const t0 = Date.now();
for (let i = 0; i < tempos.length; i++) {
  const t = tempos[i];
  await page.evaluate(x => window.seek(x), t);
  const ficheiro = a.tempos ? `${String(i).padStart(3, "0")}-${t.toFixed(2)}s.png` : `${String(i).padStart(5, "0")}.png`;
  await page.screenshot({ path: path.join(a.saida, ficheiro), clip: { x: 0, y: 0, width: W, height: H } });
  if ((i + 1) % 30 === 0 || i === tempos.length - 1) {
    const s = (Date.now() - t0) / 1000;
    const falta = s / (i + 1) * (tempos.length - i - 1);
    process.stdout.write(`\r${i + 1}/${tempos.length} fotogramas · ${s.toFixed(0)} s · faltam ~${falta.toFixed(0)} s   `);
  }
}
process.stdout.write("\n");
await browser.close();
console.log(`OK ${tempos.length} fotogramas ${Math.round(W * a.escala)}×${Math.round(H * a.escala)} em ${a.saida}` +
            (executavel ? ` (browser: ${path.basename(executavel)})` : ""));
