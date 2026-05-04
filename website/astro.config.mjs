// @ts-check
import { defineConfig } from 'astro/config';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

const __dirname = path.dirname(fileURLToPath(import.meta.url));

// https://astro.build/config
export default defineConfig({
  site: 'https://jbrinkman.github.io',
  base: '/valkey-analysis',
  output: 'static',
  vite: {
    resolve: {
      alias: {
        '../../results/results.json': path.resolve(__dirname, '..', 'results', 'results.json'),
      },
    },
    server: {
      fs: {
        allow: ['..'],
      },
    },
  },
});
