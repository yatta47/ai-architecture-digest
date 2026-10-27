---
type: case
title: Nitro Enclavesで検証可能なトランザクション解析（VisualSign）
title_original: How Anchorage Digital and Turnkey verify code with AWS Nitro Enclaves
ai_relevant: false
company: Anchorage Digital / Turnkey
industry: financial-services
cloud:
- aws
patterns: []
components: []
outcome:
  type: risk-compliance
source_id: aws-architecture-blog
source_name: AWS Architecture Blog
source_url: https://aws.amazon.com/blogs/architecture/how-anchorage-digital-and-turnkey-verify-code-with-aws-nitro-enclaves/
published_at: '2026-10-27'
---

## 概要

Anchorage DigitalとTurnkeyは、ブロックチェーン取引を人が読める形に変換するパーサーVisualSignをNitro Enclaves内で動かし、実行コードの正しさと出力の完全性を証明する仕組みを作った。ブラインドサイニングによるフィッシング対策になる。
