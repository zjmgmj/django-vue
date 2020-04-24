<template lang="pug">
.content
  basic-table(:tableValue="tableValue", :loading="loading", @tableRowEdit="rowEdit", @tableRowDelete="rowDel", @chooseData="chooseData", :pageSize="pageSize", :currentPage="currentPage", :total="totalPage", @pageChange="tablePageChange")
  .mt-10
    span 查看代码注释
</template>
<script>
import { mapState, mapActions } from 'vuex'
import basicTable from '@/components/BasicTable.vue'
export default {
  layout: 'main',
  data () {
    return {
      totalPage: 0, //总数
      tableValue: {
        page: false, // false 显示底部翻页, true 不显示
        tableData: [],// table列表数据
        hasCbx: false,// false 不显示选框 true显示选框
        /***********
          tableHead 
            lbl: 头部显示内容 
            prop: 字段名
            width: 宽度
            minWidth: 最小宽度            
            type: 'link' | 'linkObject' | 'linkRow' | 'edit' | 'object'
              object 需配合factValue使用
                factValue(obj){
                  return obj[key]
                }
            linkUrl: url 需配合 type:link | linkObject | linkRow 同时使用
            editType: 'text' | 'date' | 'select' 需配合 type:'edit'同时使用
            action: 操作按钮
              actionBtns
                lbl: 按钮名称
                type: ''  tableRow + type.substring(0,1).toUpperCase()
                  if type: 'edit'
                    return 'tableRowEdit'  // @tableRowEdit=""              
        ************/
        tableHead: [{
          lbl: '事件',
          prop: 'event',
          width: '150px',
          type: 'link',
          linkUrl:'/componentsDoc/basicTable'
        }, {
          lbl: '说明',
          prop: 'dec',
          minWidth: '150px',
          type: 'linkRow',
          linkUrl:'/componentsDoc/basicTable'
        }, {
          lbl: '状态',
          prop: 'status',
          width: '100px',
          type: 'edit',
          editType: 'text'
        }, {
          lbl: '时间',
          prop: 'timeStr',
          width: '150px',
          type: 'edit',
          editType: 'date'
        },{
          lbl: 'type为object',
          prop: 'object',
          width: '150px',
          type: 'object',
          factValue(obj){
            return obj.name
          }
        }, {
          type: 'action',
          width: '100px',
          actionBtns: [{
            lbl: '编辑',
            type: 'edit'
          }, {
            lbl: '删除',
            type: 'delete'
          }]
        }]
      },
      chooseArray: [], // 选中行
      loading: true,
      currentPage: 1 // 当前页
    }
  },
  computed: {
    ...mapState({
      pageSize: state => state.pageSize,
      currentUser: state => state.userCurrentUser
    })
  },
  components: {
    basicTable
  },
  mounted () {
    this.setUser(this.currentUser)
    this.$nextTick(() => {
      this.tableValue.tableData = [
        {'event': 'chooseData', 'dec': '选中 返回object ', 'status': '正常', 'timeStr': '2019-04-24', 'object': {'id': 1, 'name':'名称'}},
        {'event': 'tablePageChange', 'dec': '返回 number', 'status': '正常', 'timeStr': '2019-04-24', 'object': {'id': 1, 'name':'名称'}}        
      ]
      this.totalPage = 12
      this.loading = false
    })    
  },
  methods: {
    ...mapActions([
      'setUser'
    ]),
    chooseData (rows) {
      console.log('-----r')
      console.log(rows)
      this.chooseArray = rows
    },
    tablePageChange (cutPage) {
      console.log('-------------page')
      console.log(cutPage)
      this.currentPage = cutPage
    },
    rowEdit (obj) {},
    rowDel (obj) {
      this.confirmDialog(this, '您确认要删掉本行记录吗？').then(() => {
        console.log('-------del')
      }, () => {
        console.log('cancel')
      })
    }
  }
}
</script>
