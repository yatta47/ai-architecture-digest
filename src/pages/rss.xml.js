import rss from '@astrojs/rss';
import { getCollection } from 'astro:content';
import { plainExcerpt } from '../lib/facets';

export async function GET(context) {
  const cases = await getCollection('cases');
  cases.sort((a, b) => (a.data.published_at < b.data.published_at ? 1 : -1));
  return rss({
    title: 'AI Architecture 事例カタログ',
    description: '追跡ソースの新着を切り口で引ける事例カタログ',
    site: context.site,
    items: cases.map((e) => {
      const item = {
        title: e.data.title,
        description: plainExcerpt(e.body, 200),
        link: `/cases/${e.id}/`,
      };
      // published_at が欠損/不正な生成エントリでも RSS を壊さない
      const d = e.data.published_at ? new Date(e.data.published_at) : null;
      if (d && !Number.isNaN(d.getTime())) item.pubDate = d;
      return item;
    }),
  });
}
