<template lang="pug">
  .app-container    
    el-tabs(type="border-card", show-header=false)
      el-tab-pane(label="未阅读")
        basic-table(:tableValue="tableValue", :loading="loading", :currentPage="currentPage", :pageSize="pageSize", :total="totalCount", @pageChange="tableChange", @tableRowDetail = "rowDetail", @tableRowDel = "rowDel")
      el-tab-pane(label="已阅读")
        basic-table(:tableValue="tableValue", :loading="loading", :currentPage="currentPage", :pageSize="pageSize", :total="totalCount", @pageChange="tableChange")
    el-dialog(:visible="dialogShow", @close="closeDetail", title="详情")
      .ft-18 标题
      .ft-14.mt-10
        span 测试
        span.pl-15 测试部门
        span.pl-15 2018-12-05
      .content.mt-15
        span 发布内容
</template>

<script>
import { mapGetters } from 'vuex'
import basicTable from '@/components/basicTable'

export default {
  components: {
    basicTable
  },
  data() {
    return {
      tableValue: {
        tableHead: [{
          lbl: '发布人',
          prop: 'name',
          width: 200
        }, {
          lbl: '发布部门',
          prop: 'dept',
          width: 200
        }, {
          lbl: '发布时间',
          prop: 'time',
          width: 200
        }, {
          lbl: '发布内容',
          prop: 'content'
        }, {
          type: 'action',
          width: '150px',
          fixed: 'right',
          actionBtns: [{
            lbl: '详情',
            buttonType: 'primary',
            type: 'detail'
          }, {
            lbl: '删除',
            type: 'del'
          }]
        }],
        hasCbx: false,
        tableData: []
      },
      currentPage: 1,
      totalCount: 0,
      pageSize: 10,
      loading: false,
      queryObject: {
        currentPage: this.currentPage - 1,
        pageSize: 10
      },
      dialogShow: false
    }
  },
  computed: {
    ...mapGetters([
      'name',
      'roles'
    ])
  },
  mounted() {
    this.tableValue.tableData = [{ name: 'zhjm', dept: '测试部门', time: '2018-11-23', content: '测试内容' }, { name: 'zhjm', dept: '测试部门', time: '2018-11-23', content: '测试内容' }]
  },
  methods: {
    tableChange(val) {
      // this.loading = true
      // this.currentPage = val
      // this.queryObject.currentPage = this.currentPage - 1
      // this.loadData()
    },
    rowDetail(row) {
      console.log(row)
      this.dialogShow = true
    },
    rowDel(row) {
      this.confirmDialog(this, '您确认要删除？').then(() => {
        console.log('-----------')
        console.log(row)
      }, () => {
        console.log('cancel')
      })   
    },
    closeDetail() {
      this.dialogShow = false
    }
  }
}
</script>

<style rel="stylesheet/scss" lang="scss" scoped>
.dashboard {
  &-container {
    margin: 30px;
  }
  &-text {
    font-size: 30px;
    line-height: 46px;
  }
}
</style>
