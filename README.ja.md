![pstack for Codex](assets/banner.svg)

# pstack for Codex

[![validate](https://github.com/lengjingxu/pstack-for-codex/actions/workflows/validate.yml/badge.svg)](https://github.com/lengjingxu/pstack-for-codex/actions/workflows/validate.yml)
[![Stars](https://img.shields.io/github/stars/lengjingxu/pstack-for-codex?style=flat-square&color=4ade80)](https://github.com/lengjingxu/pstack-for-codex/stargazers)
[![License](https://img.shields.io/github/license/lengjingxu/pstack-for-codex?style=flat-square)](LICENSE)
[![Last commit](https://img.shields.io/github/last-commit/lengjingxu/pstack-for-codex?style=flat-square)](https://github.com/lengjingxu/pstack-for-codex/commits/main)
![Skills](https://img.shields.io/badge/skills-54-4ade80?style=flat-square)
![Playbooks](https://img.shields.io/badge/playbooks-23-4ade80?style=flat-square)
![Principles](https://img.shields.io/badge/principles-24-4ade80?style=flat-square)


**pstack for Codex** は、Lauren Tan による [pstack](https://github.com/cursor/plugins/tree/main/pstack) を Codex 向けに移植したものです。同じ仕事の進め方、同じプレイブック、同じ原則を、Cursor ではなく Codex で動くように配線し直しています。

[English](README.md) | [中文](README.zh-CN.md) | [Français](README.fr.md) | [한국어](README.ko.md)

スキル 54 個、プレイブック 23 個、原則 24 個。それらを振り分けるモードスキルが 1 つ。

## 立場

スキルはホストが変わっても生き残るべきです。

本家 pstack は Cursor 向けだと明言しており、Cursor にしかない仕組みに依存しています。役割ごとのモデル slug を取る Task ツール、Custom Mode、`/loop`、組み込みの `create-skill`、`cursor-team-kit` の補助スキル、そして `~/.cursor/rules` のルールです。

この移植は作者の方法をそのまま保ちます。プレイブック、原則、複数モデルでのレビュー、文章の規律、そして実行時の証拠なしに完了と言わない姿勢は、すべて書かれたままです。置き換えるのは Codex に存在しない部分だけです。

このリポジトリが守る規則は 1 つです。ベンダー固有の機能に対応する Codex のプリミティブがあればそれに写し、なければ無いと明言して続行する。方法を黙って変えてしまう代替品をでっち上げないこと。

## 変更点

| 本家（Cursor） | ここ（Codex） |
| :--- | :--- |
| `Task` ツール、`subagent_type` | `spawn_agent` |
| `~/.cursor/rules/pstack-models.mdc` | `~/.codex/pstack-models.md` |
| モデル slug `claude-opus-5-5-xhigh`、`grok-4.7-xhigh-fast` | `gpt-6-astra`、`gpt-6.1-sol` |
| `~/.cursor/projects/` 配下の `agent-transcripts/` | `$CODEX_HOME/sessions/<YYYY>/<MM>/<DD>/rollout-*.jsonl` |
| `.cursor/skills/` | `.agents/skills/` |
| Cursor 組み込みの `create-skill` | `skill-creator` スキル |
| `AskQuestion` | `ask_user_question` |
| `/loop` | スケジュールされたタスク、または監視サブエージェント |
| Custom Mode | Codex には無い。タスクごとに `$poteto-mode` を呼ぶ |
| `disable-model-invocation: true` | `policy.allow_implicit_invocation: false` |
| `cursor-team-kit` の `deslop`、`control-cli`、`control-ui` | シェル実行、ブラウザとコンピュータの操作 |
| `Make Bot UI` の routine webhook | Codex では利用不可。ドキュメントのみ |

## インストール

```bash
git clone https://github.com/lengjingxu/pstack-for-codex.git /tmp/pstack-for-codex

mkdir -p "$CODEX_HOME/skills/pstack/agents"
cp -R /tmp/pstack-for-codex/skills/. "$CODEX_HOME/skills/pstack/"
cp /tmp/pstack-for-codex/agents/*.md "$CODEX_HOME/skills/pstack/agents/"
```

Codex は新しいスキルを自動で検出します。表示されない場合は Codex を再起動してください。

## 使い方

1. `$setup-pstack` で推論の予算と役割ごとのモデルを選び、`~/.codex/pstack-models.md` に書き出します。
2. `$poteto-mode <タスク>` がタスクをプレイブックに照合し、その手順を todo リストに写し、必要に応じて他のスキルを呼びます。
3. どのスキルを使うか迷ったら `$poteto-help` に聞きます。

`setup-pstack` 以外のすべてのスキルは明示的に呼び出したときだけ動きます。54 個入れてもスキル一覧のコンテキスト予算を圧迫しません。

## 本家と異なる名前

- `tdd` は `pstack-tdd`
- `teach` は `pstack-teach`

一般的な Codex 環境には同名のスキルがすでにあり、Codex は同名スキルを統合しないため改名しています。

## 既知の制限

- `make-bot-ui` は Cursor の routine webhook を操作します。Codex では形だけを説明し、その旨を明記します。
- `deslop`、`control-cli`、`control-ui` は Cursor の `cursor-team-kit` プラグインにあり、ここには含まれません。該当する手順はその旨を述べて続行します。
- 役割のモデルは Codex のモデル slug です。`$setup-pstack` を実行し、実際に使えるモデルを指定してください。
- 会話ログを読む処理は `$CODEX_HOME/sessions` のパスを前提にしています。

## 構成

```
skills/                 54 スキル。各々 SKILL.md と agents/openai.yaml を持つ
  poteto-mode/          振り分けモード、23 のプレイブックとスクリプト
  principle-*/          24 の原則。葉として読む
  setup-pstack/         役割モデルと推論予算
agents/                 spawn_agent に渡す 2 つのサブエージェント用プロンプト
docs/guide/             本家ガイドの適応版
```

## クレジット

pstack は [Lauren Tan](https://x.com/poteto) の作品で、[cursor/plugins](https://github.com/cursor/plugins) にあります。方法、プレイブック、原則、文章はすべて彼女のものです。このリポジトリは移植であり、思想を変えるものではありません。変えるのはホスト側の配線だけです。

ライセンスは本家と同じ MIT です。[LICENSE](LICENSE) と [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md) を参照してください。

## 言語

- [English](README.md)
- [简体中文](README.zh-CN.md)
- [Français](README.fr.md)
- [日本語](README.ja.md)
- [한국어](README.ko.md)

