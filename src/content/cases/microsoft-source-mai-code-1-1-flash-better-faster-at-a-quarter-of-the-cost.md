---
type: announcement
title: 実運用RL環境で鍛えた低コストコーディングモデル(MAI-Code-1.1-Flash)
title_original: 'MAI-Code-1.1-Flash: Better, faster, at a quarter of the cost'
company: Microsoft
industry: cross-industry
cloud: []
patterns:
- reinforcement-learning
- inference-optimization
components:
- MAI-Code-1.1-Flash
- GitHub Copilot
- GitHub Copilot CLI
outcome:
  type: cost
source_id: microsoft-source
source_name: Microsoft Source
source_url: https://microsoft.ai/news/mai-code-1-1-flash-br-better-faster-at-a-quarter-of-the-cost/
published_at: '2026-08-11'
---

## 概要

Microsoft AIはGitHub Copilotに本番投入したコーディングモデルMAI-Code-1.1-Flashを発表した。GitHub Copilotでの実運用から得た数十万規模の強化学習環境で学習し、前バージョン比でトークン効率25%向上・コスト4分の1を達成しつつ、コード生存率4%増・再訪率9%増という実利用指標でも改善を確認した。

## 設計のポイント

- 実運用のGitHub Copilot利用データから数十万規模の強化学習環境を構築し、実世界のタスク分布に最適化する『出荷・学習・改善の反復』ループを回した。
- ベンチマークだけでなく実運用指標(コード生存率、再訪率)を主要な評価基準に据え、ユーザー行動で改善を検証した。
- トークン効率を25%改善することで、モデルサイズを大きくせずに応答速度とコストを同時に改善した。

## 使いどころ

- GitHub Copilotで日常的にコード生成・CLI操作を行い、応答速度とコストの両方を重視する開発チーム。
- .NETやターミナル操作など特定タスクでの精度向上を求める開発者。
- 大規模モデルの運用コストを抑えながら品質を落としたくないプロダクトチーム。
