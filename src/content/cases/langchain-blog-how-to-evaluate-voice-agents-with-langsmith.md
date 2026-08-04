---
type: guidance
title: LangSmithによるボイスエージェント評価：実行・成果・体験の3軸フレームワーク
title_original: 'How to evaluate voice agents: execution, outcomes, and experience'
industry: cross-industry
cloud: []
patterns:
- voice-agent
- eval
- llmops
components:
- LangSmith
outcome:
  type: quality
source_id: langchain-blog
source_name: LangChain Blog
source_url: https://www.langchain.com/blog/how-to-evaluate-voice-agents-execution-outcomes-and-experience
published_at: '2026-08-04'
---

## 概要

音声エージェントは指示に忠実でも顧客の目的を達成できないことがあるため、LangChainは評価を「実行(Execution)」「成果(Outcome)」「体験(Experience)」の3軸に分けることを提案する。実行の明示的な要件はコード評価器で決定的に、意味解釈が必要な要件はルーブリックを与えたLLM judgeで評価し、成果は会話内の推測だけでなく予約記録やチケット再オープン率などの下流ビジネス指標と突き合わせる。LangSmithでは通話のトレース・録音・ツール呼び出しを一体で確認し、変更前後の効果を継続的に比較できる。

## 設計のポイント

- ツール呼び出し順序や必須確認項目など明示的なルールにはコード評価器を使い、モデル呼び出し無しで高速・低コストに判定する
- 自然言語のポリシー遵守や説明の分かりやすさなど意味解釈が必要な要件には、曖昧な問いではなく具体的なPass/Fail基準を与えたLLM judgeを使う
- 『指示に従ったか』と『目的を達成したか』を別軸として評価し、指示は満たしても顧客のタイムゾーン確認漏れのような成果失敗を見逃さない
- 会話内容だけで成功を推測せず、予約レコードやケース再オープン率などの下流ビジネスシグナルを元のトレースに紐付けて評価する

## 使いどころ

- 予約受付やカスタマーサポートなど本番運用中の音声エージェントの品質を継続的に監視・改善したいチーム
- プロンプトやツール構成を変更した際に、実際のビジネス成果への影響を回帰的に検証したい場合
- 会話ログ上は問題なく見えても実際には顧客の要求を満たせていない『隠れた失敗』を検出したい場合
