---
type: case
title: ノーコードで作ったカスタムエージェントをワンクリックでSlackに配置
title_original: 'New in LangSmith Fleet: Bring agents into Slack in one click'
company: 11x
industry: cross-industry
cloud: []
patterns:
- ai-agent
- multi-agent-orchestration
- human-in-the-loop
components:
- LangChain Fleet
- Slack
- LangSmith
outcome:
  type: productivity
source_id: langchain-blog
source_name: LangChain Blog
source_url: https://www.langchain.com/blog/new-in-langsmith-fleet-bring-agents-into-slack-in-one-click
published_at: '2026-07-16'
---

## 概要

LangChainのFleetが、自然言語で作成した業務特化エージェントをワンクリックでSlackに配置できる機能を追加した。11xはFleetでバグトリアージエージェントを構築してSlackに展開し、オンコールアラートや製品Q&Aなど複数のユースケースに拡張、社員がエージェントの人格を認識してタグ付けで呼び出す運用が定着している。

## 設計のポイント

- エージェントごとに固有のSlackアイデンティティ（名前・説明・アイコン）を持たせ、汎用ボットではなく役割の明確な存在として認識させる。
- 承認が必要な操作（メール送信など）が発生した場合、同じSlackスレッド内でエージェントが確認を求め、人間が承認・修正指示・却下できるようにする。
- エージェントごとに接続先・権限・支出上限をスコープし、必要な範囲だけのアクセスを付与することでガバナンスを保つ。

## 使いどころ

- バグトリアージやオンコール対応など、定型化できるがSlack上での判断も伴う業務を持つチーム。
- エンジニア以外の担当者も含めて、自然言語だけで業務特化エージェントを作りたい組織。
- 承認フローを人間の目から切り離さずに、エージェントに一部の実行作業を任せたい業務。
