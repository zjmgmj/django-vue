<template lang="pug">
.app-container
  button-group(:btns="btnGroups", @groupBtnClick="groupBtnClick")
  .mt-15
    basic-table(:tableValue="tableValue", :loading="loading", :currentPage="currentPage", :pageSize="pageSize", :total="totalCount", @pageChange="tableChange", @tableRowDel= "rowDel")
</template>

<script>
import { mapGetters } from 'vuex'
import basicTable from '@/components/basicTable'
import buttonGroup from '@/components/ButtonGroup.vue'

export default {
  components: {
    basicTable,
    buttonGroup
  },
  data() {
    return {
      btnGroups: [{lbl: '新增',  type: 'add'}],
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
            lbl: '删除',
            type: 'delete'
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
      }
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
    groupBtnClick (type) {
      console.log(type)
      this.$router.push({path: '/product/addProduct'})
    },
    rowDel(row) {
      console.log(row)
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