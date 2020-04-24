module.exports = {
  root: true,
  env: {
    browser: true,
    node: true
  },
  parserOptions: {
    parser: 'babel-eslint'
  },
  extends: [
    // '@nuxtjs',
    // 'plugin:nuxt/recommended',
    // 'plugin:prettier/recommended',
    // 'prettier',
    // 'prettier/vue'
    'plugin:vue/essential'
  ],
  plugins: [
    // 'prettier'
    'vue'
  ],
  // add your custom rules here
  rules: {
    // 'nuxt/no-cjs-in-config': 'off'
  }
}
