![pstack for Codex](assets/banner.svg)

# pstack for Codex

[![Stars](https://img.shields.io/github/stars/lengjingxu/pstack-for-codex?style=flat-square&color=4ade80)](https://github.com/lengjingxu/pstack-for-codex/stargazers)
[![License](https://img.shields.io/github/license/lengjingxu/pstack-for-codex?style=flat-square)](LICENSE)
[![Last commit](https://img.shields.io/github/last-commit/lengjingxu/pstack-for-codex?style=flat-square)](https://github.com/lengjingxu/pstack-for-codex/commits/main)
![Skills](https://img.shields.io/badge/skills-54-4ade80?style=flat-square)
![Playbooks](https://img.shields.io/badge/playbooks-23-4ade80?style=flat-square)
![Principles](https://img.shields.io/badge/principles-24-4ade80?style=flat-square)


**pstack for Codex** 是 [pstack](https://github.com/cursor/plugins/tree/main/pstack)（作者 Lauren Tan）的 Codex 移植版。同一套工作方法，同一批 playbook，同一批原则，只把运行宿主从 Cursor 换成 Codex。

[English](README.md) | [Français](README.fr.md) | [日本語](README.ja.md) | [한국어](README.ko.md)

54 个技能，23 个 playbook，24 条原则，一个负责路由的模式技能。

## 立场

技能应当能换宿主。

上游 pstack 明确说明它为 Cursor 而写，并且依赖只有 Cursor 才有的机制：带角色模型 slug 的 Task 工具、Custom Mode、`/loop`、内置 `create-skill`、`cursor-team-kit` 辅助技能，以及 `~/.cursor/rules` 下的规则。

这次移植不改作者的方法。playbook、原则、多模型评审、文字纪律，以及「没有运行证据就不算完成」这条底线，都按原样保留。只替换 Codex 上不存在的那部分。

本仓库遵守一条规则：能在 Codex 找到对应原语的，就做映射；找不到的，就明说并继续，绝不用一个会悄悄改变方法的替代品来充数。

## 改了什么

| 上游（Cursor） | 这里（Codex） |
| :--- | :--- |
| `Task` 工具、`subagent_type` | `spawn_agent` |
| `~/.cursor/rules/pstack-models.mdc` | `~/.codex/pstack-models.md` |
| 模型 slug `claude-opus-5-5-xhigh`、`grok-4.7-xhigh-fast` | `gpt-6-astra`、`gpt-6.1-sol` |
| `~/.cursor/projects/` 下的 `agent-transcripts/` | `$CODEX_HOME/sessions/<YYYY>/<MM>/<DD>/rollout-*.jsonl` |
| `.cursor/skills/` | `.agents/skills/` |
| Cursor 内置 `create-skill` | `skill-creator` 技能 |
| `AskQuestion` | `ask_user_question` |
| `/loop` | 定时任务或监听子代理 |
| Custom Mode | Codex 没有，按任务调用 `$poteto-mode` |
| `disable-model-invocation: true` | `policy.allow_implicit_invocation: false` |
| `cursor-team-kit` 的 `deslop`、`control-cli`、`control-ui` | shell 执行、浏览器与电脑操作 |
| `Make Bot UI` 的 routine webhook | Codex 上不可用，仅作文档 |

## 安装

```bash
git clone https://github.com/lengjingxu/pstack-for-codex.git /tmp/pstack-for-codex

mkdir -p "$CODEX_HOME/skills/pstack/agents"
cp -R /tmp/pstack-for-codex/skills/. "$CODEX_HOME/skills/pstack/"
cp /tmp/pstack-for-codex/agents/*.md "$CODEX_HOME/skills/pstack/agents/"
```

Codex 会自动发现新技能。如果没有出现，重启 Codex。

## 使用

1. `$setup-pstack`：选择推理档位并为每个角色指定模型，写入 `~/.codex/pstack-models.md`。
2. `$poteto-mode <任务>`：把任务匹配到某个 playbook，将其步骤复制进待办列表，并按需调用其他技能。
3. `$poteto-help`：不确定该用哪个技能时用它。

除 `setup-pstack` 外，所有技能都只在显式调用时生效，所以装 54 个技能不会撑爆技能列表的上下文预算。

## 与上游不同的命名

- `tdd` 改为 `pstack-tdd`
- `teach` 改为 `pstack-teach`

原因是常见的 Codex 环境里已存在同名技能，而 Codex 不会合并同名技能。

## 已知限制

- `make-bot-ui` 依赖 Cursor 的 routine webhook。在 Codex 上只描述结构，并在文中说明。
- `deslop`、`control-cli`、`control-ui` 属于 Cursor 的 `cursor-team-kit` 插件，这里没有。用到它们的步骤会说明并继续。
- 角色模型使用 Codex 的模型 slug，请运行 `$setup-pstack` 指向你实际可用的模型。
- 读取会话记录的部分按 `$CODEX_HOME/sessions` 的路径。

## 目录结构

```
skills/                 54 个技能，每个含 SKILL.md 与 agents/openai.yaml
  poteto-mode/          路由模式、23 个 playbook 及其脚本
  principle-*/          24 条原则，按叶子技能读取
  setup-pstack/         角色模型与推理档位
agents/                 交给 spawn_agent 的两个子代理提示词
docs/guide/             上游指南，已适配
```

## 致谢

pstack 由 [Lauren Tan](https://x.com/poteto) 创作，位于 [cursor/plugins](https://github.com/cursor/plugins)。方法、playbook、原则与文字都出自她。本仓库是移植，不是改主张：只改宿主接线，不动思考方式。

MIT 许可，与上游一致。见 [LICENSE](LICENSE) 与 [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md)。

## 语言

- [English](README.md)
- [简体中文](README.zh-CN.md)
- [Français](README.fr.md)
- [日本語](README.ja.md)
- [한국어](README.ko.md)

