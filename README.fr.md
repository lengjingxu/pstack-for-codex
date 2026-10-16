# pstack for Codex

**pstack for Codex** est un portage pour Codex de [pstack](https://github.com/cursor/plugins/tree/main/pstack), écrit par Lauren Tan. Même méthode de travail, mêmes playbooks, mêmes principes, recâblés pour tourner sur Codex plutôt que sur Cursor.

[English](README.md) | [中文](README.zh-CN.md) | [日本語](README.ja.md) | [한국어](README.ko.md)

54 compétences. 23 playbooks. 24 principes. Une compétence de mode qui route les autres.

## Position

Une compétence doit survivre à un changement d'hôte.

pstack en amont assume d'être écrit pour Cursor, et s'appuie sur des mécanismes que seul Cursor fournit : l'outil Task avec des slugs de modèle par rôle, les Custom Modes, `/loop`, le `create-skill` intégré, les aides de `cursor-team-kit`, et les règles sous `~/.cursor/rules`.

Ce portage laisse la méthode de l'autrice intacte. Les playbooks, les principes, les panels de relecture, la discipline d'écriture et le refus de déclarer un travail terminé sans preuve d'exécution restent tels quels. Seules les pièces absentes de Codex sont remplacées.

La règle que ce dépôt s'impose : faire correspondre une fonctionnalité du vendeur à une primitive Codex quand il en existe une, et quand il n'en existe pas, le dire clairement et continuer. Ne jamais inventer un substitut qui modifierait la méthode en silence.

## Ce qui a changé

| Amont (Cursor) | Ici (Codex) |
| :--- | :--- |
| Outil `Task`, `subagent_type` | `spawn_agent` |
| `~/.cursor/rules/pstack-models.mdc` | `~/.codex/pstack-models.md` |
| Slugs `claude-opus-5-5-xhigh`, `grok-4.7-xhigh-fast` | `gpt-6-astra`, `gpt-6.1-sol` |
| `agent-transcripts/` sous `~/.cursor/projects/` | `$CODEX_HOME/sessions/<YYYY>/<MM>/<DD>/rollout-*.jsonl` |
| `.cursor/skills/` | `.agents/skills/` |
| `create-skill` intégré à Cursor | la compétence `skill-creator` |
| `AskQuestion` | `ask_user_question` |
| `/loop` | une tâche planifiée ou un sous-agent surveillant |
| Custom Modes | absents de Codex, invoquez `$poteto-mode` par tâche |
| `disable-model-invocation: true` | `policy.allow_implicit_invocation: false` |
| `cursor-team-kit` : `deslop`, `control-cli`, `control-ui` | exécution shell, outils navigateur et ordinateur |
| Webhooks de routine de `Make Bot UI` | indisponibles sur Codex, documentation seulement |

## Installation

```bash
git clone https://github.com/lengjingxu/pstack-for-codex.git /tmp/pstack-for-codex

mkdir -p "$CODEX_HOME/skills/pstack/agents"
cp -R /tmp/pstack-for-codex/skills/. "$CODEX_HOME/skills/pstack/"
cp /tmp/pstack-for-codex/agents/*.md "$CODEX_HOME/skills/pstack/agents/"
```

Codex détecte les nouvelles compétences automatiquement. Si elles n'apparaissent pas, redémarrez Codex.

## Utilisation

1. `$setup-pstack` choisit un budget de raisonnement et un modèle par rôle, puis écrit `~/.codex/pstack-models.md`.
2. `$poteto-mode <tâche>` associe la tâche à un playbook, copie ses étapes dans la liste de tâches et lance les autres compétences selon les besoins.
3. `$poteto-help` répond quand vous hésitez sur la compétence à utiliser.

Toutes les compétences sauf `setup-pstack` ne s'activent que sur invocation explicite : installer 54 compétences ne fait donc pas exploser le budget de contexte de la liste.

## Noms différents de l'amont

- `tdd` devient `pstack-tdd`
- `teach` devient `pstack-teach`

Renommées parce qu'une installation Codex classique possède déjà des compétences de ces noms, et que Codex ne fusionne pas les compétences homonymes.

## Limites connues

- `make-bot-ui` pilote les webhooks de routine de Cursor. Sur Codex, elle ne documente que la forme et le dit.
- `deslop`, `control-cli` et `control-ui` appartiennent au plugin `cursor-team-kit` de Cursor et sont absents ici. Les étapes concernées le signalent et continuent.
- Les modèles de rôle sont des slugs Codex. Lancez `$setup-pstack` pour les pointer sur ce dont vous disposez.
- Les lecteurs de transcriptions attendent les journaux de session Codex sous `$CODEX_HOME/sessions`.

## Arborescence

```
skills/                 54 compétences, chacune avec SKILL.md et agents/openai.yaml
  poteto-mode/          le mode de routage, ses 23 playbooks et ses scripts
  principle-*/          les 24 principes, lus comme feuilles
  setup-pstack/         modèles par rôle et budget de raisonnement
agents/                 les deux prompts de sous-agent passés à spawn_agent
docs/guide/             le guide amont, adapté
```

## Crédits

pstack est de [Lauren Tan](https://x.com/poteto) et vit dans [cursor/plugins](https://github.com/cursor/plugins). La méthode, les playbooks, les principes et le texte sont d'elle. Ce dépôt est un portage : il change le câblage de l'hôte et laisse la pensée intacte.

Licence MIT, comme l'amont. Voir [LICENSE](LICENSE) et [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md).

## Langues

- [English](README.md)
- [简体中文](README.zh-CN.md)
- [Français](README.fr.md)
- [日本語](README.ja.md)
- [한국어](README.ko.md)

