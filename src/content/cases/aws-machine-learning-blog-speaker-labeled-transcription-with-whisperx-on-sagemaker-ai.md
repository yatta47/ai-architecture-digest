---
type: guidance
title: WhisperX DLCで話者ラベル付き文字起こしをSageMaker AIに載せる構成
title_original: Speaker-labeled transcription with WhisperX on SageMaker AI
industry: cross-industry
cloud:
- aws
patterns:
- realtime-transcription
- inference-optimization
- cost-optimization
components:
- Amazon SageMaker AI
- WhisperX
- OpenAI Whisper
- AWS Deep Learning Container
- Amazon S3
- Amazon ECR
outcome:
  type: quality
source_id: aws-machine-learning-blog
source_name: AWS Machine Learning Blog
source_url: https://aws.amazon.com/blogs/machine-learning/speaker-labeled-transcription-with-whisperx-on-sagemaker-ai/
published_at: '2026-09-24'
---

## 概要

WhisperXのDLCをSageMaker AIのリアルタイム/非同期エンドポイントにデプロイし、単語単位タイムスタンプと話者ダイアライゼーション付きの文字起こしを実現する手引き。クリップ長と対話性でエンドポイント種別を使い分ける判断基準、GPU AMI固定、スケーリング、S3設定、コスト管理まで整理している。

## 設計のポイント

- 短い対話的クリップは60秒上限のあるリアルタイムエンドポイント、長尺・大量バッチはS3経由の非同期エンドポイントと使い分ける。
- 同一のコンテナ契約(8080番ポートの/invocationsと/ping、multipart/form-data)を両方式で共通化し、デプロイ形態だけを切り替える。
- 非同期エンドポイントはアイドル時にゼロへスケールでき、常時課金のリアルタイム型よりコストを抑えられる。
- 出力をjson/verbose_json/srt/vttから選べるため、同じエンドポイントを分析基盤にも字幕編集にも使える。

## 使いどころ

- コンタクトセンターで話者別の通話時間や台本遵守、感情分析を行いたい場合。
- メディアやeラーニングで大量コンテンツの字幕(SRT/VTT)を高精度に生成したい場合。
- 医療・法務・金融で、話者付き議事録を監査や証拠開示に使いたい場合。
