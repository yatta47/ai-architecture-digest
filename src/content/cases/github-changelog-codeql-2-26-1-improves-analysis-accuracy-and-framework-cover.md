---
type: announcement
title: 静的解析エンジンCodeQL 2.26.1、フレームワーク網羅性向上と誤検知削減
title_original: CodeQL 2.26.1 improves analysis accuracy and framework coverage
ai_relevant: false
company: GitHub
industry: cross-industry
cloud: []
patterns: []
components: []
outcome:
  type: quality
source_id: github-changelog
source_name: GitHub Changelog
source_url: https://github.blog/changelog/2026-07-29-codeql-2-26-1-improves-analysis-accuracy-and-framework-coverage
published_at: '2026-07-29'
---

## 概要

CodeQL 2.26.1がリリースされ、Go（log/slogパッケージ）、Java/Kotlin（Apache POI）、JavaScript/TypeScript（Angularの@HostListenerデコレータ）のフレームワークカバレッジが拡張された。あわせてRustのハードコード暗号値検出クエリでは、算術・ビット演算・文字列連結を「バリア」として扱うことで、ノンス増分などに伴う誤検知（false positive）を削減した。新バージョンはgithub.com上のコードスキャニング利用者に自動適用され、将来のGitHub Enterprise Serverリリースにも反映される。
