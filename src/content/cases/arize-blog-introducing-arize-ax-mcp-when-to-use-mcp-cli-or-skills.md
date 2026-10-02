---
type: opinion
title: エージェント拡張手段としてMCP・CLI・Skillsをどう使い分けるか
title_original: 'Introducing Arize AX MCP: When to use MCP, CLI, or skills'
company: Arize
industry: cross-industry
cloud: []
patterns:
- ai-agent
- context-engineering
- llmops
components:
- Arize AX
- Arize AX MCP
- ax CLI
- Arize skills
- Claude Code
- Cursor
- Claude Desktop
outcome:
  type: productivity
source_id: arize-blog
source_name: Arize Blog
source_url: https://arize.com/blog/extending-your-agent-with-arize-ax-mcp-cli-and-skills/
published_at: '2026-10-02'
---

## 概要

Arizeが同一プラットフォームを拡張する3つの手段(ホスト型MCPサーバー、CLI、Skills)の使い分けを論じた記事。ハーネス側のツール検索や遅延ロードでMCPのコンテキストコストが大きく下がったため、判断軸は『エージェントがどこで動くか、誰が使うか』に移ったと主張する。45ツールを持つホスト型MCPサーバーの公開も告知している。

## 設計のポイント

- 同じREST APIの上にMCP・CLI・Skillsを並べ、利用環境に応じて入口を選べるようにする。
- ツール定義の遅延ロードやコード実行により、MCPのコンテキストコスト問題は大きく緩和されている。
- MCPは名前付き操作の許可/拒否や認証情報の非保持など、ガバナンス面で利点がある。
- CLIはシェルがある環境でのスクリプト化・パイプ合成に向き、Skillsはその使い方をエージェントに教える層になる。

## 使いどころ

- ターミナルを持たないPMやサポート担当がClaude DesktopやCursorから観測データを参照したいとき。
- 自社プラットフォームをエージェント向けに公開する際のインターフェース設計を検討するプロダクトチーム。
- CIやcronなどシェル中心の自動化にエージェントを組み込む開発者。
