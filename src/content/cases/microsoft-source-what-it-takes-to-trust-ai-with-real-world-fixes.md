---
type: case
title: ネットワーク障害対応でAIエージェントを自律運用するための多層セーフガード
title_original: 'Copilot to autopilot: Why no single safeguard is enough'
company: Microsoft
industry: telecom
cloud:
- azure
patterns:
- ai-agent
- guardrails
- defense-in-depth
- human-in-the-loop
components:
- Azure Networking
outcome:
  type: risk-compliance
source_id: microsoft-source
source_name: Microsoft Source
source_url: https://commandline.microsoft.com/ai-agent-copilot-autopilot-layered-model-production-network-incidents-on-call-engineers/
published_at: '2026-10-13'
---

## 概要

本番ネットワーク障害の調査から修復までを担うエージェントについて、単一の防御では安全にならないとして、ID、認可、ツール、人間承認の層で自律範囲を限定するモデルを示す。安全性はモデルの賢さより周囲の決定論的な殻で決まるという考え方が中心。

## 設計のポイント

- エージェントはモデルを包む決定論的なソフトウェアであり、安全性はその殻で作る
- 読み取りと書き込みを区別し、本番変更には認可・ツール制約・承認を重ねる
- 単一のガードレールに頼らず層で守る

## 使いどころ

- 本番環境を変更するSRE・ネットワーク運用エージェントの設計者
- オンコール調査を自動化したい運用チーム
