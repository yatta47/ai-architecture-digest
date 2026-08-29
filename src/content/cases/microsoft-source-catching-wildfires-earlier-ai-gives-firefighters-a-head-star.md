---
type: case
title: 監視カメラ映像のAI解析による山火事早期検知システム(ALERTCalifornia)
title_original: 'Catching wildfires earlier: AI gives firefighters a head start'
company: ALERTCalifornia (UC San Diego) / Microsoft AI for Good Lab
industry: public-sector
cloud: []
patterns:
- video-intelligence
- human-in-the-loop
components: []
outcome:
  type: speed
source_id: microsoft-source
source_name: Microsoft Source
source_url: https://unlocked.microsoft.com/alertcalifornia-ai-wildfire-detection/
published_at: '2026-08-28'
---

## 概要

カリフォルニア州の火災多発地域に設置された約1,300台のカメラ映像を、UC San DiegoのALERTCaliforniaとMicrosoft AI for Good Labが共同開発したAIが常時解析し、煙の兆候を検知する。システムは1日7百万枚超の画像を処理し、複数カメラ角度の照合と位置検証を経て数分でアラートを出し、最速で最初の119番通報より2.5時間早く火災を検知した事例もある。AIは雲や霧などの誤検知を除去して信号を絞り込むだけで、消火判断そのものは引き続き消防隊員が行う。

## 設計のポイント

- 多数のカメラ映像をAIが常時解析し、複数カメラ角度の照合で誤検知(雲・霧・朝日の影など)を除外してから通知するパイプラインにし、ダウンストリームの人間の判断負荷を下げる
- AIは『検知して知らせる』役割に限定し、消火activityの意思決定は現場の消防隊員に委ねるヒューマン・イン・ザ・ループの設計にする
- 検知後にライブカメラ映像そのものを指令・出動隊に共有し、火の性質や最適な進入経路の判断材料を人間に提供する

## 使いどころ

- 広域に分散したセンサー/カメラ網から異常の初期兆候をいち早く検知し、対応までのリードタイムを縮めたい防災・公共安全分野
- 検知の自動化と最終判断の人間保持を両立させたい、誤報コストが高い監視・アラートシステム全般
