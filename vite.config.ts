import { defineConfig } from 'vite';
import react from '@vitejs/plugin-react';
import path from 'path';

export default defineConfig({
  plugins: [react()],
  resolve: {
    alias: {
      '@': path.resolve(__dirname, 'client/src'),
    },
  },
  server: { port: 3000, host: true },
  build: {
    outDir: 'client/dist',
    rollupOptions: {
      input: 'client/index.html',
      output: {
        entryFileNames: 'assets/index-[hash].js',
        chunkFileNames: 'assets/index-[hash].js',
        assetFileNames: 'assets/index-[hash].[ext]',
      },
    },
    sourcemap: false,
    emptyOutDir: false,
  },
});
