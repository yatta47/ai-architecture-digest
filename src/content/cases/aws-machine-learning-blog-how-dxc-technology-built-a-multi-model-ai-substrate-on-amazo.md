---
type: case
title: DXC OASIS：Bedrockでガバナンスを担保するマルチモデルAI基盤
title_original: How DXC Technology built a multi-model AI substrate on Amazon Bedrock
company: DXC Technology
industry: cross-industry
cloud:
- aws
patterns:
- multi-model-routing
- guardrails
- defense-in-depth
- ai-agent
components:
- Amazon Bedrock
- Amazon Bedrock Guardrails
- AWS PrivateLink
- Anthropic Claude
- Amazon Nova
outcome:
  type: risk-compliance
source_id: aws-machine-learning-blog
source_name: AWS Machine Learning Blog
source_url: https://aws.amazon.com/blogs/machine-learning/how-dxc-technology-built-a-multi-model-ai-substrate-on-amazon-bedrock/
published_at: '2026-11-11'
---

## 概要

DXCのOASISは、Bedrockの単一インターフェースでClaude、Nova、Llamaなど複数モデルを使い、基盤層でモデルアクセスを統制する。Guardrailsでコンテンツ・PII・禁止トピックを全モデル共通で適用し、PrivateLinkで推論をVPC内に閉じる。

## 設計のポイント

- エージェントに必要最小限の権限だけ持たせ、基盤層で制御する。
- Guardrailsをモデル横断で一律に適用する。
- PrivateLinkで推論トラフィックを閉域化する。

## 使いどころ

- 銀行や病院など本番サーバーを触るエージェントを運用する企業。
- 複数モデルを統制下で使い分けたい組織。
- 規制業種のAI基盤担当。
