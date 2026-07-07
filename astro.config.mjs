// @ts-check
import { defineConfig } from 'astro/config';

// https://astro.build/config
export default defineConfig({
  site: 'https://zigikralj.github.io', // Change this to your custom domain or https://<username>.github.io
  // Set base dynamically: if built on GitHub Actions and not using custom domain, default to '/website'
  base: process.env.GITHUB_ACTIONS && !process.env.CUSTOM_DOMAIN ? '/kapd-balkan/' : '/',
  output: 'static',
});
