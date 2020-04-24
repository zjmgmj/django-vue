<template lang="pug">
.crm.main
  //- .crm-topbar.pl-15
  .crm-topbar
    .item.brand.pl-10.row(@click="jump({path: '/dashboard'})")
      div
        img.logo-img(src="../static/logo2.png")
      span.pl-10.ft-16 CRM管理系统
    .item
    .item.flex-50(@click="jump({path: '/setting/profile'})")
      // img.header-img(:src="currentUser.avatar == undefined ? defaultAvatar : currentUser.avatar")
    .item.flex-50.ellps(@click="jump({path: '/setting/profile'})") {{currentUser.name}}
    .item.flex-50(@click="exitAction") 退出
  .crm-sidebar
    side-bar
  .crm-content
    router-view
</template>

<script>
  import sideBar from '@/components/SideBar.vue'
  import { mapState, mapActions } from 'vuex'
  export default {
    middleware: 'mainRouteMatch',
    components: {
      sideBar
    },
    computed: {
      ...mapState({
        currentUser: state => state.user.currentUser,
        defaultAvatar: state => state.defaultAvatar
      })
    },
    methods: {
      ...mapActions([
        'exitUser',
        'clearSearchParams'
      ]),
      exitAction () {
        this.confirmDialog(this, '请确定要退出吗?').then(() => {
          this.serverExit()
        }).catch(() => {
          console.log('cancel')
        })
      },
      async serverExit () {
        try {
          let { data } = await this.apiStreamPost('/proxy/logout', {})
          if (data.returnCode === 0) {
            this.exitUser()
            this.clearSearchParams()
            this.jump({path: '/login'})
          }
        } catch (e) {
          console.error(e)
          this.msgShow(this)
        }
      }
    }
  }
</script>

<style lang="stylus">
@import "../assets/stylus/common"
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
</style>