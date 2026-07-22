---
type: case
title: Kyverno CLIをだましてオフラインでも本番同等のポリシー評価を実現
title_original: I made a policy engine think it was in production
ai_relevant: false
industry: cross-industry
cloud: []
patterns: []
components: []
outcome:
  type: reliability
source_id: cncf-blog
source_name: CNCF Blog
source_url: https://www.cncf.io/blog/2026/07/22/i-made-a-policy-engine-think-it-was-in-production/
published_at: '2026-07-22'
---

## 概要

KubernetesネイティブのポリシーエンジンKyvernoは、GlobalContextEntryで実クラスタのリソースを参照するポリシーをCI/CDのCLI上では正しく評価できず、テストがパニックしたり結果が本番と乖離する問題を抱えていた。LFXメンティーが調査した結果、モックデータをCEL/JMESPathが実際に受け取る「[]interface{}のUnstructuredスライス」という形に変換するresolveResourcesMockDataという変換層をCLI側に追加することで、ポリシーエンジン自体には一切手を加えずにオフラインでも本番と同一の評価結果を得られるようにした。
