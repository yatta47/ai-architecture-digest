---
type: case
title: 臨床レビューを再利用可能な評価資産に変えるヘルスケアAIの信頼性基盤
title_original: 'The Reliability Layer for Healthcare AI: Common LangSmith Use Cases'
company: Abridge, Included Health
industry: healthcare
cloud: []
patterns:
- eval
- llmops
- guardrails
components:
- LangSmith
- LangGraph
- Deep Agents
outcome:
  type: quality
source_id: langchain-blog
source_name: LangChain Blog
source_url: https://www.langchain.com/blog/reliability-healthcare-ai-langsmith-use-cases
published_at: '2026-09-22'
---

## 概要

医療AIでは臨床専門家によるレビューが品質担保の要だが、その時間はスケールしない。AbridgeとIncluded Healthは、専門家の判断をLangSmith上でラベル付きデータセットや較正済みジャッジに変換し、リリースのたびに専門家レビューをやり直さずに済む仕組みを作った。Abridgeはリリースサイクルを1〜2カ月から数日へ短縮し、Included Healthはチャットエンゲージメントを75%向上させつつ高リスク状況の99%以上を正しくフラグ立てしている。

## 設計のポイント

- 既知の失敗モードを精度・コンプライアンス・文体・網羅性などカテゴリ別に分け失敗モードごとに個別のジャッジを構築した
- リファレンスフリーなジャッジ（会話に対する直接評価）とリファレンスベースのジャッジ（専門分野別のキュレーション例と比較）を組み合わせ網羅性と精度を両立させた
- アノテーションガイドと具体例を自動プロンプト最適化フレームワークに入力しジャッジプロンプトの手動調整を排した
- 最適化したジャッジを臨床家のアノテーションと突き合わせ不一致を検証するAlign Evaluatorで較正の妥当性を確認する

## 使いどころ

- 限られた臨床専門家の時間をリリースのたびに消費してしまう医療AIプロダクトチーム
- 行動しなかったこと（不要な介入を控えたこと）の正しさも評価したいセーフティクリティカルなエージェント
- 属性の誤帰属やハルシネーションが記録の信頼性を損なう文書生成AI（カルテ作成など）
