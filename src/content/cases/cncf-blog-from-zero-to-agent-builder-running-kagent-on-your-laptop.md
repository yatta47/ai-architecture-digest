---
type: guidance
title: kagentでエージェントを作るエージェントをノートPC上のKubernetesで動かす
title_original: 'From zero to agent builder: running kagent on your laptop'
company: Solo.io
industry: cross-industry
cloud:
- on-prem
patterns:
- ai-agent
- multi-model-routing
- policy-as-code
components:
- kagent
- Kubernetes
- kind
- Helm
- Ollama
- qwen3-coder
- A2A
outcome:
  type: productivity
source_id: cncf-blog
source_name: CNCF Blog
source_url: https://www.cncf.io/blog/2026/10/12/from-zero-to-agent-builder-running-kagent-on-your-laptop/
published_at: '2026-10-12'
---

## 概要

CNCFのkagentでは、エージェントをKubernetesのカスタムリソースとして定義でき、エージェントを作るエージェントも1種類のYAMLを書けるエージェントとして構成できる。kindとOllamaでノートPC上に構築する手順で、ローカルモデルの選定と最小権限のツールサーバ設定も扱う。

## 設計のポイント

- ツールサーバのRBACを読み取り専用にし、kagent.devのagentsだけ作成・更新できるよう追加して、cluster-adminを避ける。
- YAMLを生成して適用するツール呼び出しは小型モデルでは失敗しやすく、qwen3-coder:30bのみ全回で成功した。
- 認証や共有クラスタ向けのセキュリティはあえて対象外とし、本番化の課題として明示する。

## 使いどころ

- エージェント基盤のセルフサービス化を低コストで試作したいプラットフォームチーム。
- Kubernetesネイティブにエージェントを管理する方針を検討する場面。
