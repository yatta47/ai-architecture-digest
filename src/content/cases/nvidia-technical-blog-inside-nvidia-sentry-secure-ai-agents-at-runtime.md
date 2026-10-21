---
type: guidance
title: 'NVIDIA Sentry: DPU上のホスト隔離によるAIエージェント実行時防御'
title_original: 'Inside NVIDIA Sentry: Secure AI Agents at Runtime'
company: NVIDIA
industry: cross-industry
cloud:
- on-prem
patterns:
- defense-in-depth
- guardrails
- policy-as-code
- out-of-band-inference
components:
- NVIDIA Sentry
- BlueField-4
- DOCA Tower
- DOCA Argus
- Open Policy Agent
- Envoy
- NVIDIA OpenShell
outcome:
  type: risk-compliance
source_id: nvidia-technical-blog
source_name: NVIDIA Technical Blog
source_url: https://developer.nvidia.com/blog/inside-nvidia-sentry-secure-ai-agents-at-runtime/
published_at: '2026-10-21'
---

## 概要

NVIDIA SentryはBlueField-4 DPU上のホストから隔離された信頼ドメインで、エージェントの通信を検査しアクセスポリシーを強制する。DOCA TowerがTLSを終端してOPAルールで評価し、DOCA Argusがメモリを検査して、逸脱時はミリ秒で封じ込める。

## 設計のポイント

- 監視と強制をエージェントの手の届かない別ハードウェア層に置く。
- エージェントのモデルへの唯一の経路をDPUが握り、自己申告に頼らない。
- ネットワーク通信とコンテナハッシュ・SBOMなど実行時コンテキストを突き合わせてポリシー化する。
- 改ざん耐性のある証跡を保持してフォレンジックに使う。

## 使いどころ

- 自律エージェントを本番基盤で動かすセキュリティ担当。
- ホストが侵害されても監査可能性を保ちたい規制業種。
