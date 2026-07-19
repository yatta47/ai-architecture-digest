---
type: guidance
title: 'テレコムの自律ネットワーク: エージェンティックAIプラットフォームの作り方'
title_original: How Telcos Build Autonomous Networks with Agentic AI
industry: telecom
cloud:
- on-prem
patterns:
- ai-agent
- multi-agent-orchestration
- root-cause-analysis
components:
- NVIDIA NeMo Data Designer
- NVIDIA Safe Synthesizer
- NVIDIA Nemotron
- NV-Tesseract
- NVIDIA Agent Toolkit
- NVIDIA OpenShell
- NVIDIA AI-Q
outcome:
  type: reliability
source_id: nvidia-technical-blog
source_name: NVIDIA Technical Blog
source_url: https://developer.nvidia.com/blog/how-telcos-build-autonomous-networks-with-agentic-ai/
published_at: '2026-07-09'
---

## 概要

ネットワーク運用の自動化の多くはLevel 2-3(既定解の実行)に留まっており、Level 4-5の自律性には意図理解・リアルタイムセンシング・立案・トレードオフ評価・ドメイン横断での統制されたアクションが必要になる。テレコム自律化プラットフォームはオンデマンド/長期稼働/ディープリサーチの3種のエージェントを、既知解の実行・最適化・未知課題の発見という3つの問題パターンに応じて組み合わせる。

## 設計のポイント

- 既知の問題は実行パスとして既存ランブックを流用し、既知だが未最適化の課題はディープリサーチで最適化案をランク付けし、未知の異常は発見パスで特徴づける
- 長期稼働エージェントが選ばれた計画をポリシー下で適用し、効果を継続観測しながらロールバックや再最適化を判断する
- 確立された対応は再利用可能なスキルとしてコード化し、次回以降はリサーチ不要な統制された実行パスへ昇格させる

## 使いどころ

- SR-MPLSネットワークの異常検知と自動復旧を自律化したい通信事業者のNOC
- 無線アルゴリズムの発見・改善など既知解のない最適化課題にAIエージェントを活用したい通信事業者
