<template>
  <section class="container">
    <div>
      <h1 class="title">
        crm-client
      </h1>
      <h2 class="subtitle xx">
        Nuxt.js project
      </h2>
      <div class="links">
        <a
          href="https://nuxtjs.org/"
          target="_blank"
          class="button--green">Documentation</a>
        <a
          href="https://github.com/nuxt/nuxt.js"
          target="_blank"
          class="button--grey">GitHub</a>
      </div>
    </div>
    <el-button type="primary">Default</el-button>
  </section>
</template>

<script>

export default {
  layout: 'main',
  middleware: 'indexJump',
  components: {
  }
}
</script>

<style lang="stylus">
</style>
