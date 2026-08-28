---
type: guidance
title: 大規模GPU学習の『goodput』を守る、非同期分散チェックポイントとデータパイプライン設計
title_original: Fast, fault-tolerant PyTorch training on AI Runtime
company: Databricks
industry: cross-industry
cloud: []
patterns:
- fault-tolerant-training
- gpu-fleet-reliability
components:
- PyTorch
- Databricks AI Runtime
- Unity Catalog
- torch.distributed.checkpoint
outcome:
  type: reliability
source_id: databricks-blog
source_name: Databricks Blog
source_url: https://www.databricks.com/blog/fast-fault-tolerant-pytorch-training-ai-runtime
published_at: '2026-08-28'
---

## 概要

大規模GPUクラスタでは障害が例外ではなく前提であり（256GPU・30日運用で約19%、1024GPUで57%が障害に遭遇）、GPUの生産的稼働時間の割合を示す『goodput』を守る鍵はチェックポイントとデータパイプラインの設計にあると説く。単一プロセスへの同期書き込み（torch.save）ではなく、各ランクが並列にシャードを書き込むPyTorch分散チェックポイント（DCP）と非同期保存（async_save）を組み合わせることで、保存コストをほぼゼロに近づけ頻繁な保存を可能にする。

## 設計のポイント

- torch.saveの単一ランク同期書き込みではなく、DCPで各ランクが自分のシャードを並列に書き込みGPUのアイドル時間を減らす
- async_saveでステージングコピーとバックグラウンドアップロードを分離し、学習ループが支払うコストをステージング分だけにする
- チェックポイント間隔を短縮するほど障害時の再計算コスト（平均で間隔の半分）が線形に減る点を運用指標に組み込む
- モデルの状態だけでなくデータパイプラインの状態もチェックポイントし、再開時のデータ破損・重複を防ぐ
- .metadataファイルの有無を『保存完了』の判定に使い、再起動時に自動的に最新の完全なチェックポイントへ復帰する

## 使いどころ

- 数百〜数千GPU規模の分散学習で、障害からの復旧コストを下げてGPU予算の無駄を減らしたいMLインフラチーム
- DDPからFSDP/テンソル並列への移行を見据え、チェックポイント基盤を早期に統一しておきたい場合
- リモートオブジェクトストレージへの同期書き込みがGPUを長時間ブロックしている既存の学習パイプラインの改善
