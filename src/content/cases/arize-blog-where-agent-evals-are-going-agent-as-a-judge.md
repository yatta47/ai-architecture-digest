---
type: opinion
title: エージェント評価はAgent-as-a-Judgeへ移行する
title_original: 'Where agent evals are going: Agent-as-a-Judge'
industry: cross-industry
cloud: []
patterns:
- eval
- ai-agent
components: []
outcome:
  type: quality
source_id: arize-blog
source_name: Arize Blog
source_url: https://arize.com/blog/agent-as-a-judge-agentic-evaluation/
published_at: '2026-08-19'
---

## 概要

エージェントは単一の出力ではなくツール呼び出しを含む軌跡（トラジェクトリ）の中で失敗するため、最終出力だけを採点する従来のLLM-as-a-Judgeでは検知できない不具合が多いと指摘する。Meta AI/KAUSTの研究では、トレースを調査できるAgent-as-a-Judgeが人間専門家の合意率を上回りつつコストも人手評価の1/40程度に抑えられたことを紹介し、評価戦略の階層の中にエージェント型ジャッジを位置づけるべきだと論じる。

## 設計のポイント

- 失敗が最終出力ではなく中間のツール呼び出しや意思決定の中に潜むエージェントには、トレース調査可能な評価者を充てる
- 評価エージェントに記憶を持たせると初期の誤判定が後続判断に伝播するため、毎回フレッシュな証拠収集をさせる設計の方が精度が高い
- 決定論的な安価な評価器から始め、LLM-as-a-Judge、Agent-as-a-Judgeへと段階的にコストと精度をトレードオフする階層型eval戦略を組む

## 使いどころ

- ツール呼び出しを伴うエージェントの本番運用で、最終応答だけでは見抜けない失敗モードを検知したいチーム
- 人手による評価コストや評価者間のばらつきを削減したいエージェント開発・QA組織
- 医療・法律・金融など専門ドメインでドメイン特化のジャッジエージェントを検討する場面
