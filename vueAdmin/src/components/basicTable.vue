<template lang="pug">
.content
  el-table(:data="currentData", :row-class-name="tableRowClassName", highlight-current-row,  v-loading="loading", element-loading-text="Loading", fit, border, @selection-change="handleSelectionChange", @current-change="handleCurrentChange", :default-sort="{order: 'descending'}", size="medium", :header-cell-class-name="headerCellClassName", :filter-change="tableFiler", @sort-change="sortChange")
    el-table-column(v-if="tableValue.hasCbx", type="selection", width="55")
    template(v-for="head in tableValue.tableHead")
      el-table-column(v-if="head.type == 'action'", :align="head.align ? head.align : 'left'" :fixed="head.fixed", label="操作", :width="head.width ? head.width : 'auto'", :min-width="head.minWidth? head.minWidth : 'auto'")
        template(slot-scope="scope")
          template(v-for="btn in head.actionBtns")
            el-button(:type="btn.buttonType ? btn.buttonType : 'default'", size="mini", :class="btn.class ? btn.class : 'default'", @click="handerRowBtn(scope.$index, scope.row, btn.type)") {{btn.lbl}}
      el-table-column(v-else,align="center", :label="head.lbl", :width="head.width ? head.width : 'auto'", :min-width="head.minWidth? head.minWidth : 'auto'")
        template(slot-scope="scope")
          span {{scope.row[head.prop]}}
  .padding.text-right
    el-pagination(v-if="!tableValue.page", :current-page="currentPage", :page-size="pageSize", background, layout="prev, pager, next, jumper", :total="total", @current-change="pgCurrentChange")
</template>

<script>
import { mapGetters } from 'vuex'
export default {
  props: {
    tableValue: {
      type: null,
      default: false
    },
    currentPage: {
      type: Number,
      default: 1
    },
    total: {
      type: Number,
      default: 100
    },
    pageSize: {
      type: Number,
      default: 15
    },
    loading: {
      type: Boolean,
      default: true
    },
    lockFun: {
      type: Function,
      require: true
    }
  },
  computed: {
    ...mapGetters([
      'name',
      'roles'
    ])
  },
  data() {
    return {
      currentData: [],
      regionOptions: [],
      supplyCatalogOptions: [],
      comboOptions: [],
      acctOptions: [],
      orgOptions: [],
      isVerify: true
    }
  },
  beforeMount () {
    this.$nextTick(() => {
      this.currentData = Object.assign([], this.tableValue.tableData)
    })
  },
  watch: {
    'tableValue.tableData': {
      handler (newVal, oldVal) {
        this.currentData = Object.assign([], newVal)
      },
      deep: true
    }
  },
  methods: {
    tableRowClassName ({row, rowIndex}) {
      if(this.tableValue.rowClassName){
        console.log(row.billDateDays)
        if (row.billDateDays >= 60) {
          return 'loss-cstm'
        } else if (row.billDateDays > 30 && row.billDateDays < 60) {
          return 'communicate-cstm'
        }
      }
    },
    pgCurrentChange (val) {
      // console.log(val)
      this.$emit('pageChange', val)
    },
    handleSelectionChange (rows) {
      this.$emit('chooseData', rows)
    },
    handleCurrentChange (row) {
      this.$emit('chooseData', row)
    },
    headerCellClassName ({row, column, rowIndex, columnIndex}) {
      let head = this.tableValue.tableHead[columnIndex]
      if (head !== undefined && head.hasOwnProperty('required')) {
        return 'crm-table-required'
      }
    },
    tableFiler (row, col) {},
    sortChange (column, prop, order) {
      // console.log('**********')
      let obj = {
        sortable: column.sortable,
        order: column.order,
        property: column.prop
      }
      this.$emit('sort', obj)
    },
    handerRowBtn (idx, row, btnType) {
      row.idx = idx
      this.isVerify = true
      if (btnType =='save') {
        let lblStr = ''
        for (let key in row){
          if (key == 'name') {
            this.tableValue.tableHead.map(itm => {
              if (itm.prop == 'name') {
                lblStr = itm.lbl
              }
            })
          }
          this.verifyInput(key, row[key], lblStr)
        }
      }
      if (this.isVerify) {
        this.$emit(`tableRow${btnType.substring(0, 1).toUpperCase()}${btnType.substring(1)}`, row)
      }
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
