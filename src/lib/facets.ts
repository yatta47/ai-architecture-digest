import { getCollection, type CollectionEntry } from 'astro:content';

export type CaseEntry = CollectionEntry<'cases'>;

/** URL 安全な slug に落とす（表示ラベルは別途保持する）。
 * Unicode 文字/数字は保持する（\p{L}\p{N}）＝日本語のファセット値が
 * 全て空→'item' に潰れて1ページに合流するバグを防ぐ。ASCII の挙動は従来と同じ。 */
export function slugify(s: string): string {
  const out = s
    .normalize('NFC') // NFD混入(結合文字)で「か/が」等が別slugに分裂/合流するのを防ぐ
    .toLowerCase()
    .trim()
    .replace(/[^\p{L}\p{N}]+/gu, '-')
    .replace(/^-+|-+$/g, '');
  return out || 'item';
}

/** base（'/' or '/ai-architecture-digest/'）を尊重した内部リンク */
export function url(path: string): string {
  const base = import.meta.env.BASE_URL;
  const b = base.endsWith('/') ? base : base + '/';
  return b + path.replace(/^\/+/, '');
}

/** 全事例を新しい順で返す */
export async function allCases(): Promise<CaseEntry[]> {
  const cases = await getCollection('cases');
  return cases.sort((a, b) => (a.data.published_at < b.data.published_at ? 1 : -1));
}

export type Accessor = (e: CaseEntry) => string[];

/** 各 facet の「エントリ→ラベル配列」定義 */
export const accessors: Record<string, Accessor> = {
  cloud: (e) => e.data.cloud,
  patterns: (e) => e.data.patterns,
  components: (e) => e.data.components,
  industries: (e) => (e.data.industry ? [e.data.industry] : []),
  companies: (e) => (e.data.company ? [e.data.company] : []),
  outcomes: (e) => (e.data.outcome?.type ? [e.data.outcome.type] : []),
};

/** getStaticPaths 用: facet の全値をルート化（空値は生成しない） */
export function facetPaths(entries: CaseEntry[], accessor: Accessor) {
  const map = new Map<string, { label: string; items: CaseEntry[] }>();
  for (const e of entries) {
    const seen = new Set<string>(); // 同一記事が複数ラベル→同一slugでも1回だけ入れる
    for (const label of accessor(e)) {
      if (!label) continue;
      const slug = slugify(label);
      if (seen.has(slug)) continue;
      seen.add(slug);
      if (!map.has(slug)) map.set(slug, { label, items: [] });
      map.get(slug)!.items.push(e);
    }
  }
  return [...map.entries()].map(([slug, v]) => ({
    params: { slug },
    props: { label: v.label, items: v.items },
  }));
}

/** サイドナビ用: facet の値と件数（件数降順） */
export function facetSummary(entries: CaseEntry[], accessor: Accessor) {
  const map = new Map<string, { label: string; count: number }>();
  for (const e of entries) {
    const seen = new Set<string>(); // 件数は「記事数」＝同一記事の重複カウントを防ぐ
    for (const label of accessor(e)) {
      if (!label) continue;
      const slug = slugify(label);
      if (seen.has(slug)) continue;
      seen.add(slug);
      if (!map.has(slug)) map.set(slug, { label, count: 0 });
      map.get(slug)!.count++;
    }
  }
  return [...map.entries()]
    .map(([slug, v]) => ({ slug, label: v.label, count: v.count }))
    .sort((a, b) => b.count - a.count);
}

/** 本文から見出し行（## 概要 等）を除いたプレーン抜粋を作る */
export function plainExcerpt(body: string | undefined, n = 140): string {
  return (body || '')
    .split('\n')
    .filter((l) => !/^#{1,6}\s/.test(l.trim())) // 見出し行を除外
    .join(' ')
    .replace(/\s+/g, ' ')
    .trim()
    .slice(0, n);
}

function tagsOf(e: CaseEntry): Set<string> {
  const t = new Set<string>();
  e.data.cloud.forEach((x) => t.add('cloud:' + slugify(x)));
  e.data.patterns.forEach((x) => t.add('pat:' + slugify(x)));
  e.data.components.forEach((x) => t.add('comp:' + slugify(x)));
  if (e.data.industry) t.add('ind:' + slugify(e.data.industry));
  return t;
}

/** 類似事例: cloud/patterns/components/industry の重み付きJaccardで算出（AI不要） */
export function similarCases(target: CaseEntry, all: CaseEntry[], n = 3) {
  const t = tagsOf(target);
  return all
    .filter((e) => e.id !== target.id)
    .map((e) => {
      const s = tagsOf(e);
      let inter = 0;
      for (const x of t) if (s.has(x)) inter++;
      const union = new Set([...t, ...s]).size;
      return { entry: e, score: union ? inter / union : 0, shared: inter };
    })
    .filter((x) => x.shared > 0)
    .sort((a, b) => b.score - a.score)
    .slice(0, n);
}
