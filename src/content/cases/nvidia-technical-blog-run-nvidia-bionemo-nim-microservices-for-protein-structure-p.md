---
type: case
title: エージェントによるタンパク質構造予測ワークフローのオーケストレーション
title_original: Run NVIDIA BioNeMo NIM Microservices for Protein Structure Prediction in Claude Science
company: NVIDIA
industry: healthcare
cloud:
- on-prem
patterns:
- ai-agent
- multi-model-routing
components:
- NVIDIA BioNeMo Agent Toolkit
- Claude Science
- NVIDIA NIM
- MSA Search NIM
- OpenFold3
- Boltz-2
outcome:
  type: quality
source_id: nvidia-technical-blog
source_name: NVIDIA Technical Blog
source_url: https://developer.nvidia.com/blog/run-nvidia-bionemo-nim-microservices-for-protein-structure-prediction-in-claude-science/
published_at: '2026-08-31'
---

## 概要

NVIDIAとAnthropicは、BioNeMo Agent ToolkitをClaude Scienceに統合し、AIエージェントがMSA検索・OpenFold3・Boltz-2といった複数のNIMマイクロサービスを呼び出してタンパク質構造予測を自律的に実行できるようにした。Seh1タンパク質とその推定パートナーの複合体予測を題材に、進化的アラインメント（MSA）の有無で予測精度（iPTM）が大きく変動することを示し、社内ベンチマークではドメイン特化スキルの利用によりタスク正答率が60%から100%に向上したという。

## 設計のポイント

- ドメイン特化のライフサイエンスモデル群をエージェント呼び出し可能な『スキル』としてパッケージ化し、汎用エージェントがAPIやパラメータの詳細を意識せず呼び出せるようにする
- MSA生成→単鎖予測→複合体予測という多段パイプラインの中間出力（アラインメント等）を保持し、複数モデル（OpenFold3・Boltz-2）で同一条件を横断比較できるようにする
- 推論はローカルGPU上のNIMマイクロサービス（Dockerコンテナ）として起動し、セッション内でエンドポイントのヘルスチェックを行ってからオーケストレーションする

## 使いどころ

- 創薬・構造生物学の研究者が、タンパク質複合体の構造仮説を素早く検証したい場面
- 汎用コーディングエージェントに専門ドメインのモデル操作を任せたいが、モデル選定やパラメータ調整のノウハウが不足している場合
- 複数の予測モデルの結果を横断比較し、入力条件（MSAの有無など）が予測品質に与える影響を切り分けたい場合
