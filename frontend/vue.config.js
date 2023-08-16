const { defineConfig } = require("@vue/cli-service");
const path = require("path");

module.exports = defineConfig({
  transpileDependencies: true,
  lintOnSave: false,
  configureWebpack: {
    module: {
      rules: [
        {
          test: /\.(js|vue)$/,
          loader: "eslint-loader",
          enforce: "pre",
          include: [path.resolve(__dirname, "src")],
          options: {
            rules: {
              "vue/multi-word-component-names": "off",
            },
          },
        },
      ],
    },
  },
  css: {
    loaderOptions: {
      sass: {
        implementation: require("sass"),
        sassOptions: {
          indentedSyntax: false, // 만약 .sass 파일을 사용한다면 true로 설정
        },
      },
    },
  },
});
