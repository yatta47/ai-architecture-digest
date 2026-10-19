---
type: announcement
title: CodeQLがmacOS 27・Xcode 27・Swift 6.4で制約を受ける
title_original: CodeQL changes for macOS 27, Xcode 27 and Swift 6.4
ai_relevant: false
company: GitHub
industry: cross-industry
cloud: []
patterns: []
components: []
outcome:
  type: reliability
source_id: github-changelog
source_name: GitHub Changelog
source_url: https://github.blog/changelog/2026-10-19-codeql-changes-for-macos-27-xcode-27-and-swift-6-4
published_at: '2026-10-19'
---

## 概要

AppleがmacOS 27とXcode 27の一部システムバイナリからIntelコードを外したため、CodeQLはこれらの環境で追跡型スキャンができず、Swift 6.4も解析できない。Swiftや追跡ビルドを使う場合はmacOS 26以前とXcode 26以前に固定し、C/C++、C#、Javaはbuild mode noneへ切り替えられる。
