<template lang="pug">
.error-page
  template(v-if="error.statusCode == 404")
    .blank-logo
    .text-center
      h2 Sorry，您访问的页面不见了
      el-button(type="primary", @click="back", size="medium") 返回
  template(v-else)
    h1 {{error.statusCode}}
    h3 Error: {{error.message}}

</template>

<script>
  export default {
    props: ['error']
  }
</script>

<style lang="stylus">
.error-page
  position fixed
  top 0
  bottom 0
  left 0
  right 0
  width 100%
  .text-center
    text-align center
  .blank-logo
    background-image url('http://pav6lmvyn.bkt.clouddn.com/404.png?imageView2/0/w/500/h/250')
    width 500px
    height 250px
    margin 0 auto
    margin-top 15%
</style>