---
type: case
title: Toyota北米、Deep Agents/LangGraph/LangSmithで社内エージェント基盤ToyotaGPTを50本超展開し8桁ドルのコスト削減へ
title_original: How Toyota North America Put Enterprise AI on the Balance Sheet with Deep Agents and LangSmith
company: Toyota Motor North America
industry: manufacturing
cloud: []
patterns:
- ai-agent
- multi-agent-orchestration
- rag
- eval
components:
- ToyotaGPT
- GearPal
- R&D GPT
- Deep Agents
- LangGraph
- LangSmith
- LangSmith Insights Agent
outcome:
  type: cost
source_id: langchain-blog
source_name: LangChain Blog
source_url: https://www.langchain.com/blog/how-toyota-north-america-put-enterprise-ai-on-the-balance-sheet-with-deep-agents-and-langsmith
published_at: '2026-08-24'
---

## 概要

Toyota Motor North Americaの約35人の全社AIチームは、Deep Agents・LangGraph・LangSmithを標準基盤にすることで新規エージェントの開発を『6か月・6人』から『4日・1人』に短縮し、社内データに根拠付けて回答するToyotaGPTを50以上の本番エージェントに拡大した。製造ライン向けの故障診断エージェントGearPalは診断時間を5〜6時間から2〜3分に、R&D GPTは研究サイクルを約3年から1年に圧縮しており、製造ラインごとに年間6桁ドル以上、施設単位で数百万ドル規模の削減を見込んでいる。

## 設計のポイント

- Toyota固有のドメイン知識を個々のエージェントにハードコードせず、製造・サプライチェーン・R&Dなど再利用可能な『スキル』ライブラリとして切り出し、実行時にDeep Agentsへ注入する
- 検索精度が重なり合うドメイン(塗装とサビなど)で低下する問題に対し、主要ツールで見つからない場合に副次ツールへ並列問い合わせしマージするLangGraphベースの並列ツール呼び出しを実装した
- LLMプロバイダ障害時のフォールバックを行うLLMゲートウェイを挟み、製造ラインという止められない環境での可用性を確保する
- SharePointなど既存の権限管理と連動させ、閲覧権限を持たないデータはエージェントの回答にも表示しない
- LangSmithを『工場のアンドン(Andon)ボード』と位置付け、ツール呼び出し失敗やパイプライン破損をリアルタイムに可視化し、現場の信頼獲得と経営層への説明責任の両方に使う

## 使いどころ

- 全社で数十のエージェントを標準基盤の上で量産・運用したい大企業のAIプラットフォームチーム
- 熟練技術者の退職に伴う暗黙知の喪失を、自然言語インターフェースの診断エージェントで補いたい製造現場
- 膨大な社内研究資料を横断検索し、リサーチサイクルを短縮したいR&D組織
- エージェントのROIを定量化して経営層に説明する必要がある場合の可観測性基盤の使い方として
