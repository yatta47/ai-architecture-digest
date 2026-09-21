---
type: guidance
title: NVIDIA Earth-2で最新の観測データを取り込むAIデータ同化パイプライン
title_original: Turn Your Latest Observations Into Timely Weather Decisions With NVIDIA Earth-2
industry: cross-industry
cloud: []
patterns:
- ai-data-assimilation
- inference-optimization
components:
- NVIDIA Earth-2
- Earth2Studio
- CorrDiff
- StormCast
- HealDA
outcome:
  type: quality
source_id: nvidia-technical-blog
source_name: NVIDIA Technical Blog
source_url: https://developer.nvidia.com/blog/turn-your-latest-observations-into-timely-weather-decisions-with-nvidia-earth-2/
published_at: '2026-09-15'
---

## 概要

NVIDIA Earth-2は、独自または第三者の観測データを拡散モデル(CorrDiff/StormCast)やHealDAに取り込むAIデータ同化ツールを提供し、6時間おきの数値解析を待たずに予報を最新の実測値へ継続的に合わせられるようにする。Score-Based Data Assimilation(SDA)はCorrDiff-COSMOのダウンスケーリング例で風速RMSEを54%、StormCast-CONUSの6予報ステップ平均で7.2%改善した。

## 設計のポイント

- 拡散モデルの多段階デノイズ過程の各ステップで中間予測と観測値を比較し、モデルを再学習せずに観測へ寄せるSDAという手法で、既存モデル資産を活かしたまま精度を上げる
- モデル出力を観測される量へ写像する観測オペレータ(単純な格子値の補間から、風力タービン出力のような代理指標まで)を定義できるようにし、多様なセンサーを同じ同化フレームワークに統一する
- 観測地点近傍では不確実性を小さく、離れるほど広く保つ確率的な出力にすることで、観測密度に応じた信頼度をそのまま下流の意思決定に伝える
- HealDAでは異種の衛星・地上観測をHEALPixの1度グリッドへ観測エンコーダとVision Transformerでマッピングし、秒単位で全球大気状態を推定する

## 使いどころ

- 風力・太陽光発電資産や送電網など、局所観測が意思決定に直結するエネルギー事業者の地域予報改善
- 6時間ごとの数値解析更新を待てない、災害対応やイベント運営など即時性が求められる現場での予報更新
- 保険・資本市場・物流など、独自の観測データを予報パイプラインに組み込んで物理リスクを評価したい業界
