---
type: case
title: 本番運用フェーズのCXエージェント基盤 - Lyftのルーター型マルチエージェントと自己サービス化
title_original: 'Customer Experience (CX) Agents in Production: Lessons from Lyft, Vodafone, and LATAM Airlines'
company: Lyft
industry: logistics
cloud: []
patterns:
- multi-agent-orchestration
- ai-agent
- eval
- llmops
components:
- LangGraph
- LangSmith
- Prompt Hub
- Deep Agents
outcome:
  type: productivity
source_id: langchain-blog
source_name: LangChain Blog
source_url: https://www.langchain.com/blog/customer-experience-cx-agents-in-production-lessons-from-lyft-vodafone-and-latam-airlines
published_at: '2026-08-04'
---

## 概要

Lyftは月間270万件超の問い合わせに対応するAI Assistを、LangGraphベースのルーター型マルチエージェント構成で本番運用している。損害賠償など高難度業務は機械学習エンジニアが作る専門エージェントに、それ以外は非エンジニアがJSON設定とプロンプトだけで作れる設定可能エージェントに分離することで、新規エージェントの開発期間を約6か月から約2週間へ短縮した。プラットフォームが使いやすくなるにつれてプロンプト・評価の質がボトルネックとなり、構造化されたプロンプト作成フレームワークと自動チェックを導入している。

## 設計のポイント

- メタエージェントが受信リクエストを分類し、ライダー用・ドライバー用など専門サブエージェント（LangGraphのサブグラフ）へルーティングする
- 会話途中でより専門的なハンドラが必要と判明した場合はメタエージェントに制御を戻して再ルーティングし、誤った経路に流れ続けるのを防ぐ
- 高難度・高リスクな業務は機械学習エンジニアが構築する専門エージェント、それ以外はドメイン専門家がJSON設定とプロンプトだけで構築できる設定可能エージェントに分離する二層アーキテクチャを採用する
- 非エンジニアの参加が増えるにつれてevalsを共通言語とし、矛盾する指示や未対応の会話パスを本番投入前に自動チェックで検出する

## 使いどころ

- 大量かつ多様な問い合わせに対応するカスタマーサポート組織が、エンジニアを介さず現場チームだけで新しいサポートエージェントを迅速に立ち上げたい場合
- 損害賠償請求のように情報収集・ツール呼び出し・不正判定・説明までを一貫して自動化する必要がある高難度ワークフロー
- 非エンジニアがプロンプトや評価基準の作成に参加し、エージェントの品質管理・出荷判断に関与する体制を構築したい場合
