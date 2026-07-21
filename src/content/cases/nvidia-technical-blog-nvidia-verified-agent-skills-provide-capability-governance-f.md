---
type: announcement
title: NVIDIA検証済みエージェントスキルによるケイパビリティガバナンス
title_original: NVIDIA-Verified Agent Skills Provide Capability Governance for AI Agents
company: NVIDIA
industry: cross-industry
cloud: []
patterns:
- guardrails
- policy-as-code
- ai-agent
- defense-in-depth
components:
- SkillSpector
- NVIDIA NeMo Guardrails
- NVIDIA OpenShell
- NVIDIA NemoClaw
- Claude Code
- Codex
- Cursor
outcome:
  type: risk-compliance
source_id: nvidia-technical-blog
source_name: NVIDIA Technical Blog
source_url: https://developer.nvidia.com/blog/nvidia-verified-agent-skills-provide-capability-governance-for-ai-agents/
published_at: '2026-06-11'
---

## 概要

NVIDIAは、AIエージェントが利用するスキル（指示セット）に透明性・出所証明・セキュリティスキャン・暗号署名を組み込む「NVIDIA検証済みエージェントスキル」を提供する。スキルはNVIDIA/skillsリポジトリでカタログ化され、SkillSpectorによる自動リスクスキャンと人手レビューを経て署名・スキルカード化された上で公開される。これによりClaude Code、Codex、Cursorなど複数のコーディングエージェントで、同一のSKILL.mdを安全に再利用できる共通の信頼基盤が提供される。

## 設計のポイント

- スキルはカタログ化→リスクスキャン→評価→スキルカード生成→署名→公開という一連のパイプラインを経て「検証済み」となる。
- SkillSpectorは脆弱な依存関係や危険なコードパターンといった従来型のソフトウェアリスクに加え、隠し命令・プロンプトインジェクション・過剰な権限要求といったエージェント特有のリスクも検査する。
- スキルカードという機械可読な信頼メタデータに機能・作成者・ライセンス・依存関係・既知の制限やリスクを記載し、導入前の互換性/リスク評価を可能にする。
- スキルディレクトリ全体を対象とした暗号署名により、ダウンロードしたスキルが改ざんされていないことを事後検証できるようにする。

## 使いどころ

- サードパーティ製のエージェントスキルを社内ワークフローに組み込む前に、出所やリスクを確認したい開発チーム。
- Claude Code、Codex、Cursorなど複数のコーディングエージェント間で同じスキル資産を安全に再利用したい組織。
- エージェントのランタイムガードレールだけでなく、エージェントが取り込む「能力（スキル）」そのものを継続的にガバナンスしたいセキュリティ/プラットフォームチーム。
