<template lang="pug">
  .content
    search-form(:searchFormItems="searchFormItems", @search="searchForm")
    .mt-15
      basic-table(:tableValue="tableValue", :loading="loading")
      basic-table(:tableValue="eventTableValue", :loading="loading")
</template>
<script>
import { mapState, mapActions } from 'vuex'
import searchForm from '@/components/SearchForm.vue'
import basicTable from '@/components/BasicTable.vue'
export default {
  layout: 'main',
  components:{
    searchForm,
    basicTable
  },
  data () {
    return {
      searchFormItems: [
        [{label: '商机名称', model: 'opptyName', type: 'text', placeholder: '请输入商机名称', val: ''},          
        {label: '状态', model: 'dptName', type: 'select', placeholder: '请输入提交部门', val: '', list: [{'label': '显示', 'value': 1}, {'label': '不显示', 'value': 0}]},
        {label: '客户得分', model: 'cstmScore', type: 'range', minPlaceholder: '最小值', maxPlaceholder: '最大值', min: '', max: ''}],        
        [{label: '提交日期', model: 'createAt', type: 'date', placeholder: '请选择提交日期', val: ''},
        {label: '提交时间', model: 'createAt', type: 'datetimerange', val: ''},
        {label: '修改日期', model: 'updateAt', type: 'timeLimit', placeholder: '请输入公司名称', val: ''}]
      ],
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
  computed: {
    ...mapState({
      currentUser: state => state.userCurrentUser
    })
  },
  mounted () {
    this.setUser(this.currentUser)
    this.$nextTick(() => {
      this.tableValue.tableData = [
        {"params": "label", "dec": "显示的标题"},
        {"params": "model", "dec": "字段名"},
        {"params": "type", "dec": "输入框类型 'date' | 'timeLimit' | 'datetimerange' | 'select' | 'range'"},
        {"params": "list", "dec": "当使用 select 时需要使用 list: [{'label': '显示的内容', 'value': '值'}, {'label': '显示的内容', 'value': '值'}]"},
        {"params": "min", "dec": "最小值 type 为range时需要使用"},
        {"params": "max", "dec": '最大值 type 为range时需要使用'}
      ]
      this.eventTableValue.tableData = [
        {"event": "searchForm", "dec": "查询按钮 返回object"}
      ]
    })    
  },
  methods: {
    ...mapActions([
      'setUser'
    ]),
    searchForm (paramsObj) {
      console.log('-----------obj')
      console.log(paramsObj)
    }
  }
}
</script>

