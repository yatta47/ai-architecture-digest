---
type: announcement
title: GitHub EnterpriseにおけるSSO認可の一括自動化API
title_original: Automate SSO authorization for classic PATs and SSH keys
ai_relevant: false
industry: cross-industry
cloud: []
patterns: []
components: []
outcome:
  type: risk-compliance
source_id: github-changelog
source_name: GitHub Changelog
source_url: https://github.blog/changelog/2026-09-16-automate-sso-authorization-for-classic-pats-and-ssh-keys
published_at: '2026-09-16'
---

## 概要

GitHub Enterprise Cloudの管理者が、SSO保護された複数組織にまたがるクラシックPATやSSHキーの認可を、GitHub App経由のAPIで一括自動化できるようになった。従来は組織ごとに手動認可が必要で長期トークンの温床になっていた課題を、1リクエストで最大50組織へのバルク認可により解消する。
