# 🔐 Segurança

Skills para **encontrar e corrigir falhas de segurança na tua própria app** — nunca para atacar sistemas de outros.
*Skills to find and fix security flaws in your own app — never to attack anyone else's.*

| Skill | O que faz | Fonte |
|---|---|---|
| [`app-attack-audit`](skills/app-attack-audit/SKILL.md) | Audita o teu código contra 20 ataques reais e públicos (HTTP/2 Rapid Reset, username de 52 caracteres da Okta, SAML da GitLab, nOAuth, JWT, views que contornam RLS, Unicode da Spotify…). Para cada um: se te afeta, onde está no código e a correção. Inclui uma prompt de auditoria pronta | [@murphmaxxing](https://www.instagram.com/reel/DfsWbkrB6vN/) |

Sempre: mapear a stack → classificar os 20 → correções com diff → **tu aprovas** → as 3 mais urgentes.

**Instalar esta categoria · Install this category** (Claude Code):

```
/plugin marketplace add mozuraa/claude-skills
/plugin install seguranca@mozuraa-skills
```

[← Voltar à biblioteca · Back to the library](../README.md)
