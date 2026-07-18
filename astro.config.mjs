import { defineConfig } from 'astro/config';
import sitemap from '@astrojs/sitemap';

// MVP はローカル確認用に base='/' で組む。
// GitHub Pages（project pages）公開時は base='/ai-architecture-digest' に変更する。
export default defineConfig({
  site: 'https://yatta47.github.io',
  base: '/',
  integrations: [sitemap()],
});
