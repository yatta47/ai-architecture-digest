---
type: announcement
title: 自然言語でフローを作りエージェントを協調させるAWS Quickの更新
title_original: 'New in AWS Quick: More capable flows, an updated web experience, and agents that work together'
company: Amazon Web Services
industry: cross-industry
cloud:
- aws
patterns:
- ai-agent
- multi-agent-orchestration
- human-in-the-loop
- parallel-execution
components:
- AWS Quick
- Quick Flows
- Slack
- Microsoft Excel
outcome:
  type: productivity
source_id: aws-machine-learning-blog
source_name: AWS Machine Learning Blog
source_url: https://aws.amazon.com/blogs/machine-learning/new-in-aws-quick-more-capable-flows-an-updated-web-experience-and-agents-that-work-together/
published_at: '2026-11-21'
---

## 概要

AWS Quickが、チャットで業務プロセスを記述するとフローを生成する機能、複数の専門エージェントが並列で答えを統合するマルチエージェント構成、ウェブアプリの刷新を発表した。月次レポートを例に、個人の手順をチーム共通のプロセスにする流れを示している。

## 設計のポイント

- 固定の計算・チェックなど決定論的ステップとエージェントによる下書きを組み合わせ、結果の一貫性と検証可能性を確保している。
- 最終承認は人が行い、フラグ理由を確認してから確定する構成にしている。
- 地域ごとの処理を並列に走らせ、対象が増えても所要時間が伸びにくくしている。

## 使いどころ

- 属人化した月次レポートなどの定型業務をチームで再利用したいとき。
- 複数データソースを横断した問い合わせを1つのプロンプトで済ませたいとき。
- ブラウザを閉じても動き続ける長時間のエージェントタスクを回したいとき。
