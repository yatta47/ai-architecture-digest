import { defineCollection, z } from 'astro:content';
import { glob } from 'astro/loaders';

// 1事例 = 1 Markdown。ユーザー提案スキーマを正典にする。
// type でキュレーション（全件取り込み、case/guidance/opinion/announcement に分類）。
const cases = defineCollection({
  loader: glob({ pattern: '**/*.md', base: './src/content/cases' }),
  schema: z.object({
    type: z.enum(['case', 'guidance', 'opinion', 'announcement']),
    // カバレッジ優先度: ソースは網羅的に取り込み、AI関連(true)だけ深掘りしてフルカードにする。
    // false=非AI（周辺技術）は概要＋汎用タグのみの軽量カード。既定 true（既存カードは無指定=フル）。
    ai_relevant: z.boolean().default(true),
    title: z.string(), // 日本語の再構成タイトル（記事名の和訳ではない）
    title_original: z.string().optional(),
    company: z.string().optional(), // 実装主体（cloud基盤とは別）。事例以外は無くてよい
    industry: z.string().optional(), // vocab: industries
    cloud: z.array(z.string()).default([]), // vocab: cloud
    patterns: z.array(z.string()).default([]), // vocab: patterns
    components: z.array(z.string()).default([]), // vocab: components/products
    data_sources: z.array(z.string()).default([]), // free-form
    outcome: z.object({ type: z.string() }).optional(), // vocab: outcomes
    source_id: z.string().optional(),
    source_name: z.string().optional(),
    source_url: z.string().url(),
    // YAML が日付を Date に自動変換するため、文字列/日付どちらも受けて YYYY-MM-DD に正規化
    published_at: z
      .union([z.string(), z.date()])
      .transform((v) => (typeof v === 'string' ? v : v.toISOString().slice(0, 10))),
  }),
});

export const collections = { cases };
