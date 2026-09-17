---
type: guidance
title: 病院チェーン向けクラウドネイティブPACSアーキテクチャ
title_original: Building cloud-native PACS on AWS
ai_relevant: false
industry: healthcare
cloud:
- aws
patterns: []
components: []
outcome:
  type: cost
source_id: aws-architecture-blog
source_name: AWS Architecture Blog
source_url: https://aws.amazon.com/blogs/architecture/building-cloud-native-pacs-on-aws/
published_at: '2026-09-17'
---

## 概要

複数病院を抱えるチェーンでは年間50〜200TBもの医療画像データが蓄積し、オンプレミスSAN/NASの個別運用ではストレージコスト増大・施設間データサイロ化・放射線科医の読影ボトルネックが顕在化する。本記事はAWS Direct ConnectやSite-to-Site VPNで各病院のローカルPACS（スポーク）と中央クラウドアーカイブ（ハブ）を接続するハブ・アンド・スポーク型の構成パターンを提示し、Webサーバー・VNA・アプリケーションサーバー・DB・オブジェクトストレージ・ビューアという6つの中核コンポーネントの役割を整理する。
