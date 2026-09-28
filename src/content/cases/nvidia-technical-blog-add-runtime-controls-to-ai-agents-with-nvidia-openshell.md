---
type: announcement
title: 既存エージェントを書き換えずに権限を外側から制御するランタイム（NVIDIA OpenShell）
title_original: Add Runtime Controls to AI Agents with NVIDIA OpenShell
company: NVIDIA
industry: cross-industry
cloud: []
patterns:
- guardrails
- ai-agent
- policy-as-code
components:
- NVIDIA OpenShell
- OpenShell Gateway
- OpenShell Supervisor
- OpenShell Sandbox
outcome:
  type: risk-compliance
source_id: nvidia-technical-blog
source_name: NVIDIA Technical Blog
source_url: https://developer.nvidia.com/blog/add-runtime-controls-to-ai-agents-with-nvidia-openshell/
published_at: '2026-09-28'
---

## 概要

NVIDIA OpenShell 0.1.0は、既存のAIエージェントを書き換えることなく、アクセス可能なシステムやデータをエージェント外部から制御するオープンソースランタイム。Gateway・Supervisor・Sandboxの3コンポーネントでサンドボックス実行・権限のフォーマル検証・資格情報保護を提供し、Cadence（チップ設計）やSlack（業務自動化）、Gecko Robotics（物理ロボット制御）などが採用している。

## 設計のポイント

- Supervisorをサンドボックスの外側でエージェントとペアにし、HTTP/GraphQL/MCPの送信リクエストをポリシーと照合してから通す構成で、エージェント本体は無改造のまま制御を追加する。
- カーネルレベルのファイルシステム・プロセス制御とネットワーク経路の限定（Supervisor経由のみ）により、シェル実行や子プロセス起動、サブエージェントへの委譲時も一貫して制限を適用する。
- 形式手法によるポリシー検証で、申請された権限が定義済みの境界内に収まるかを人間・AI双方のレビュアーに提示する。

## 使いどころ

- 長時間動作する自律エージェントに資格情報やAPIアクセスを与えつつ、書き込み操作だけを制限するなど細粒度のガバナンスをかけたい場合。
- チップ設計・業務自動化・物理ロボット制御など、失敗時の影響が大きい領域でエージェントの実行環境を統制したいチーム。
