---
type: announcement
title: AIエージェント専用の実行サンドボックス「LangSmith Sandboxes」
title_original: Give your agent its own computer
company: LangChain
industry: cross-industry
cloud: []
patterns:
- ai-agent
- defense-in-depth
- parallel-execution
- ci-cd
components:
- LangSmith Sandboxes
- LangSmith SDK
- Cursor
- Claude Code
- OpenSWE
outcome:
  type: risk-compliance
source_id: langchain-blog
source_name: LangChain Blog
source_url: https://www.langchain.com/blog/give-your-ai-agent-its-own-computer
published_at: '2026-06-25'
---

## 概要

LangChainは、AIエージェントがコードを安全に実行できる専用環境「LangSmith Sandboxes」を正式提供した。コンテナではなくハードウェア仮想化されたマイクロVMを採用し、信頼できないモデル生成コードやパッケージインストールをホスト基盤やカーネルから完全に分離する。スナップショット/フォーク、事前構築済みブループリント、認証プロキシなど、エージェントワークロードを本番運用するための一連の機能もあわせて提供する。

## 設計のポイント

- コンテナではなくハードウェア仮想化されたマイクロVMを採用し、カーネルを共有しないことで既知の脱獄・特権昇格リスクを遮断する
- スナップショットとフォークをCopy-on-Writeで実装し、10並列のブランチ起動を1台分に近いコストで実現する
- リポジトリクローンや依存関係インストール済みのブループリントから起動することで、数分かかる準備を数秒に短縮する
- アウトバウント通信を認証プロキシ経由にし、認証情報をエージェントランタイム自体には触れさせない設計にする

## 使いどころ

- コーディングアシスタントが生成したコードを実行・検証してから応答を返す場面
- CIエージェントがリポジトリをクローンし依存関係を入れてテストを実行しPRを開く場面
- RLやeval用にゼロから数千のサンドボックスをバースト起動し即座に破棄するワークロード
- ユーザー入力や外部パッケージなど、信頼できないコードを実行せざるを得ないエージェント
