// Site-base — website-builder. Pequeno e sem dependências.
// O menu móvel só fica escondido quando este script corre (classe "js" no <html>),
// por isso sem JavaScript a navegação continua visível e utilizável.
document.documentElement.classList.add("js");

document.addEventListener("DOMContentLoaded", () => {
  const botao = document.querySelector(".menu-botao");
  const menu = document.getElementById("menu");

  if (botao && menu) {
    const fechar = () => {
      botao.setAttribute("aria-expanded", "false");
      menu.classList.remove("aberta");
    };
    botao.addEventListener("click", () => {
      const aberto = botao.getAttribute("aria-expanded") === "true";
      botao.setAttribute("aria-expanded", String(!aberto));
      menu.classList.toggle("aberta", !aberto);
      if (!aberto) menu.querySelector("a")?.focus();
    });
    // Fecha com Esc e devolve o foco ao botão
    document.addEventListener("keydown", (e) => {
      if (e.key === "Escape" && botao.getAttribute("aria-expanded") === "true") {
        fechar();
        botao.focus();
      }
    });
    // Fecha ao escolher um link
    menu.addEventListener("click", (e) => {
      if (e.target.closest("a")) fechar();
    });
    // Fecha se o ecrã passar a largura de desktop
    matchMedia("(min-width: 48rem)").addEventListener("change", fechar);
  }

  // Ano atual no rodapé (o HTML já tem um valor de recurso)
  document.querySelectorAll("[data-ano]").forEach((el) => {
    el.textContent = String(new Date().getFullYear());
  });
});
