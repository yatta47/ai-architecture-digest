---
type: case
title: CVS Healthが実践する評価駆動開発——AIパイロットを本番に定着させる3層の規律
title_original: 'Evaluation-driven development: How to move AI agents from pilot to production'
company: CVS Health
industry: healthcare
cloud: []
patterns:
- eval
- spec-driven-development
- llmops
components: []
outcome:
  type: speed
source_id: arize-blog
source_name: Arize Blog
source_url: https://arize.com/blog/evaluation-driven-development-ai-agents-production/
published_at: '2026-08-13'
---

## 概要

CVS Healthが4週間かかっていた機能を1.5日、6〜9ヶ月見積もりのレガシー書き換えを1ヶ月で完了させた事例を基に、仕様書・評価ハーネス・AIオブザーバビリティ・コスト計測を核とするAIネイティブな開発ライフサイクルを解説。個人の生産性向上（レイヤー1）からチーム間の共有コンテキスト（レイヤー2）へと規律を積み上げる。

## 設計のポイント

- 仕様書をエンジニアとエージェント双方が参照する『信頼できる唯一の情報源』とし、実装前に意図を明文化させる
- コーディング支援ツールによる個人の生産性向上を、共有コンテキストとチーム間の依存関係マップで組織的な速度に転換する
- デモが動くことと本番に定着することを区別し、リリース基準・監視・所有権・ROIをモデル改善とは別に設計する

## 使いどころ

- AIパイロットが『pilot purgatory（パイロット煉獄）』から抜け出せない大企業のエンジニアリング組織
- コーディングエージェントの生産性向上を全社的な開発速度に変換したいプラットフォームチーム
