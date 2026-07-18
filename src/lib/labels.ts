// facet 値の「表示専用」日本語ラベル。
// 内部値（スラッグ）は英語のまま保持し（URL・ファセット集約・重複判定のキー）、
// 表示だけ日本語に変換する。未マップの facet / 未知スラッグは生値にフォールバックする。
const MAPS: Record<string, Record<string, string>> = {
  // vocab/industries.yml ＋ データに出た vocab 外（legal 等）を含める
  industries: {
    'financial-services': '金融',
    manufacturing: '製造',
    healthcare: 'ヘルスケア',
    retail: '小売',
    'public-sector': '公共',
    media: 'メディア',
    telecom: '通信',
    logistics: '物流',
    legal: '法務',
    'cross-industry': '業界横断',
    other: 'その他',
  },
  // vocab/outcomes.yml
  outcomes: {
    productivity: '生産性',
    cost: 'コスト',
    quality: '品質',
    revenue: '収益',
    'risk-compliance': 'リスク・コンプライアンス',
    speed: '速度',
    reliability: '信頼性',
  },
};

/** facet 種別 kind の値 value を日本語表示ラベルに。無ければ生値を返す。 */
export function label(kind: string, value: string | undefined | null): string {
  if (!value) return '';
  return MAPS[kind]?.[value] ?? value;
}
