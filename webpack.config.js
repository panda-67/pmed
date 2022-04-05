const path = require('path');
module.exports = {
	mode: 'production',
	entry: './src/index.js',
	output: {
		path: path.resolve(__dirname, 'static'),
		filename: 'app.js',
	},
	module: {
		rules: [
			{
				test: /\.js$/i,
				include: path.resolve(__dirname, 'src'),
				use: {
					loader: 'babel-loader',
					options: {
						presets: ['@babel/preset-env'],

					},
				},
			},
			{
				test: /\.css$/i,
				include: path.resolve(__dirname, 'src'),
				use: ['style-loader', 'css-loader', 'postcss-loader'],
			},
		],
	},
	devServer: {
		static: 'dist',
		watchContentBase: true,
	},
	watch: true,
	watchOptions: {
		ignored: [
			/node_modules/,
			/src/,
			/pmed/,
			/article/,
		],
		// aggregateTimeout: 2000,
	},
};
