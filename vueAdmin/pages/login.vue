<template lang="pug">
.login-container
  .login-box
    .logo
    .text-content
      .one
        .txt
          span 客户
        .txt
          span 商机
        .txt
          span 销售
      .two 尽在型云CRM
      .three
        span 推动业务进展
        span 提高工作效率
        span 管理大数据
    .content
      h1 型云CRM管理系统
      .box
        el-form(:model="loginModel",:rules="loginRules", ref="loginForm", status-icon)
          el-form-item(prop="acct")
            el-input(placeholder="请输入账号", v-model="loginModel.acct", :maxlength="20")
          el-form-item(prop="pwd")
            el-input(placeholder="请输入登录密码", v-model="loginModel.pwd", type="password", :maxlength="20")
          el-form-item.flex(prop="codeConfirm")
            .col
              el-input(placeholder="请输入验证码", v-model="loginModel.codeConfirm", :maxlength="4", @keyup.enter.native="submit('loginForm')")
            .col.code
              graphic-code(:identifyCode="code", @refresh="refreshCode") 验证码
          el-button(type="primary", size="medium", style="border-radius: 0px; width: 100%", @click="submit('loginForm')") 登录
</template>

<script>
  import graphicCode from '@/components/GraphicCode.vue'
  import sha1 from 'sha1'
  import { mapActions } from 'vuex'
  import _ from 'lodash'
  export default {
    components: {
      graphicCode
    },
    data () {
      var codeValidate = (rule, value, cb) => {
        if (value.trim() === '') {
          cb(new Error('不能为空'))
        } else if (this.loginModel.codeConfirm.trim().toLocaleLowerCase() !== this.code.toLocaleLowerCase()) {
          cb(new Error('验证码输入错误'))
        } else {
          cb()
        }
      }
      return {
        code: '',
        loginModel: {
          acct: '',
          pwd: '',
          codeConfirm: ''
        },
        loginRules: {
          acct: [{required: true, message: '不能为空', trigger: 'blur'}],
          pwd: [{required: true, message: '不能为空', trigger: 'blur'}],
          codeConfirm: [{validator: codeValidate, trigger: 'blur'}]
        }
      }
    },
    beforeMount () {
      this.configVal({key: 'globalErrorMsg', val: ''})
      this.code = this.getValidateCode()
    },
    methods: {
      ...mapActions([
        'configVal',
        'setUser'
      ]),
      refreshCode () {
        this.code = this.getValidateCode()
      },
      submit (formName) {
        this.$refs[formName].validate((valid) => {
          if (valid) {
            this.login()
          } else {
            console.error('error submit!!')
            return false
          }
        });
      },
      async login () {
        let encodePwd = sha1(this.loginModel.pwd.trim())
        let now = this.date2Str(new Date())
        let { data } = await this.apiStreamPost('/proxy/common/post', {url: 'login', params: {code: this.code, acct: this.loginModel.acct.trim(), pwd: encodePwd, hashCode: sha1(now+this.code)}})
        if (data.returnCode === 0) {
          let params = {
            loginAcct: this.loginModel.acct.trim(),
            ip: data.currentUser.ipAddress,
            deviceType: navigator.userAgent.toLowerCase()
          }
          this.createLoginMsg(params)
          this.setUser(data.currentUser)
          this.configVal({key: 'globalSuccessMsg', val: '登录成功'})
          let pageUrl = '/'
          if (data.currentUser.id !== 1) {
            const userAuthGroup = _.groupBy(data.currentUser.auths, (itm) => {
              return itm.fkMenu.parent.factOrder
            })
            const firstKey = Object.keys(userAuthGroup)[0]
            pageUrl = (userAuthGroup[firstKey][0]).fkMenu.pageUrl
          }
          this.jump({path: data.currentUser.id !== 1 ? pageUrl : '/'})
          setTimeout(() => {
            this.visitDialogData(data.currentUser.id)
          }, 6000);
        } else {
          this.msgShow(this, data.errMsg)
          this.refreshCode()
        }
      },
      async createLoginMsg (params) {
        try {
          let { data } = await this.apiStreamPost('/proxy/common/post', {url: 'setting/loginMsg/create', params: params})
          if (data.returnCode === 0) {
          } else {
            this.msgShow(this, data.errMsg)
          }
        } catch (e) {
          console.error(e)
          this.msgShow(this)
        } 
      },
      async visitDialogData (uid) {
        try {
          let params = {
            currentPage: 0,
            pageSize: 3,
            mark: '1',
            uid: uid
            // startTime: this.date2Str(new Date()),
            // endTime: this.date2Str(new Date())
          }
          let { data } = await this.apiStreamPost('/proxy/common/post', {url: 'customerManage/cstmCall', params: params})
          if (data.returnCode === 0) {
            if(data.list.length>0){
              let temp = ''
              data.list.map(itm => {
                itm[0].planVisitTime = this.datetime2Str(new Date(itm[0].planVisitTime))
                itm[0].compName = itm[0].customer.compName
                // temp += '<div style="cursor: pointer; margin-bottom: 15px;"><div>' + itm[0].planVisitTime + '</div>'+ itm[0].compName + '</div>'
                temp += '<div style="cursor: pointer; margin-bottom: 15px;"><div>名称：' + itm[0].compName + '</div><div>拜访时间：' + itm[0].planVisitTime + '</div>'
              })
              this.visitNotify(temp)
            }
          } else {
            this.msgShow(this, data.errMsg)
          }
        } catch (e) {
          console.error(e)
          this.msgShow(this)
        }
      },
      visitNotify(temp) {
        let me = this
        this.$notify({
          title: '您有以下客户需要拜访：',
          dangerouslyUseHTMLString: true,
          message: temp,
          onClick: function(){
            me.jump({path: '/customManager/customerVisit'})
          }
        })
      }
    }
  }
