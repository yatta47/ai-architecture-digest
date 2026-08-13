---
type: case
title: Text2SQLのレイテンシを80%削減したパラメータ化クエリテンプレートキャッシュ
title_original: Reducing Text2SQL latency with parameterized query templates
industry: cross-industry
cloud:
- aws
patterns:
- text-to-sql
- cost-optimization
- inference-optimization
components:
- Amazon Bedrock
- AWS Lambda
- Amazon Nova 2 Lite
outcome:
  type: speed
source_id: aws-architecture-blog
source_name: AWS Architecture Blog
source_url: https://aws.amazon.com/blogs/architecture/reducing-text2sql-latency-with-parameterized-query-templates/
published_at: '2026-08-13'
---

## 概要

自然言語からSQLを生成するText2SQLシステムで、質問文そのものではなくSQLクエリの構造をテンプレート化してキャッシュすることでレイテンシを80%、トークン消費を50%以上削減した事例。テンプレートと質問の埋め込みをペアで保存し、意味的類似検索でLLM呼び出しを迂回することで自己改善型のキャッシュを実現する。

## 設計のポイント

- 質問文ではなくSQLクエリ自体（プレースホルダ付きテンプレート）をキャッシュすることで、データ更新によるキャッシュ失効問題を回避する
- テンプレートに質問文のベクトル埋め込みを紐付け、意味的類似検索で言い回しの違いを吸収してキャッシュヒット率を上げる
- キャッシュミス時は通常通りLLMでSQLを生成し、新しいテンプレートとして追加登録することでカバレッジが自然に育つ

## 使いどころ

- パイロットから本番へスケールする際にレイテンシと推論コストがボトルネックになっているText2SQLシステム
- 同じ構造で条件だけ異なる質問（期間・カテゴリ違いなど）が繰り返し発生する業務分析ツール
