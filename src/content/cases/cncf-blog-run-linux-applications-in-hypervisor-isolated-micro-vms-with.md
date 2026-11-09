---
type: guidance
title: Hyperlight：AI生成コード実行向けのハイパーバイザ隔離マイクロVM
title_original: Run Linux applications in hypervisor-isolated micro-VMs with Hyperlight
company: Microsoft
industry: cross-industry
cloud: []
patterns:
- defense-in-depth
- ai-agent
components:
- Hyperlight
- hyperlight-unikraft
- Unikraft
- KVM
- Kubernetes
outcome:
  type: risk-compliance
source_id: cncf-blog
source_name: CNCF Blog
source_url: https://www.cncf.io/blog/2026/11/09/run-linux-applications-in-hypervisor-isolated-micro-vms-with-hyperlight/
published_at: '2026-11-09'
---

## 概要

CNCF Sandboxプロジェクトのライブラリ型VMM『Hyperlight』は、アプリに組み込める軽量マイクロVMで、AIエージェントが生成したコード等を隔離実行する。hyperlight-unikraftにより、未改変のLinuxアプリをユニカーネル上で動かせる。

## 設計のポイント

- ホストが公開した関数だけをゲストに許可するケイパビリティ型の許可リストで、権限を絞る
- プロセスやサンドボックスの速さとVMの強い隔離を両立するため、デバイスを持たないマイクロVMを使う
- Dockerfileでrootfsを拡張でき、既存のLinuxバイナリを移植や再コンパイルなしで動かせる

## 使いどころ

- AIエージェントが生成したコードを安全に実行したいプラットフォーム
- 顧客がアップロードしたプラグインを隔離して動かすSaaS
- サプライチェーン攻撃に備えて実行境界を強めたい開発組織
