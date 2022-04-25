/** @format */

const path = require("path");

module.exports = {
    mode: "production",
    entry: {
        style: "./src/bootstrapcss.js",
        bundle: "./src/bundle.js"
    },
    output: {
        filename: "[name].js",
        path: path.resolve(__dirname, "static"),
    },
    module: {
        rules: [
            {
                test: /\.(scss)$/,
                use: [
                    {
                        // inject CSS to page
                        loader: "style-loader",
                    },
                    {
                        // translates CSS into CommonJS modules
                        loader: "css-loader",
                    },
                    {
                        // Run postcss actions
                        loader: "postcss-loader",
                        options: {
                            // `postcssOptions` is needed for postcss 8.x;
                            // if you use postcss 7.x skip the key
                            postcssOptions: {
                                // postcss plugins, can be exported to postcss.config.js
                                plugins: function () {
                                    return [require("autoprefixer")];
                                },
                            },
                        },
                    },
                    {
                        // compiles Sass to CSS
                        loader: "sass-loader",
                    },
                ],
            },
        ],
    },
    watchOptions: {
        aggregateTimeout: 200,
        ignored: ["/node_modules", "/src", "/pmed", "/user_auth"],
    },
};

// module.exports = {
//     mode: "production",
//     entry: {
//         app: "./src/index.js",
//     },
//     output: {
//         path: path.resolve(__dirname, "static"),
//         filename: "app.js",
//     },
//     module: {
//         rules: [
//             {
//                 test: /\.js$/i,
//                 include: path.resolve(__dirname, "src"),
//                 use: {
//                     loader: "babel-loader",
//                     options: {
//                         presets: ["@babel/preset-env"],
//                     },
//                 },
//             },
//             {
//                 test: /\.css$/i,
//                 include: path.resolve(__dirname, "src"),
//                 use: ["style-loader", "css-loader", "postcss-loader"],
//             },
//         ],
//     },
//     devServer: {
//         static: "dist",
//         watchContentBase: true,
//     },
//     watchOptions: {
//         aggregateTimeout: 200,
//         ignored: ["/node_modules", "/src", "/pmed", "/user_auth"],
//     },
// };
