---
type: case
title: NVIDIAがPalantir FoundryとNemotronでサプライチェーン判断を型式知化
title_original: 'From Wafer-Out to First Token: Codifying Supply Chain Expertise with Nemotron and Palantir Foundry'
company: NVIDIA
industry: manufacturing
cloud: []
patterns:
- fine-tuning
- decision-execution
- ai-agent
components:
- Palantir Foundry
- Nemotron 3.5 Lightning
- NVIDIA cuOpt
- NeMo Anonymizer
- Data Designer
- AutoModel
outcome:
  type: quality
source_id: nvidia-technical-blog
source_name: NVIDIA Technical Blog
source_url: https://developer.nvidia.com/blog/from-wafer-out-to-first-token-codifying-supply-chain-expertise-with-nemotron-and-palantir-foundry/
published_at: '2026-09-10'
---

## 概要

NVIDIAはPalantir Foundry上に部材・生産能力・定性情報を統合するDigital Supply Chain Intelligenceセンターを構築し、cuOptによる週次の混合整数計画に加え、過去の人間の割当判断・理由・結果でNemotron 3.5 Lightningを追加学習させた。特化型30Bモデルは開発ベンチマークで86.7%の割当判断精度を達成し、ベースモデル比69.2ポイント向上した。

## 設計のポイント

- 定量ソルバー（cuOpt）だけでは捉えられないメール・天候・地政学情報などの定性判断を人間の意思決定として記録し学習データにする
- ガバナンスされたPalantir Autopilotのライフサイクル内で、匿名化・データ設計・自動モデル学習のパイプラインを構築する
- 承認・修正・却下された推奨をOntologyへフィードバックし、継続的な再学習で組織知を蓄積する

## 使いどころ

- 数千のサプライヤーと部材制約が絡み合う大規模ハードウェア供給網での配分意思決定
- 熟練プランナーの暗黙知を定量モデルに組み込み、オンボーディング期間を短縮したい場合
