<template lang="pug">
.content
  .row.ft-24 11111111
</template>

<script>
  import { mapActions } from 'vuex'
  export default {
    layout: 'main',
    data () {
      return {
        currentUser:{
          id:1,
          createAt:1544767935000,
          updateAt:1544767935000,
          name:"超级管理员",
          fkDpt:{id:1,createAt:1544767931000,updateAt:1544767931000,name:"电商平台服务部",leader:"曹玉林",status:1,remark:null,
            fkOrg:{id:1,createAt:1544767931000,updateAt:1544767931000,name:"江苏智恒达型云网络科技有限公司",simpleName:"型云",status:1,legalRept:null,remark:null}},
          loginAcct:"admin",
          pwd:"1f82c942befda29b6ed487a51da199f78fce7f05",
          phone:"88888888888",
          status:1,
          fkRole:{id:1,createAt:1544767931000,updateAt:1544767931000,name:"superadmin",auths:[],status:1},
          auths:[],
          dataLevel:"公司",
          sex:1,
          national:null,
          position:null,
          edu:null,
          professional:null,
          email:null,
          jobTitle:null,
          telephone:null,
          addr:null,
          nativePlace:null,
          maritalStatus:null,
          politicalLandscape:null,
          birthday:null,
          inTime:null,
          workGroup:null,
          remark:null,
          avatar:null,
          platformCode:null,
          demission:0,
          loginTime:1556086423969,
          ipAddress:"172.16.120.235"}
      }
    },
    components: {},
    mounted () {
      this.setUser(this.currentUser)
    },
    methods: {
      ...mapActions([
        'setUser'
      ]),
    }
  }
</script>
<style lang="stylus", scoped>
  .avatar{
    width: 120px;
    height: 120px;
    border-radius: 100%;
    overflow: hidden;
    border: 4px #fff solid;
  }
  .avatar img{
    width: 100%;
    height: 100%;
  }
  .box-header{
    border-radius: 10px;
  }
  .elTabPaneSale{
    height: 880px;
  }
  .elTabPaneTask {
    height: 600px;
  }
</style>