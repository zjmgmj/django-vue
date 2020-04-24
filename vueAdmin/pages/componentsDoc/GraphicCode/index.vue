<template lang="pug">
  .content    
    graphic-code(:identifyCode="code", @refresh="refreshCode")
    .mt-15
      basic-table(:tableValue="tableValue", :loading="loading")
    .mt-15
      basic-table(:tableValue="eventTableValue", :loading="loading")
</template>
<script>
import { mapState, mapActions } from 'vuex'
import graphicCode from '@/components/GraphicCode.vue'
import basicTable from '@/components/BasicTable.vue'
export default {
  layout: 'main',
  components: {
    graphicCode,
    basicTable
  },
  data () {
    return {
      code: '',
      loading: false,
      tableValue: {
        page: true,
        tableData: [],
        hasCbx: false,
        tableHead: [{
          lbl: '参数',
          prop: 'params',
          width: '150px'
        }, {
          lbl: '说明',
          prop: 'dec'
        }]
      },
      eventTableValue: {
        page: true,
        tableData: [],
        hasCbx: false,
        tableHead: [{
          lbl: '事件',
          prop: 'event',
          width: '150px'
        }, {
          lbl: '说明',
          prop: 'dec'
        }]
      }
    }
  },
  beforeMount () {
    this.$nextTick(() => {
      this.code = this.getValidateCode()
    })    
  },
  computed: {
    ...mapState({
      currentUser: state => state.userCurrentUser
    })
  },
  mounted () {
    this.setUser(this.currentUser)
    this.$nextTick(() => {
      this.tableValue.tableData = [
        {"params": "identifyCode", "dec": "传入验证码规则 mixin.js中getValidateCode()"},
      ]
      this.eventTableValue.tableData = [
        {"event": "refresh", "dec": "刷新验证码"}
      ]
    })    
  },
  methods: {
    ...mapActions([
      'setUser'
    ]),
    refreshCode () {
      this.code = this.getValidateCode()
    }
  }
}
</script>
