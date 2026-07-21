---
type: guidance
title: LangChainのDeep Agentsが実現するプロバイダー横断プロンプトキャッシングでエージェントのトークンコストを削減
title_original: Prompt Caching with Deep Agents
company: LangChain
industry: cross-industry
cloud: []
patterns:
- ai-agent
- cost-optimization
- context-engineering
- inference-optimization
components:
- Deep Agents
- LangSmith
- Amazon Bedrock
- Claude Haiku 4.5
- GPT-5.4-mini
- Gemini 3.5 Flash
- Fireworks
outcome:
  type: cost
source_id: langchain-blog
source_name: LangChain Blog
source_url: https://www.langchain.com/blog/deep-agents-prompt-caching
published_at: '2026-06-26'
---

## 概要

LangChainのDeep Agentsは、Anthropic・OpenAI・Gemini・AWS Bedrock・Fireworksなど主要モデルプロバイダーごとに異なるプロンプトキャッシング機能を自動検出し、明示的キャッシュブレークポイントの設定やプロンプト構造の最適化によってトークンコストを削減する仕組みを提供する。Deep Agentsの評価スイートを3プロバイダーのミドルティアモデルで実行した結果、トークンコストを49〜80%削減できることを確認し、LangSmithによってキャッシュ読み取り状況やコスト削減効果を可視化できることも示している。

## 設計のポイント

- モデルプロバイダーごとに異なるキャッシング機能（明示的ブレークポイント・TTL設定・キャッシュプレウォームなど）の対応状況をハーネス側で検出し、利用可能な最適戦略へ自動的に切り替える。
- 明示的キャッシュブレークポイントが使えないプロバイダーでは、プロバイダー側の暗黙的（automatic）キャッシュに自動でフォールバックする設計にする。
- システムプロンプト・ツール定義・スキルなど変化の少ない静的プレフィックスを先頭にまとめて配置し、メモリ更新や会話圧縮が起きても静的部分だけはキャッシュヒットを維持できるようプロンプト構造とキャッシュ境界を設計する。
- LangSmithなどのトレーシングツールでリクエストごとのキャッシュ読み取りトークン数を計測し、キャッシュ戦略・会話の長さ・モデル選択それぞれによるコスト削減効果を切り分けて把握する。

## 使いどころ

- 複数のLLMプロバイダーを併用・切り替えながら運用するエージェントプロダクトで、プロバイダーごとの実装差異を意識せずにキャッシュによるコスト削減を得たいチーム。
- 長時間・多ターンにわたる会話やエージェント軌跡を扱うプロダクトで、キャッシュ再利用による累積的なコスト削減効果を最大化したい場合。
- 本番運用中のAIエージェントにおいて、トークンコストやキャッシュヒット率を可視化・計測し、継続的にコスト最適化を行いたい運用チーム。
