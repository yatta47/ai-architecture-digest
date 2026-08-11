---
type: guidance
title: 分散型インフラで運用されるランサムウェアDeadLockの技術分析と対策
title_original: Microsoft Details DeadLock Extortion Tactics
ai_relevant: false
company: Microsoft
industry: cross-industry
cloud: []
patterns: []
components: []
outcome:
  type: risk-compliance
source_id: microsoft-source
source_name: Microsoft Source
source_url: https://www.microsoft.com/en-us/security/blog/2026/08/10/deadlock-ransomware-breaking-down-a-rust-based-encryptor-with-decentralized-recovery-infrastructure/
published_at: '2026-08-10'
---

## 概要

MicrosoftはDeadLockと呼ばれる新興のランサムウェアグループを追跡しており、被害者との交渉やデータリークサイト運営にSessionメッセージングネットワークとブロックチェーン連携サービスを組み合わせた分散型インフラを使うことで、摘発への耐性を高めている点が特徴だと報告する。2025年7月の初観測以降、二重恐喝(暗号化とデータ公開の脅迫)を行い、2026年7月時点で80組織以上を被害者リストに公開している。本稿ではDeadLockの実行フロー、防御回避手法、暗号化設計、旧ソ連圏を避けるジオフェンシングなどを技術的に解説し、IOCと緩和策を提供する。
