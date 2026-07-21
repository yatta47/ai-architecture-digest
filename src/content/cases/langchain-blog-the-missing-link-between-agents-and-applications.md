---
type: announcement
title: LangChainのheadless toolsでエージェントがブラウザ/アプリのクライアント状態を直接操作
title_original: The Missing Link Between Agents and Applications
company: LangChain
industry: cross-industry
cloud: []
patterns:
- ai-agent
- headless-tools
- memory-consolidation
components:
- LangChain
- IndexedDB
- slidev-agent
outcome:
  type: quality
source_id: langchain-blog
source_name: LangChain Blog
source_url: https://www.langchain.com/blog/agents-and-applications
published_at: '2026-06-11'
---

## 概要

LangChainは「headless tools」という仕組みを導入し、ジオロケーションやクリップボード、ローカルメモリ、アプリ固有の操作といったクライアント側の機能をエージェントの推論ループに第一級のツールとして組み込めるようにした。サーバーはツール呼び出しの意思決定のみを担い、実際の実行はブラウザやデスクトップアプリなどクライアント側で行うことで、バックエンド専用ツールでは扱えなかったフロントエンド状態やデバイスAPIへのアクセスを実現し、UXとプライバシーの両方を改善する。

## 設計のポイント

- headless toolはモデルから見れば通常のツール(name/description/schema)と同一だが、実行主体はサーバーではなくクライアント(ブラウザ/デスクトップアプリ)になる
- サーバーは「何を呼ぶか」を、クライアントは「どう実行するか」を知るという役割分離により、クライアント専用APIをエージェントの推論ループの内側に統合し、アドホックなUIブリッジを不要にする
- TypeScriptでは.implement()によりツール定義と実装を分離し、サーバー/クライアントで同じスキーマを共有しつつ実行ロジックはクライアント側にのみロードする
- IndexedDBなどブラウザストレージにエージェントメモリを保持することで、センシティブなデータをサーバーに送らずデフォルトでローカルに留められる

## 使いどころ

- Figma/Google Slides/リッチテキストエディタなどのサイドカーエージェントで、カーソル位置への挿入や選択オブジェクトの整形などクライアント側状態を直接操作したい場合
- ジオロケーションやクリップボードなどブラウザ/デバイス専用APIをエージェントに使わせたいプロダクトチーム
- ユーザーデータをサーバーに送信せずローカルに留めたいプライバシー重視のエージェントメモリ設計
