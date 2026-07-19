---
type: case
title: コーディングエージェントによるRL研究ワークフローの自律実行（NeMo RL × Agent Skills）
title_original: How to Run an Autoresearch Workflow with RL Agent Skills and NVIDIA NeMo
company: NVIDIA
industry: cross-industry
cloud: []
patterns:
- reinforcement-learning
- ai-agent
- llmops
- human-in-the-loop
components:
- Codex (GPT-5.5)
- NVIDIA NeMo RL
- NVIDIA NeMo Gym
- NVIDIA Brev
- Qwen3-VL-2B-Instruct
- Ray
- vLLM
outcome:
  type: quality
source_id: nvidia-technical-blog
source_name: NVIDIA Technical Blog
source_url: https://developer.nvidia.com/blog/how-to-run-an-autoresearch-workflow-with-rl-agent-skills-and-nvidia-nemo/
published_at: '2026-07-13'
---

## 概要

コーディングエージェントCodex(GPT-5.5)がNVIDIA NeMo RL/NeMo GymとBrev GPUインスタンス上で、環境構築から実験実行、メトリクス分析までを自律的に遂行するautoresearchワークフローを検証した。新規のNeMo Gym視覚カウント環境をゼロから作成しQwen3-VL-2B-Instructを学習させたところ精度が25.0%から96.9%に向上し、さらに論文中のオフポリシーRLアルゴリズム(OAPL)をエージェント自身がコード実装して長時間の検証学習キャンペーンを開始した。

## 設計のポイント

- Brev-etiquette(運用衛生)・session-memory(セッション記憶)・autoresearch(実験管理)という3つの再利用可能なagent skillに運用知識をカプセル化し、エージェントがローカルな運用慣習を守りながら再現性のある実験を回せるようにしている。
- ベースライン計測→仮説ごとのブランチ作成→レッジャーへの記録→停止条件の監視、という定型ループ(autoresearch)により、長時間・複数セッションにまたがる実験でも進捗と意思決定を追跡可能にしている。
- session-memoryが目的・サブタスク・重要ファイル・意思決定を記録するため、コンテキスト圧縮や切断が起きても目的を見失わずに作業を再開できる。
- エージェントには環境構築からハイパーパラメータ調整までのフルスタック作業を委譲しつつ、目標設定・マイルストーンレビュー・最終意思決定は人間が保持するという役割分担を明確にしている。

## 使いどころ

- MLリサーチチームがRLパイプラインの環境構築や反復実験など定型作業をエージェントに任せ、研究者は仮説設計と意思決定に集中したい場合。
- 論文で提案された新しいアルゴリズムを迅速にコード化し、実データで検証まで持っていきたいR&Dチーム。
- 長時間・断続的なセッションにまたがる実験キャンペーンで、再現性と進捗の追跡可能性を担保したい場合。
