---
type: guidance
title: ARC Zonal Shiftによる複数日AZ退避ドリルの手引き
title_original: Running multi-day AZ evacuation drills with ARC Zonal Shift
ai_relevant: false
industry: financial-services
cloud:
- aws
patterns: []
components: []
outcome:
  type: reliability
source_id: aws-architecture-blog
source_name: AWS Architecture Blog
source_url: https://aws.amazon.com/blogs/architecture/running-multi-day-az-evacuation-drills-with-arc-zonal-shift/
published_at: '2026-09-30'
---

## 概要

Amazon Application Recovery ControllerのZonal Shiftで1つのAZから48〜72時間トラフィックを退避し、N-1構成で持続運用できることを実証する手法を解説する。ECS、EKS、RDS/Aurora PostgreSQLを対象に手順と観測指標、復旧手順を示し、金融機関での運用レジリエンス要件にも触れる。
