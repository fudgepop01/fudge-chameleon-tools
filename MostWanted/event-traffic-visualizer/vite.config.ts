import { sveltekit } from '@sveltejs/kit/vite';
import commonjs from '@rollup/plugin-commonjs';
import { defineConfig } from 'vite';

export default defineConfig({
	plugins: [sveltekit()],
	// optimizeDeps: {
	// 	exclude: ['plotly.js']
	// },
	// build: {
	// 	commonjsOptions: { transformMixedEsModules: true }
	// }
});
