---
type: case
title: 機密コードを扱うためのガバナンス型コーディングエージェント基盤
title_original: 'Deep Agents Code on NemoClaw: a governed blueprint for your most sensitive code'
company: LangChain / NVIDIA
industry: cross-industry
cloud:
- on-prem
patterns:
- ai-agent
- guardrails
- human-in-the-loop
- defense-in-depth
components:
- Deep Agents Code (dcode)
- Nemotron 3 Ultra
- NemoClaw
- OpenShell
outcome:
  type: risk-compliance
source_id: langchain-blog
source_name: LangChain Blog
source_url: https://www.langchain.com/blog/deep-agents-code-on-nemoclaw-a-governed-blueprint-for-your-most-sensitive-code
published_at: '2026-07-08'
---

## 概要

LangChainのオープンソースコーディングエージェントdcodeを、NVIDIAのオープンモデルNemotron 3 UltraとブループリントNemoClaw上で稼働させ、OpenShellサンドボックス内でデフォルト拒否のネットワーク制御・人間承認・監査ログ付きで実行する構成を紹介する。COBOLなどのレガシー資産のモダナイゼーションを主要ユースケースとし、ソースコードと推論基盤を自社インフラ内に留めたまま安全にコーディングエージェントを使えるようにする。

## 設計のポイント

- コーディングエージェントをOpenShellサンドボックス内で実行し、ネットワークアクセスをデフォルト拒否・許可制にする
- オープンモデル(Nemotron 3 Ultra)とオープンハーネス(dcode)を採用し、モデルとハーネスの両方を自社で監査・チューニング・置換できるようにする
- 機密操作には人間の承認を必須とし、セッションごとにスナップショットと監査ログを残す
- レガシーコードの現状把握→ドメイン分割→段階的リファクタリング→レビューという小さく検証可能な波(wave)単位で移行を進める

## 使いどころ

- COBOLなど有識者が減っているレガシー資産をモダナイズしたい規制業界のチーム
- ソースコードや推論基盤を自社インフラ内に留めたい情報統制の厳しい企業
- 定型的なコードベース作業をエンジニアに任せるガバナンス型の社内コーディングアシスタントを構築したいチーム
