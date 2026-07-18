import { defineConfig } from 'astro/config';
import sitemap from '@astrojs/sitemap';

// GitHub Pages（project pages）公開: site + base で https://yatta47.github.io/ai-architecture-digest/ に出る。
// 内部リンクは src/lib/facets.ts の url() が import.meta.env.BASE_URL を前置するため base 追従。
// ローカル目視は `npm run preview`（astro preview は base を尊重してサブパスで配信する）。
export default defineConfig({
  site: 'https://yatta47.github.io',
  base: '/ai-architecture-digest',
  integrations: [sitemap()],
});
