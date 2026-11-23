---
type: announcement
title: MongoDB連携とMavenBio事例による文書処理（LlamaIndexニュースレター 2025-11-11）
title_original: LlamaIndex Newsletter 2025-11-11
company: LlamaIndex
industry: healthcare
cloud:
- aws
patterns:
- document-processing
- ai-agent
- rag
- context-engineering
components:
- LlamaParse
- MongoDB Atlas
- Amazon S3
- LlamaClassify
- LlamaExtract
- Resend
outcome:
  type: speed
source_id: llamaindex-blog
source_name: LlamaIndex Blog
source_url: https://www.llamaindex.ai/blog/llamaindex-newsletter-2025-11-11
published_at: '2025-11-11'
---

## 概要

S3、LlamaParse、MongoDB Atlas、LLMをつなぐ文書処理パイプラインの共同セッションと、メール添付を自動トリアージする財務エージェントを紹介している。MavenBioはバイオ医薬の学会ポスターや規制文書の図表を検索可能にし、ワークフローが10〜20倍高速化したという。

## 設計のポイント

- S3からパース、ベクトル検索可能なMongoDB Atlas、LLMへと流す構成で文書を洞察に変える。
- 請求書と経費精算書で異なる業務ロジックを分岐させるトリアージを設ける。
- エージェントワークフローにメモリと永続状態を持たせる。

## 使いどころ

- バイオ・製薬で図表を含む資料を検索したい研究部門。
- 受信メールの添付書類を種別ごとに処理したい経理業務。
