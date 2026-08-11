---
type: guidance
title: Omnigentのコンテキストポリシーでエージェントの『三重脅威(lethal trifecta)』によるデータ持ち出しを阻止
title_original: 'Innocent Until Combined: Blocking the Lethal Trifecta with Omnigent Contextual Policies'
company: Databricks
industry: cross-industry
cloud: []
patterns:
- guardrails
- ai-agent
- defense-in-depth
components:
- Omnigent
outcome:
  type: risk-compliance
source_id: databricks-blog
source_name: Databricks Blog
source_url: https://www.databricks.com/blog/innocent-until-combined-blocking-lethal-trifecta-omnigent-contextual-policies
published_at: '2026-08-10'
---

## 概要

エージェントは『機密データへのアクセス』『信頼できない外部コンテンツへの曝露』『外部への送信手段』の3つが1セッションで揃うと、外部コンテンツに埋め込まれた指示によって機密データを持ち出す『三重脅威(lethal trifecta)』のリスクを負う。個々のアクション単位の認可チェックはこの危険を見逃すため、Omnigentのコンテキストポリシーはセッション内でどの『脚』が点灯したかを状態として追跡し、2つの脚が点灯した状態で送信(exfiltration)が呼ばれた場合のみそれをブロックする。サポートチケット対応エージェントの例では、チケット本文に仕込まれた指示で内部の売上データをメール送信させる攻撃を、通常業務を妨げずに阻止できることを示している。

## 設計のポイント

- 個別アクションの可否ではなく、セッション内でどの機能(私的データ・信頼できないコンテンツ・外部送信)が『点灯』したかという文脈状態を追跡する
- 3要素のうち2つが揃った時点では何もブロックせず、3つ目(送信)が実行されようとした瞬間にのみ介入する
- どのツールがどの『脚』に該当するかは人間がエージェント設定で事前に定義し、エージェント自身やランタイムには決めさせない
- サブエージェントからの指示も『信頼できないコンテンツ』として扱い、マルチエージェント構成でも同じポリシーを適用する

## 使いどころ

- 外部から到達可能な入力(チケット、メール、ドキュメント)を読み、機密データにアクセスし、外部送信もできるエージェントを運用する場合
- プロンプトインジェクションによるデータ持ち出しを、個別ツールの権限を絞らずに防ぎたい場合
- マルチエージェント構成でサブエージェントの指示が信頼境界を越える可能性がある場合
