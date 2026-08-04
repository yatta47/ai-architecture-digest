---
type: announcement
title: GitHub Copilotのエンタープライズ管理設定をチーム単位で特化できる仕組み
title_original: Enterprise team specialization for managed settings
company: GitHub
industry: cross-industry
cloud: []
patterns:
- policy-as-code
- guardrails
- ai-agent
- multi-model-routing
components:
- GitHub Copilot
- Copilot CLI
- Copilot App
- Copilot cloud agent
- managed-settings.json
- team-mappings.json
- Copilot SDK
outcome:
  type: risk-compliance
source_id: github-changelog
source_name: GitHub Changelog
source_url: https://github.blog/changelog/2026-08-03-enterprise-team-specialization-for-managed-settings
published_at: '2026-08-03'
---

## 概要

GitHubはエンタープライズ管理者がmanaged-settings.jsonの特定キーを「overridable」として指定し、チームごとに個別設定ファイルでCopilotのモデル選択や権限バイパスモードなどを上書きできる機能を追加した。コンプライアンス上重要な設定は上書き不可のままエンタープライズ側で固定しつつ、チームは許可された範囲内で自分たちのワークフローに合わせてCopilotを調整できる。これにより、すべての設定変更を中央管理者経由にする必要がなくなり、大規模組織でのガバナンスをボトルネックなくスケールさせられる。

## 設計のポイント

- overridableと明示指定したキーのみチーム側の値が有効になり、未指定キーはエンタープライズ側の値がceiling(上限/固定)として常に優先される二層構造にしている
- team-mappings.jsonで1つの設定ファイルを複数のチームslugに紐づけられるため、役割ごと(ai-users.json、devs.jsonなど)に設定を使い回せる
- ユーザーが複数チームに所属する場合はチームレベル設定を「最も緩い値」で合成してからエンタープライズ既定値の上に重ねる、というマージ規則で競合を解消している
- enabledPluginsやextraKnownMarketplacesは加算方式(additive)とし、チームが拡張しても組織全体のベースラインは弱まらないようにしている

## 使いどころ

- 大企業で全設定変更を中央管理者経由にするとボトルネックになる場合に、チームへ権限を委譲しつつガバナンスを維持したいとき
- AI Pioneersのような先進的なチームにはデフォルトモデル選択や権限バイパスモードなど一部の裁量を与えつつ、他のチームは標準ポリシーのままにしたいとき
- 研修修了チーム向けや開発者向けなど、職種・役割別にCopilotのプラグイン/マーケットプレイス構成を段階的に拡張したいとき
- コンプライアンス上必須の設定(セキュリティ関連キーなど)は上書き不可にしてリスクを抑えつつ、それ以外は柔軟に運用したいとき
