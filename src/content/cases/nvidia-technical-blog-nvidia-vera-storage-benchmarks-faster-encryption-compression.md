---
type: announcement
title: NVIDIA Vera BlueField-4 STXによるAIネイティブストレージ処理の高速化
title_original: 'NVIDIA Vera Storage Benchmarks: Faster Encryption, Compression, Integrity Checking, and Recovery for AI-Native
  Storage'
company: NVIDIA
industry: cross-industry
cloud:
- on-prem
patterns:
- storage-processing-acceleration
- unified-runtime
- cost-optimization
components:
- NVIDIA Vera BlueField-4 STX Storage Processor
- NVIDIA Olympus CPUコア
- NVIDIA Scalable Coherency Fabric
- SOCAMM2 LPDDR5Xメモリ
- NVIDIA Rubin GPU
- NVIDIA STX
outcome:
  type: speed
source_id: nvidia-technical-blog
source_name: NVIDIA Technical Blog
source_url: https://developer.nvidia.com/blog/nvidia-vera-storage-benchmarks-faster-encryption-compression-integrity-checking-and-recovery-for-ai-native-storage/
published_at: '2026-08-01'
---

## 概要

NVIDIA Vera BlueField-4 STX Storage Processorは、88基のOlympus Armv9.2コア、Spatial Multithreading、Scalable Coherency Fabric、SOCAMM2 LPDDR5Xメモリを組み合わせ、AIネイティブなストレージ基盤に必要な暗号化・圧縮・整合性検証・データ復旧などのCPU側処理を高速化する。ベンチマークではx86 CPU比で暗号化最大1.43倍、Reed-Solomon復旧最大3.26倍、CRC32C整合性チェック最大3.67倍、圧縮最大3.29倍などの向上を示し、エージェントAIワークロードの拡大に伴うストレージ処理負荷をより少ないCPU・電力・冷却コストで支える。GPUが推論を担う一方でCPUがエージェント実行・ツール呼び出し・ストレージサービスを担うという役割分担のもと、統一されたVera CPUアーキテクチャがサービス密度と同時データフロー数の向上を可能にする。

## 設計のポイント

- GPUは推論処理、CPUはエージェント実行・ツール呼び出し・ストレージサービスという役割分離を前提に、CPU側のストレージ処理性能を独立して強化する
- 88コアのOlympus CPU、Spatial Multithreading、Scalable Coherency Fabric、SOCAMM2 LPDDR5Xメモリを組み合わせ、シングルスレッド性能と帯域幅の両方を同時に満たす
- 暗号化・整合性チェック・Reed-Solomon復旧・圧縮/展開といったデータパス上の逐次処理をCPU内で高速化し、SSDやネットワークの性能をボトルネックにしない
- 統一CPUアーキテクチャによりエージェント実行とストレージ処理を同一基盤上でスケールさせ、コア数・電力・冷却の増加を抑えたままサービス密度を高める

## 使いどころ

- 数千規模の同時実行エージェントが大きなコンテキストウィンドウやKVキャッシュを扱うエージェントAI基盤の運用者
- 暗号化・圧縮・整合性検証・復旧などの多段ストレージパイプラインがCPU処理でボトルネックになっているAIネイティブデータプラットフォーム
- CPUコア数や電力・冷却コストを増やさずにストレージ処理のスループットと同時データフロー数を高めたいデータセンター運用者
- 高速なSSD・ネットワークの性能をCPU側処理の遅延で無駄にしたくないAIインフラ設計者
