---
type: case
title: Salesforce、モバイルCI/CDのビルド障害を熟練サポートエンジニアのように調査するAIスキル群「Analyze Build Tools」を構築
title_original: How AI Learned to Investigate Mobile Build Failures Like an Experienced Support Engineer
company: Salesforce
industry: cross-industry
cloud: []
patterns:
- root-cause-analysis
- ci-cd
- ai-agent
components:
- Analyze Build Tools
- Managed Pipelines
outcome:
  type: productivity
source_id: salesforce-engineering-blog
source_name: Salesforce Engineering Blog
source_url: https://engineering.salesforce.com/how-ai-learned-to-investigate-mobile-build-failures-like-an-experienced-support-engineer/
published_at: '2026-07-01'
---

## 概要

Salesforceのモバイル基盤チーム(8名)は、60以上のリポジトリにまたがるiOS/Android向けCI/CDパイプラインのビルド障害調査を、熟練サポートエンジニアの調査手順を再現するAIスキル群「Analyze Build Tools」として実装した。/mp-investigate-buildなどのスキルが複数システムのログ・ビルド履歴・障害パターンを横断的に相関させ、原因がアプリコード/自社基盤/Apple・Googleの外部変更のどこにあるかを自動判定することで、インシデント解決時間を約60%、ビルド障害分析の工数を75%削減した。

## 設計のポイント

- AIにログの読み方をゼロから学習させるのではなく、熟練サポートエンジニアが実際に使っていた調査の勘所(例:1チームからの報告はアプリ側の問題、複数チーム同時報告は共有基盤の問題)を明示的なスキルとしてAIに移植する。
- 調査結果を受動的なダッシュボードとして提示するのではなく、/mp-investigate-buildのようなセルフサービスのスラッシュコマンド型スキルとして提供し、開発者が人間のサポートを待たずに同じ調査を自分で実行できるようにする。
- ビルド履歴・ログ・インフラ指標・他リポジトリでの類似障害を横断的に相関させ、原因をアプリコード/CI基盤/クラウド基盤/外部プラットフォーム変更という固定カテゴリに分類してからエスカレーションする。
- 少人数の基盤チームの工数を個別障害の調査対応から解放し、共有スキル・プラットフォームの改善に振り向けることで、対応リポジトリ数の増加に人員を比例させずに済むようにする。

## 使いどころ

- 多数のリポジトリやサービスを少人数で支える基盤/SREチームで、利用拡大に合わせてサポート要員を線形に増やせない組織。
- 障害原因がアプリ・CI基盤・クラウド基盤・外部サービスなど複数レイヤーにまたがり得るCI/CD環境で、開発者が原因の見当をつけられず闇雲にエスカレーションしている状況。
- 一部の熟練エンジニアだけが持つ暗黙のデバッグ知識を、再利用可能で問い合わせ可能なAI機能として組織全体に展開したい場合。
- 受動的な監視ダッシュボードから一歩進んで、『なぜビルドが失敗したか』という開発者の直接の問いにAIがオンデマンドで答える体験へ移行したいチーム。
