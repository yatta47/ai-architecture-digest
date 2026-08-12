---
type: case
title: 生成×判別を統合した胸部X線VLM(CARE-X)の研究アーキテクチャ
title_original: CARE-X makes radiology AI more helpful in the clinic
company: Microsoft Research
industry: healthcare
cloud:
- azure
patterns:
- reinforcement-learning
- fine-tuning
- eval
components:
- SigLIP2-so400M
- Phi-4-mini-instruct
- Qwen3-VL-4B-Instruct
outcome:
  type: quality
source_id: microsoft-source
source_name: Microsoft Source
source_url: https://www.microsoft.com/en-us/research/blog/introducing-care-x-towards-clinically-useful-radiology-vlms-with-auxiliary-supervision-reward-aligned-learning-and-tool-augmented-measurement/
published_at: '2026-08-12'
---

## 概要

Microsoft ResearchはSigLIP2ビジョンエンコーダとPhi-4-mini-instructを組み合わせ、レポート生成と閾値調整可能な構造化予測を1モデルで両立する胸部X線VLM「CARE-X」を研究開発した。DAPO強化学習で臨床的正しさそのものを報酬化し、Narayana Healthの実臨床データで検証した。別実験ではQwen3-VLに決定論的な計測ツールを組み合わせ、測定依存所見の精度向上を確認した。

## 設計のポイント

- 生成ヘッドと分類・位置特定用の補助ヘッドを共有バックボーンに統合し、自由記述レポートと閾値調整可能な構造化出力を単一モデルで両立させた。
- トークンレベルの交差エントロピーではなくDAPO強化学習で臨床的正しさを報酬化し、否定の反転など臨床的に重大な誤りを重く罰するようにした。
- 心胸郭比のような測定依存の所見は視覚的近似に頼らず、外部の決定論的計測ツールと連携させて精度を高めた。

## 使いどころ

- 生成AIの柔軟性と閾値調整可能な確信度スコアの両方が必要な臨床意思決定支援システムの研究者。
- レポート生成・所見有無判定・デバイス位置評価など複数タスクを1モデルで扱いたい医療AI開発チーム。
- 測定に基づく所見(心拡大など)で視覚推定の限界に直面しているVLM開発者。
