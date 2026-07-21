---
type: case
title: Cisco発、Worker/Leaderエージェント群でソフトウェア配信全体を協調させる「Agentic Engineering」基盤
title_original: 'Agentic Engineering: How Swarms of AI Agents Are Redefining Software Engineering'
company: Cisco
industry: cross-industry
cloud: []
patterns:
- multi-agent-orchestration
- root-cause-analysis
- ci-cd
- context-engineering
components:
- LangChain
- LangGraph
- LangSmith
- A2A
- MCP
outcome:
  type: productivity
source_id: langchain-blog
source_name: LangChain Blog
source_url: https://www.langchain.com/blog/agentic-engineering-redefining-software-engineering
published_at: '2026-06-25'
---

## 概要

Ciscoのエンジニアが、LangGraphとLangSmithを用いてWorker Agent（実行担当）とLeader Agent（統率・共有基盤）の2層からなるマルチエージェント協調フレームワーク「Agentic Engineering」を構築した。コーディングAIが単一セッションでコード生成を高速化するのに対し、この仕組みは要件定義から運用までのソフトウェア配信ライフサイクル全体を横断的にオーケストレーションする制御プレーンとして機能する。20件超のデバッグワークフローのパイロットではroot cause特定までの時間を93%短縮し、月間512セッションで200時間超のエンジニアリング工数を削減、開発ワークフローでも実行時間を65%短縮した。

## 設計のポイント

- Worker Agent（自律実行）とLeader Agent（統率・共有基盤）の2層構造にすることで、エッジでの自律性とスワーム全体の一貫性を両立させる
- エージェント間通信は基本A2Aプロトコルに統一し、A2A非対応のエージェントはMCPラッパー経由で接続することで異種エージェントを疎結合に統合する
- Leader Agentが共有プロンプト/ワークフローライブラリ・共通ツールゲートウェイ・スワーム共有の長期記憶・グローバル可観測性を提供し、チーム間の再利用とオンボーディングを効率化する
- コーディングAIエージェント（Codex等）をWorker Agent内部の推論・コード生成エンジンとして組み込み、既存のコーディングAIと競合させず上位の協調レイヤーとして統合する

## 使いどころ

- デバッグの根本原因特定を大幅に高速化したいチーム（実績: time-to-root-cause 93%削減）
- 要件定義からデプロイ・運用まで複数チームにまたがるソフトウェア配信を横断的にオーケストレーションしたい大規模エンジニアリング組織
- 単一セッション型のコーディングAIエージェントを、長期記憶とトレーサビリティを持つ上位のワークフロー制御層に統合したい場合
- 標準化されたプロンプト/ワークフローライブラリで新メンバーのエージェント活用オンボーディングを加速したいケース
