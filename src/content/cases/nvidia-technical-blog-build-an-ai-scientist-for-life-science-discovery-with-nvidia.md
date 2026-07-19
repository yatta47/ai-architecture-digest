---
type: guidance
title: 'BioNeMo Agent Toolkit: ライフサイエンス向けAIサイエンティストの構築'
title_original: Build an AI Scientist for Life Science Discovery with NVIDIA BioNeMo Agent Toolkit
industry: healthcare
cloud:
- multi-cloud
patterns:
- ai-agent
- agentic-tool-use
components:
- NVIDIA BioNeMo
- NVIDIA NIM
- Model Context Protocol
- cuEquivariance
- Parabricks
- Boltz-2
- GenMol
- DiffDock
- Evo 2
outcome:
  type: quality
source_id: nvidia-technical-blog
source_name: NVIDIA Technical Blog
source_url: https://developer.nvidia.com/blog/build-an-ai-scientist-for-life-science-discovery-with-nvidia-bionemo-agent-toolkit/
published_at: '2026-07-09'
---

## 概要

汎用コーディングエージェントをそのまま生物学に向けても新薬は生まれない。BioNeMo Skillsは構造予測・分子生成・ドッキング・配列解析・ゲノム解析といったモデルを、目的・入力・想定アーティファクト・失敗モードまで文書化してエージェントが自律的に選択・実行できるツールとして提供する。Codex CLI(GPT-5.5 fast)での検証ではトークン効率が倍増し、タスク完了率が57.1%から100%に向上した。

## 設計のポイント

- 各モデルをBioNeMo Skillとして、目的・必須入力・任意パラメータ・期待アーティファクト・失敗モードまで文書化しエージェントが自律選択できるようにする
- NIM化されていないオープンモデルはMCPサーバーラッパーで包み、同じエージェント呼び出しパターンに統一する
- 評価・探索・散発的呼び出しはホスト型NIMから始め、反復頻度や低遅延要件が高まったモデルだけをローカル配備に移行する

## 使いどころ

- 構造予測やドッキングなど専門モデルをエージェントに安全かつ確実に呼び出させたい創薬・バイオ研究チーム
- モデル呼び出しの試行錯誤を減らしイテレーションループの効率を上げたいAIサイエンティスト開発者
