// @ts-check
import { defineConfig } from 'astro/config';

// https://astro.build/config
export default defineConfig({
  site: 'https://www.kapd-balkan.rs',
  // Set base dynamically: if built on GitHub Actions and not using custom domain, default to '/website'
  base: process.env.GITHUB_ACTIONS && !process.env.CUSTOM_DOMAIN ? '/website' : '/',
});
