---
type: case
title: AI家庭教師評価のための学習者シミュレータStudentSim
title_original: Simulating student learning for better AI tutoring
company: Microsoft
industry: public-sector
cloud: []
patterns:
- eval
- fine-tuning
components:
- StudentSim
- StudentSimEval
outcome:
  type: quality
source_id: microsoft-source
source_name: Microsoft Source
source_url: https://www.microsoft.com/en-us/research/blog/simulating-student-learning-for-better-ai-tutoring/
published_at: '2026-10-12'
---

## 概要

StudentSimは公開の匿名化学習記録から個々の学生を模したシミュレータを学習し、AIチューターの評価・改善に使う研究システムである。チェス、英作文、数学で既存手法を上回り、学習フィードバックとして使える。

## 設計のポイント

- LLMへのロールプレイではなく個人別に学習したシミュレータにする。
- 個人らしさと指導後の更新という2軸で評価する。

## 使いどころ

- 実学習者での試験前にAIチューターを反復改善する研究開発。
