---
type: guidance
title: Hermes AgentとNemoClawで作る自己進化型の社内リサーチエージェント
title_original: Deploy Self-Evolving Agents for Faster, More Secure Research with a Hermes Agent and NVIDIA NemoClaw
company: NVIDIA
industry: cross-industry
cloud:
- on-prem
patterns:
- ai-agent
- memory-consolidation
- guardrails
- llmops
components:
- NVIDIA NemoClaw
- Hermes Agent
- NVIDIA OpenShell
- NVIDIA Nemotron 3 Super
- NVIDIA NIM
- vLLM
outcome:
  type: productivity
source_id: nvidia-technical-blog
source_name: NVIDIA Technical Blog
source_url: https://developer.nvidia.com/blog/deploy-self-evolving-agents-for-faster-more-secure-research-with-a-hermes-agent-and-nvidia-nemoclaw/
published_at: '2026-06-11'
---

## 概要

SlackやOutlook、GitHubなど社内外データを横断するHermes AgentをNVIDIA NemoClawブループリント上に構築し、学んだ書式や手順をSKILL.mdとしてファイルシステムに書き出して永続化する自己進化型エージェントの実装例。NVIDIA OpenShellがサンドボックス内で認証情報の隠蔽とネットワークポリシーによるアクセス制御を強制し、機密データを扱いながらもエージェントが外部に情報を持ち出せない設計にすることで、安全に公開/非公開データを混在利用できるようにする。

## 設計のポイント

- OpenShellのネットワークポリシーをpolicy.yamlとしてコードで宣言し、エージェントがアクセスできる宛先・ポート・HTTPメソッドをプロンプトではなく実行環境レベルで強制する
- SlackやOutlookの認証情報はサンドボックスプロキシがリクエスト送出時に注入し、エージェント自身には認証情報を一切見せない
- GitHubやフォーラムなどの公開データは別ETLプロセスでミラーし読み取り専用でエージェントに渡すことで、機密データにアクセスするエージェントの外部インターネット接続を遮断できるようにする
- 会話から学んだ出力書式をSKILL.mdとして書き出し、スナップショット/リストアでサンドボックスを再構築してもスキルが失われないようにする

## 使いどころ

- SlackやメールなどのチャットからGitHub Issueのダイジェスト作成のような定型業務を継続学習させたいチーム
- 社内の機密データと公開データを組み合わせて調査するが、エージェントが外部に情報を漏らすリスクを避けたいセキュリティ担当者
- エージェントの再デプロイのたびに学習内容が失われず引き継がれる運用を必要とするプラットフォームチーム
