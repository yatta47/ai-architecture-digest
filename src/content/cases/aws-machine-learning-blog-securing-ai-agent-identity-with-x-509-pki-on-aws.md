---
type: guidance
title: X.509 PKIでAIエージェントの身元をゼロトラストに証明する
title_original: Securing AI agent identity with X.509 PKI on AWS
company: Keyfactor
industry: cross-industry
cloud:
- aws
patterns:
- defense-in-depth
- ai-agent
- policy-as-code
components:
- Keyfactor EJBCA
- Amazon Bedrock
- Strands Agents SDK
- MCP
- OCSP
outcome:
  type: risk-compliance
source_id: aws-machine-learning-blog
source_name: AWS Machine Learning Blog
source_url: https://aws.amazon.com/blogs/machine-learning/securing-ai-agent-identity-with-x-509-pki-on-aws/
published_at: '2026-10-20'
---

## 概要

MCPには標準の認証が無く、エージェントのなりすましや資格情報の再利用が起こり得る。EJBCAのX.509 PKIと署名付きリクエスト、ユーザー署名の委任アサーション、RFC 8693のオーディエンス限定トークン、OCSP失効確認を組み合わせた参照アーキテクチャを示す。

## 設計のポイント

- 全リクエストに署名エンベロープを付け、鍵の所持証明でどのエージェントの呼び出しかを検証する。
- ユーザーが署名した委任アサーションで、資格情報を共有せずエージェントに権限を委譲する。
- オーディエンス限定トークンとリアルタイムOCSPで、漏えい時の影響範囲と失効の反映遅延を小さくする。

## 使いどころ

- MCPツールサーバーでデータベースや業務APIを扱う、規制の厳しい企業。
- 複数エージェントが連鎖するシステムで、APIキー共有やトークン転送を排したい場面。
