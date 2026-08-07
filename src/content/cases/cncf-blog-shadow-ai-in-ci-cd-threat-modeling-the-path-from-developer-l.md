---
type: guidance
title: 開発者PCからKubernetesまでのCI/CDパイプラインにおけるShadow AI脅威モデリング
title_original: 'Shadow AI in CI/CD: threat modeling the path from developer laptop to Kubernetes'
industry: cross-industry
cloud: []
patterns:
- ai-agent
- defense-in-depth
- guardrails
components:
- gitleaks
- Gitsign
- Sigstore
- Kubernetes
outcome:
  type: risk-compliance
source_id: cncf-blog
source_name: CNCF Blog
source_url: https://www.cncf.io/blog/2026/08/07/shadow-ai-in-ci-cd-threat-modeling-the-path-from-developer-laptop-to-kubernetes/
published_at: '2026-08-07'
---

## 概要

この記事は、開発者のノートPCからKubernetesのワークロードに至るソフトウェア配信パスの各段階で「Shadow AI」（未承認のAIツールやエージェント）がどのように侵入し得るかを脅威モデリングし、各段階に対応する防御策をCNCFプロジェクトを用いて示す。AIがアドバイスを与えるだけでなく実際にツールを呼び出し行動を起こすようになった時点で、それは権限とブラスト半径を持つ新しい非人間アイデンティティとして脅威モデルに組み込む必要があると論じている。

## 設計のポイント

- AIエージェントを生産性ツールではなく権限を持つ非人間アイデンティティとして扱い、所有者・最小権限・監視を割り当てる
- コミット前のシークレットスキャン(gitleaks)と署名付きコミット(Gitsign)で、漏えいと改ざんの両方を追跡可能にする
- 自律的にコマンドを実行するエージェントは使い捨てのVM分離ワークスペースで動かし、破壊的操作の被害をその環境内に封じ込める
- プロンプトインジェクションを前提に、フィルタリング単体に頼らず多層防御で各配信段階を守る

## 使いどころ

- AIコーディングアシスタントやレビューボットが未承認のまま使われている(Shadow AI化している)プラットフォーム/セキュリティチーム
- CI/CDパイプラインにAIエージェントを組み込み、ビルド修正やデプロイ承認まで任せ始めている組織
- Kubernetes上でAIエージェントにクラスタ操作権限を与える前にリスクを整理したい運用者
