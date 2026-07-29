---
type: announcement
title: ローカルVMツールLimaがWindowsゲストとTPM 2.0エミュレーションに対応
title_original: 'Lima v2.2: Windows guests and TPM 2.0 emulation'
ai_relevant: false
industry: cross-industry
cloud: []
patterns: []
components: []
outcome:
  type: productivity
source_id: cncf-blog
source_name: CNCF Blog
source_url: https://www.cncf.io/blog/2026/07/28/lima-v2-2-windows-guests-and-tpm-2-0-emulation/
published_at: '2026-07-29'
---

## 概要

Lima v2.2は、Linux/macOS/FreeBSDに加えてWindows Server 2025やWindows 11をゲストとして起動できる実験的サポートを追加した。autounattend.xmlによる無人インストールやvirtio-winドライバ、SSHの自動セットアップにより`limactl`から単一ワークフローでWindows VMを操作できる。あわせてswtpmによるTPM 2.0エミュレーションも導入し、Windows 11の要件を満たしつつディスク暗号化などのワークフローを可能にした。
