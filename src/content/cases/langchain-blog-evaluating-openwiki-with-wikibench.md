---
type: case
title: 読み手エージェントとLLM審査員でコードWiki生成エージェントの質を測るベンチマークWikiBench
title_original: Evaluating OpenWiki with WikiBench
company: LangChain
industry: cross-industry
cloud: []
patterns:
- eval
- ai-agent
- rag
- context-engineering
components:
- OpenWiki
- WikiBench
- Harbor
- LangSmith
- Deep Agents
- DeepSeek Flash
- GLM 5.2
outcome:
  type: quality
source_id: langchain-blog
source_name: LangChain Blog
source_url: https://www.langchain.com/blog/evaluating-openwiki-with-wikibench
published_at: '2026-08-26'
---

## 概要

LangChainは、コードベースのWikiを自動生成・維持するエージェントOpenWikiの品質を測るため、Harbor上にWikiBenchというベンチマークを構築した。生成されたWikiに対して「読み手エージェント」に実際の質問を答えさせ、複数のLLM審査員が回答の事実性と根拠をルーブリックJSONに基づき採点することで、異なるハーネスやモデル間の性能・コスト・所要時間を比較した。結果として、Wikiと元のソースコードを併用した場合が最も高精度かつ低コストであり、Wiki単体では性能が大きく劣ることが分かった。

## 設計のポイント

- 評価をHarborのenvironment/agent/verifierの3要素に分解し、pinned commitのリポジトリを環境として固定することで再現性のあるベンチマークにしている。
- リポジトリのテーマ領域から自動生成する「カバレッジ」質問と、個別の挙動を問う「検索」質問の2種類を組み合わせ、網羅性と深さの両方を評価する。
- 各質問に事実リスト形式のルーブリックJSONを付与し、事実の有無をチェックする審査員と、その事実がWikiのページに根拠づけられているかをチェックする審査員を分けることでハルシネーションを防いでいる。
- 読み手エージェントにWikiのみ/ソースのみ/両方の3パターンでアクセスさせて比較することで、生成物単体の見た目の質ではなく実タスクへの実効性を測っている。

## 使いどころ

- エージェントが自動生成するドキュメントやWikiの品質を、人手レビューなしで継続的かつ定量的に評価したいプロダクトチーム。
- 複数のハーネスやモデル(バージョン)を切り替えて、性能・コスト・所要時間のトレードオフを比較検討したいAI基盤運用チーム。
- 索引となる生成ドキュメントと一次情報のソースコードを組み合わせるRAG的な設計が実際に有効かどうかを検証したいエンジニア。
- LLM-as-judgeによる採点で、事実の正確性だけでなく根拠の有無まで分離してチェックする評価パイプラインを設計したいチーム。
