---
type: case
title: Deep Agentsのコードインタプリタをサンドボックスなしで安全に実行する仕組み
title_original: Running Untrusted Agent Code Without a Sandbox
company: LangChain
industry: cross-industry
cloud: []
patterns:
- ai-agent
- multi-agent-orchestration
- guardrails
- human-in-the-loop
components:
- Deep Agents
- LangGraph
- LangSmith Sandboxes
- WebAssembly (WASM)
- QuickJS
- quickjs-rs
- langchain-quickjs
outcome:
  type: risk-compliance
source_id: langchain-blog
source_name: LangChain Blog
source_url: https://www.langchain.com/blog/running-untrusted-agent-code-without-a-sandbox
published_at: '2026-06-30'
---

## 概要

LangChainはDeep Agentsでサブエージェントをコードから動的にオーケストレーションする機能を導入するにあたり、プロンプトインジェクションで汚染されうるエージェント生成コードを安全に実行する「Code Interpreters」を開発した。専用マシンを立てるLangSmith Sandboxesとは異なり、WebAssembly上でQuickJSを動かすことでプロセス内に閉じた実行境界を作り、ハーネスが明示的に渡した機能だけを使わせるcapability isolationと、実行状態をLangGraphのstateにシリアライズして人間承認待ちなどで長時間一時停止・再開できる仕組みを実現した。

## 設計のポイント

- WASMを用いてホストプロセスと分離した線形メモリ空間でエージェント生成コードを実行し、ホストへのポインタ参照を不可能にすることで実行境界を確保する。
- QuickJSのような小さく閉じたJSエンジンを採用し、信頼境界内に置くトラステッドサーフェスを最小化する。
- インタプリタは初期状態で何の権限も持たせず、サブエージェント呼び出しなど必要な機能だけをハーネス経由で明示的にブリッジする（Meta's rule of twoに基づくcapability isolation）。
- QuickJSのメモリ状態をLangGraphのstateにシリアライズすることで、人間の承認を待つような長時間の一時停止と復元を可能にする。

## 使いどころ

- プロンプトインジェクションのリスクがあるエージェント生成コードを、専用サンドボックスマシンを立てずに安全に実行したい場合。
- 複数のサブエージェントをコードで動的にオーケストレーションする機能を提供したいエージェント開発者。
- 秒〜数日単位で人間の承認を挟む必要がある長時間実行のエージェントワークフローを構築する場合。
