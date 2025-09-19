// ./webpack.mix.js
mix_ = require("laravel-mix");
mix_.webpackConfig({watchOptions: { ignored: /node_modules|dist|mix-manifest.json/ },})
mix_.setPublicPath("dist");

mix_.js("./src/js/module.js", "./dist/js")
    .js("./src/js/custom.js", "./dist/js")
    .scripts(
        [
            "./dist/js/module.js",
            "./dist/js/custom.js"
        ],
        "./dist/js/app.js"
    )

mix_.css("./src/css/custom.css", "./dist/css")
    .css("./src/css/module.css", "./dist/css")
    .postCss("./src/css/tailwind.css", "./dist/css", [require("@tailwindcss/postcss")])
    .styles(
        [
            "./dist/css/custom.css",
            "./dist/css/module.css",
            "./dist/css/tailwind.css"
        ],
        "./dist/css/app.css"
    )