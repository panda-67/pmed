module.exports = {
	content: [
		'./template/**',
		'./template/*/*.html'],
	theme: {
		extend: {},  
	},
	plugins: [
		require('@tailwindcss/forms'),
		require('daisyui'),
	],
}
