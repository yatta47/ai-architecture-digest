---
type: guidance
title: 液冷AIファクトリーの漏液対応をITと設備系で連携させるMission Control
title_original: Manage Liquid-Cooled AI Factories with NVIDIA Mission Control
ai_relevant: false
company: NVIDIA
industry: cross-industry
cloud:
- on-prem
patterns: []
components: []
outcome:
  type: reliability
source_id: nvidia-technical-blog
source_name: NVIDIA Technical Blog
source_url: https://developer.nvidia.com/blog/manage-liquid-cooled-ai-factories-with-nvidia-mission-control/
published_at: '2026-11-25'
---

## 概要

NVIDIA Mission ControlはMQTTでビル管理システムと接続し、漏液の場所と影響台数に応じた対応ポリシーをBMC・クラスタマネージャ・BMSにまたがって実行する。電力・冷却・漏液の監視はラック単位のコマンドとPrometheus/Grafanaで統合する。
