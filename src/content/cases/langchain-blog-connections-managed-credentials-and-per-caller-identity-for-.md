---
type: guidance
title: LangChainエージェントに呼び出し元ごとのID解決を持たせる認証基盤「Connections」
title_original: 'Connections: Managed credentials and per-caller identity for Managed Deep Agents'
company: LangChain
industry: cross-industry
cloud: []
patterns:
- ai-agent
- llmops
- human-in-the-loop
components:
- LangSmith
- Managed Deep Agents
- GitHub
- Tavily
- MCP
- Linear
outcome:
  type: risk-compliance
source_id: langchain-blog
source_name: LangChain Blog
source_url: https://www.langchain.com/blog/connections-managed-credentials-and-per-caller-identity-for-managed-deep-agents
published_at: '2026-09-09'
---

## 概要

Managed Deep AgentsのConnectionsは、認証情報を.envやビルドに含めずLangSmithワークスペース側で名前付き接続として管理し、実行時にスラッグ経由で取得する仕組みを提供する。エージェント共有のシークレットとユーザーごとのOAuth権限を切り分けることで、誰が代理でアクションを実行したかを追跡できるようにする。

## 設計のポイント

- 認証情報の所有者（エージェント共有 or 呼び出し元ごと）と種別（静的シークレット or OAuth）を独立した2軸として設計する
- connections.get()を1行呼ぶだけでOAuthの往復処理・トークン保存・リフレッシュを肩代わりし、アプリ側にコールバックルートを持たせない
- ユーザー所有の接続は実行時に本人の権限で解決されるため、発行されたチケットやIssueが実際の利用者名義になり監査性が上がる
- 未認可の呼び出し元にはトークン発行を止めて認可フローを差し込み、失敗ではなく同意取得へフォールバックする

## 使いどころ

- ユーザーに代わってGitHub Issue作成やチケット発行などを行うエージェントで操作主体を正しく記録したい場合
- APIキーのローテーション/失効をコード変更やデプロイなしで行いたい運用チーム
- 複数のMCPサーバーや外部SaaSと連携するエージェントでOAuth実装コストを削減したい場合
