---
type: case
title: 1億2100万台の同時gRPC接続を支えたDNSルーティング設計変更
title_original: How bitdrift scaled to 121 million concurrent gRPC connections on Amazon CloudFront for live telemetry sporting
  events
ai_relevant: false
company: bitdrift
industry: media
cloud:
- aws
patterns: []
components: []
outcome:
  type: reliability
source_id: aws-architecture-blog
source_name: AWS Architecture Blog
source_url: https://aws.amazon.com/blogs/architecture/how-bitdrift-scaled-to-121-million-concurrent-grpc-connections-on-amazon-cloudfront-for-live-telemetry-sporting-events/
published_at: '2026-07-15'
---

## 概要

モバイルオブザーバビリティ企業bitdriftは、T20ワールドカップの試合開始直後に数千万台規模のgRPC接続が急増し、CloudFrontとNLB間でエラーが多発する問題に直面した。原因はRoute 53のWeighted RoutingがDNSクエリ1回につきIPを1つしか返さず、TTL期間中すべてのCloudFrontエッジが同一オリジンに集中する「サンダリングハード」現象で、Multi-Value Answer Routing（1回のクエリで最大8IPを返す）への切り替えのみで、1億2100万台・ゼロエラーの負荷分散を実現した。
