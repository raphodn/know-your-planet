/* eslint-disable */

var PrerenderSpaPlugin = require('prerender-spa-plugin');
var path = require('path');

module.exports = {
  lintOnSave: true, // 'default' makes compilation fail in case of errors
  configureWebpack: config => {
    if (process.env.NODE_ENV !== 'production') return
    return {
      plugins: [
        new PrerenderSpaPlugin({
          // Required - The path to the webpack-outputted app to prerender.
          staticDir: path.join(__dirname, 'dist'),
          // Required - Routes to render.
          routes: [ '/', '/a-propos', '/contribuer', '/glossaire'],
        }),
      ]
    }
  }
};