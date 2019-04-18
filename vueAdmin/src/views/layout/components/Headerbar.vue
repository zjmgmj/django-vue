<template lang="pug">
  .crm-topbar.pl-15.navbar
    .item.brand.pl-5.row
      div
        img.logo-img
      //- span.pl-10.ft-16 箴易科技
    .item(style="text-align: right;") 一号门店
    .item.flex-50
      el-tooltip(:content="$t('navbar.screenfull')", effect="dark", placement="bottom")
        screenfull.screenfull.right-menu-item
    .item.flex-50
      el-dropdown.avatar-container.right-menu-item(trigger="click")
        .avatar-wrapper
          img.user-avatar(:src="avatar+'?imageView2/1/w/80/h/80'")
          i.el-icon-caret-bottom
        el-dropdown-menu(slot="dropdown")
          span(style="display:block;", @click="logout") 退出
          //- router-link(to="/")
          //-   el-dropdown-item {{ $t('navbar.dashboard') }}
          //- router-link(to="/")
            el-dropdown-item {{ $t('navbar.dashboard') }}
        //- el-dropdown-item(divided)
          //- span(style="display:block;", @click="logout") {{ $t('navbar.logOut') }}
          span(style="display:block;", @click="logout") 退出
</template>
<script>
import { mapGetters } from 'vuex'
import Screenfull from '@/components/Screenfull'

export default {
  name: 'Headerbar',
  components: {
    Screenfull
  },
  computed: {
    ...mapGetters([
      'sidebar',
      'name',
      'avatar',
      'device'
    ])
  },
  methods: {
    toggleSideBar() {
      this.$store.dispatch('toggleSideBar')
    },
    logout() {
      this.$store.dispatch('LogOut').then(() => {
        location.reload()// In order to re-instantiate the vue-router object to avoid bugs
      })
    }
  }
}
</script>

<style rel="stylesheet/scss" lang="scss" scoped>
.header-img{
  border-radius: 50%;
  width: 36px;
  height: 36px;
  margin-top: 7px;
}
.logo-img{
  width: 50px;
  padding-top: 16px;
}
.row{
  align-items: center;
}
.screenfull {
  height: 20px;
  margin-top: 14px;
}
.screenfull >>> .screenfull-svg{
  fill: #fff;
}
.international{
  vertical-align: top;
}
.theme-switch {
  vertical-align: 15px;
}
.avatar-container {
  height: 50px;
  margin-right: 30px;
  .avatar-wrapper {
    margin-top: 5px;
    position: relative;
    .user-avatar {
      cursor: pointer;
      width: 40px;
      height: 40px;
      border-radius: 10px;
    }
    .el-icon-caret-bottom {
      cursor: pointer;
      position: absolute;
      right: -20px;
      top: 25px;
      font-size: 12px;
    }
  }
}
</style>
