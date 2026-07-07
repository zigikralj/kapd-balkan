// @ts-check
import { defineConfig } from 'astro/config';

// https://astro.build/config
export default defineConfig({
  site: 'https://kapd-balkan.rs',
  base: '/',
  output: 'static',
  i18n: {
    defaultLocale: 'sr',
    locales: ['sr', 'en'],
    routing: {
      prefixDefaultLocale: false,
    },
  },
});
