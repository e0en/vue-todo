const frontendPath = require('./settings.js').frontendPath
const path = require('path')
const PurgecssPlugin = require('purgecss-webpack-plugin')
const glob = require('glob-all')

module.exports = {
  publicPath: frontendPath,
  pwa: {
    manifestOptions: {
      scope: frontendPath
    }
  },
  configureWebpack: {
    plugins: [
      new PurgecssPlugin({
        paths: glob.sync([
          path.join(__dirname, './../src/index.html'),
          path.join(__dirname, './../**/*.vue'),
          path.join(__dirname, './../src/**/*.js')
        ])
      })
    ]
  }
}