</script>

<style lang="stylus">
* {
  -webkit-top-highlight-color: transparent;
  -webkit-box-sizing: border-box !important;
  box-sizing: border-box !important;
}
body,html
  font-family: 'PingFang SC', 'Microsoft Yahei', 'SimSun', 'Helvetica', 'STHeitiSC-Light', 'Helvetica-Light', arial, sans-serif, 'Droid Sans Fallback'
  font-size: 14px
  color: #262626
.login-container
  position fixed
  top 0
  bottom 0
  left 0
  right 0
  margin 0 auto
  padding 0 auto
  background linear-gradient(to bottom, #163069, #082940)
  background -prefix-linear-zgradient(top, #163069, #082940)
  // background #173068
  // background-image url('http://pav6lmvyn.bkt.clouddn.com/login_bg.jpg')
  background-size cover
  background-position center
  overflow hidden
  .login-box
    display flex
    overflow hidden
    margin 0 auto
    position relative
    width 1400px
    height 600px
    top calc((100% - 600px) / 2)
    align-items center
    .logo
      flex 0 0 450px
      height 600px
      background-image url('http://pav6lmvyn.bkt.clouddn.com/login_logo_new.png?imageView2/2/w/450/h/465')
      background-repeat no-repeat
      // background-size cover
      background-position center
    .text-content
      flex 0 0 500px
      color #fff
      font-family 'Microsoft Yahei'
      // padding-left 15px
      .one
        display flex
        line-height 36px
        font-size 36px
        text-align center
        .txt
          flex 1
          span
            display inline-block
            position relative
            &:before
              position absolute
              content ''
              border-radius 50%
              width 8px
              height 8px
              background #fff
              left -18px
              top 14px

      .two
        padding-top 30px
        font-size 54px
        text-align center
      .three
        padding-top 30px
        font-size 20px
        text-align center
        span
          margin-right 15px
          &:last-child
            margin-right 0px
    .content
      flex 0 0 450px
      padding-left 15px
      text-align center
      color #fff
      .box
        margin 0 auto
        width 400px
        background #fff
        box-sizing border-box
        padding 30px 30px
        margin-top 15px
        .el-input__inner
          border-radius 0px !important
        .el-form-item.flex
          .el-form-item__content
            width 100%
            display -webkit-box
            display -webkit-flex
            display flex
            flex-wrap wrap
            .col
              flex 1
              &.code
                flex 0 0 180px
                padding-left 20px

</style>
