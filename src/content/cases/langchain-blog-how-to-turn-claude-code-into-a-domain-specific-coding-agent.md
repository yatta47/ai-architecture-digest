---
type: case
title: Claude Codeをドメイン特化コーディングエージェントに変える文脈設計の実験
title_original: How to turn Claude Code into a domain specific coding agent
company: LangChain
industry: cross-industry
cloud: []
patterns:
- context-engineering
- eval
components:
- Claude Code
- MCPDoc
- Claude Sonnet 4
outcome:
  type: quality
source_id: langchain-blog
source_name: LangChain Blog
source_url: https://www.langchain.com/blog/how-to-turn-claude-code-into-a-domain-specific-coding-agent
published_at: '2026-06-15'
---

## 概要

LangChainは自社ライブラリ(LangGraph/LangChain)のコードをClaude Codeにうまく書かせるため、MCP経由のドキュメントアクセス・Claude.md による凝縮ガイド・その組み合わせという4パターンを比較実験した。タスク別の評価ハーネス(スモークテスト・タスク要件テスト・LLM-as-Judgeによるコード品質評価)で計測した結果、生ドキュメントをそのまま渡すよりも凝縮された構造化ガイドと必要時に詳細を引けるツールの組み合わせが最も高品質なコードを生んだ。

## 設計のポイント

- 生ドキュメントをそのまま与えるより、要点を凝縮した構造化ガイド(Claude.md)を基本知識として与える方が効果が高い
- 凝縮ガイドと、必要に応じて詳細ドキュメントを取得できるMCPツールを組み合わせることで両者の弱点を補い合う
- よくある失敗パターン（誤った状態更新、型の思い込み、過度に複雑な実装など）をガイドに明記し再発を防ぐ
- 機能性だけを見るPass@k的指標に頼らず、客観チェックと専門家コードを基準にしたLLM-as-Judgeを組み合わせて品質を評価する

## 使いどころ

- 社内ライブラリや新しいバージョンのAPIをコーディングエージェントにうまく使わせたいチーム
- ニッチなフレームワーク向けにコーディングエージェントの精度を上げたい開発者
