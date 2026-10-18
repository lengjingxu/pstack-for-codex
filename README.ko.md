![pstack for Codex](assets/banner.svg)

# pstack for Codex

> 참고: 최신 채택 데이터와 커뮤니티 인용은 영어 및 중국어 README에 있습니다. 이 번역은 업데이트 중입니다.

[![validate](https://github.com/lengjingxu/pstack-for-codex/actions/workflows/validate.yml/badge.svg)](https://github.com/lengjingxu/pstack-for-codex/actions/workflows/validate.yml)
[![Stars](https://img.shields.io/github/stars/lengjingxu/pstack-for-codex?style=flat-square&color=4ade80)](https://github.com/lengjingxu/pstack-for-codex/stargazers)
[![License](https://img.shields.io/github/license/lengjingxu/pstack-for-codex?style=flat-square)](LICENSE)
[![Last commit](https://img.shields.io/github/last-commit/lengjingxu/pstack-for-codex?style=flat-square)](https://github.com/lengjingxu/pstack-for-codex/commits/main)
![Skills](https://img.shields.io/badge/skills-54-4ade80?style=flat-square)
![Playbooks](https://img.shields.io/badge/playbooks-23-4ade80?style=flat-square)
![Principles](https://img.shields.io/badge/principles-24-4ade80?style=flat-square)


**pstack for Codex** 는 Lauren Tan이 만든 [pstack](https://github.com/cursor/plugins/tree/main/pstack) 을 Codex용으로 옮긴 포트입니다. 같은 작업 방식, 같은 플레이북, 같은 원칙을 Cursor 대신 Codex에서 돌도록 다시 배선했습니다.

[English](README.md) | [中文](README.zh-CN.md) | [Français](README.fr.md) | [日本語](README.ja.md)

스킬 54개, 플레이북 23개, 원칙 24개. 이들을 라우팅하는 모드 스킬 하나.

## 관점

스킬은 호스트가 바뀌어도 살아남아야 합니다.

원본 pstack은 Cursor용이라고 분명히 밝히고 있으며, Cursor에만 있는 장치에 기대고 있습니다. 역할별 모델 slug를 받는 Task 도구, Custom Mode, `/loop`, 내장 `create-skill`, `cursor-team-kit` 보조 스킬, 그리고 `~/.cursor/rules` 아래의 규칙입니다.

이 포트는 저자의 방법을 그대로 둡니다. 플레이북, 원칙, 다중 모델 리뷰, 문장 규율, 그리고 실행 증거 없이는 완료라 하지 않는 태도는 쓰인 그대로 남습니다. 바꾸는 것은 Codex에 없는 부분뿐입니다.

이 저장소가 지키는 규칙은 하나입니다. 벤더 기능에 대응하는 Codex 원시 기능이 있으면 매핑하고, 없으면 없다고 분명히 말한 뒤 계속 진행합니다. 방법을 조용히 바꾸는 대체물을 만들어 넣지 않습니다.

## 바뀐 것

| 원본 (Cursor) | 여기 (Codex) |
| :--- | :--- |
| `Task` 도구, `subagent_type` | `spawn_agent` |
| `~/.cursor/rules/pstack-models.mdc` | `~/.codex/pstack-models.md` |
| 모델 slug `claude-opus-5-5-xhigh`, `grok-4.7-xhigh-fast` | `gpt-6-astra`, `gpt-6.1-sol` |
| `~/.cursor/projects/` 아래의 `agent-transcripts/` | `$CODEX_HOME/sessions/<YYYY>/<MM>/<DD>/rollout-*.jsonl` |
| `.cursor/skills/` | `.agents/skills/` |
| Cursor 내장 `create-skill` | `skill-creator` 스킬 |
| `AskQuestion` | `ask_user_question` |
| `/loop` | 예약 작업 또는 감시 서브에이전트 |
| Custom Mode | Codex에는 없음. 작업마다 `$poteto-mode` 호출 |
| `disable-model-invocation: true` | `policy.allow_implicit_invocation: false` |
| `cursor-team-kit`의 `deslop`, `control-cli`, `control-ui` | 셸 실행, 브라우저와 컴퓨터 도구 |
| `Make Bot UI`의 routine webhook | Codex에서 사용 불가. 문서 역할만 |

## 설치

빠른 설치:

```bash
git clone --depth 1 https://github.com/lengjingxu/pstack-for-codex.git /tmp/pstack-for-codex
bash /tmp/pstack-for-codex/scripts/install.sh
```

또는 직접 복사:

```bash
git clone https://github.com/lengjingxu/pstack-for-codex.git /tmp/pstack-for-codex

mkdir -p "$CODEX_HOME/skills/pstack/agents"
cp -R /tmp/pstack-for-codex/skills/. "$CODEX_HOME/skills/pstack/"
cp /tmp/pstack-for-codex/agents/*.md "$CODEX_HOME/skills/pstack/agents/"
```

Codex는 새 스킬을 자동으로 감지합니다. 보이지 않으면 Codex를 다시 시작하세요.

## 사용

1. `$setup-pstack` 로 추론 예산과 역할별 모델을 고르고 `~/.codex/pstack-models.md` 에 기록합니다.
2. `$poteto-mode <작업>` 이 작업을 플레이북에 맞추고, 그 단계를 할 일 목록으로 옮기고, 필요할 때 다른 스킬을 호출합니다.
3. 어떤 스킬을 쓸지 모르겠으면 `$poteto-help` 에 물어봅니다.

`setup-pstack` 을 뺀 모든 스킬은 명시적으로 호출할 때만 동작합니다. 54개를 설치해도 스킬 목록의 컨텍스트 예산을 밀어내지 않습니다.

## 원본과 다른 이름

- `tdd` 는 `pstack-tdd`
- `teach` 는 `pstack-teach`

일반적인 Codex 환경에 같은 이름의 스킬이 이미 있고, Codex는 같은 이름의 스킬을 합치지 않기 때문에 이름을 바꿨습니다.

## 알려진 제약

- `make-bot-ui` 는 Cursor의 routine webhook을 다룹니다. Codex에서는 형태만 설명하고 그렇다고 밝힙니다.
- `deslop`, `control-cli`, `control-ui` 는 Cursor의 `cursor-team-kit` 플러그인에 있으며 여기에는 없습니다. 해당 단계는 그렇다고 말하고 계속합니다.
- 역할 모델은 Codex 모델 slug입니다. `$setup-pstack` 을 실행해 실제로 쓸 수 있는 모델로 지정하세요.
- 대화 로그를 읽는 부분은 `$CODEX_HOME/sessions` 경로를 전제로 합니다.

## 구조

```
skills/                 스킬 54개. 각각 SKILL.md 와 agents/openai.yaml 포함
  poteto-mode/          라우팅 모드, 플레이북 23개와 스크립트
  principle-*/          원칙 24개. 잎 스킬로 읽음
  setup-pstack/         역할 모델과 추론 예산
agents/                 spawn_agent 에 넘기는 서브에이전트 프롬프트 2개
docs/guide/             원본 가이드의 적응판
```

## 크레딧

pstack은 [Lauren Tan](https://x.com/poteto) 의 작품이며 [cursor/plugins](https://github.com/cursor/plugins) 에 있습니다. 방법, 플레이북, 원칙, 문장은 모두 그녀의 것입니다. 이 저장소는 포트이며 사상을 바꾸지 않습니다. 호스트 배선만 바꿉니다.

라이선스는 원본과 같은 MIT입니다. [LICENSE](LICENSE) 와 [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md) 를 보세요.

## 언어

- [English](README.md)
- [简体中文](README.zh-CN.md)
- [Français](README.fr.md)
- [日本語](README.ja.md)
- [한국어](README.ko.md)
