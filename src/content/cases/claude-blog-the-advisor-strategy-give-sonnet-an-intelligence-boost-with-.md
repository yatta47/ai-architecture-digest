---
type: announcement
title: 実行役Sonnet/Haiku×助言役OpusでAPI一発呼び出しの低コスト高精度化「advisorツール」
title_original: 'The advisor strategy: Give agents an intelligence boost'
company: Anthropic
industry: cross-industry
cloud: []
patterns:
- multi-model-routing
- reasoning-computation-separation
- cost-optimization
components:
- Claude Platform
- Messages API
- advisor tool
- Claude Opus 4.6
- Claude Sonnet 4.6
- Claude Haiku 4.5
outcome:
  type: cost
source_id: claude-blog
source_name: Claude Blog
source_url: https://claude.com/blog/the-advisor-strategy
published_at: '2026-04-09'
---

## 概要

Claude PlatformはSonnetやHaikuを実行役（executor）とし、判断に迷った局面だけOpusにアドバイス役（advisor）として相談させる「advisor戦略」を、advisorツールとして1行のAPI変更で使えるようにした。advisorはツール呼び出しや出力生成を行わず、共有コンテキストをもとに計画・修正・停止のいずれかを返すだけで、実行そのものは低コストなexecutorが担う。SWE-bench Multilingualでは通常のSonnet単体比でスコアが2.7ポイント向上しつつタスクあたりコストは11.9%削減され、BrowseCompではHaiku単体比でスコアが2倍以上になるなど、フロンティア級の推論を必要な局面だけに絞ることでコストと精度を両立している。

## 設計のポイント

- オーケストレータが作業を分解して複数ワーカーに委譲する従来のサブエージェント構成とは逆に、軽量なexecutorモデルが最初から最後まで駆動し、自力で解けない判断点でのみ大型モデルに相談するように設計する。
- advisor役のモデルはツール呼び出しや利用者向け出力を一切行わず、共有コンテキストを受け取って計画・修正・停止シグナルのいずれかを返すだけの純粋な助言者として定義することで、責務を明確に分離する。
- モデル間の受け渡しを単一の/v1/messagesリクエスト内で完結させ、往復や外部のコンテキスト管理を発生させないことで、レイテンシとオーケストレーション複雑性の増加を避ける。
- advisor呼び出し回数をmax_usesで上限設定し、advisorトークンをexecutorトークンと別会計でusageに計上することで、コスト管理と観測性を両立させる。

## 使いどころ

- コーディングエージェントやブラウジングエージェントのように、大半のステップは軽量モデルで十分だが一部の難所だけ最上位モデル級の判断が欲しい高頻度・高コスト感応度のタスク。
- 構造化文書抽出のように文書ごとに複雑さが大きく変動する業務で、複雑な文書のときだけ動的にモデル知性を引き上げたいケース。
- Haikuのような最安価モデルを実行役にしつつ、フロンティアモデル単体運用よりも大幅に低いコストで精度を底上げしたい大量処理タスク。
