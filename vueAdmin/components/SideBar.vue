<template lang="pug">
el-menu(background-color="#42485b", text-color="#fff", active-text-color="#fff", router, :default-active="currentPathIdx", :unique-opened="true")
  template(v-for="(menu,idx) in currentMenus")
    template(v-if="menu.subItems")
      el-submenu(:index="menu.title")
        template(slot="title")
          i(v-if="menu.iconClass", :class="menu.iconClass")
          span {{menu.title}}
        el-menu-item(:index="(idx + 1) + '-' + (subIdx + 1)", :route="itm.url ? itm.url : '#'", v-for="(itm, subIdx) in menu.subItems", :key="subIdx") {{itm.title}}
    el-menu-item(:index="menu.title", :route="menu.url ? menu.url : '#'", v-else) {{menu.title}}
</template>

<script>
  import { mapState } from 'vuex'
  export default {
    computed: {
      ...mapState({
        currentPathIdx: state => state.currentPathIdx,
        currentMenus: state => state.currentMenus
      })
    }
  }
</script>

<style lang="stylus", scoped>

</style>
