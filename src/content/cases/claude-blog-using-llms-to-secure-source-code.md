---
type: guidance
title: Claude Opusでソースコードの脆弱性を発見・検証・修正する『ディフェンダーループ』
title_original: Using LLMs to secure source code
company: Anthropic
industry: cross-industry
cloud: []
patterns:
- ai-agent
- guardrails
- human-in-the-loop
components:
- Claude Opus
outcome:
  type: risk-compliance
source_id: claude-blog
source_name: Claude Blog
source_url: https://claude.com/blog/using-llms-to-secure-source-code
published_at: '2026-05-27'
---

## 概要

セキュリティチームがClaude Opusで脅威モデル構築・脆弱性発見・検証・トリアージ・パッチ適用を回す「ディフェンダーループ」のベストプラクティスガイド。発見は並列化が容易になった一方でボトルネックは検証・トリアージ・パッチ適用に移ったとし、脅威モデルの整備度が誤検知率を大きく左右すると報告している。

## 設計のポイント

- コードとドキュメント、脆弱性履歴からブートストラップした脅威モデル（信頼境界・資産・過去のバグの傾向）を先に作り、発見のスコープ設定とトリアージの重大度較正の両方に使う
- 脅威モデルが整備されているシステムでは指摘の90%が実際にエクスプロイト可能だったという結果から、脅威モデルの質が発見精度を左右すると位置づける
- 発見→検証→トリアージ→パッチという反復ループを回し、初回実行が最も指摘が多く以降は複雑だが少数の指摘に収束することを前提に運用する
- THREAT_MODEL.mdをリポジトリに含めて発見エージェントに事前に読ませ、既知の非問題をスキップさせる

## 使いどころ

- 大規模コードベースで脆弱性発見を並列化したいが、検証・トリアージ・修正の人的ボトルネックに悩むセキュリティチーム
- 誤検知率の高さに困っているチームが、脅威モデル整備によって精度を改善したい場面
