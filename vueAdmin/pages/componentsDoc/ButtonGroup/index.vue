<template lang="pug">
  .content
    button-group(:btns="btnGroups", @groupBtnClick="groupBtnClick")
    .mt-15
      basic-table(:tableValue="tableValue", :loading="loading")
      basic-table(:tableValue="eventTableValue", :loading="loading")
</template>
<script>
import { mapState, mapActions } from 'vuex'
import buttonGroup from '@/components/ButtonGroup.vue'
import basicTable from '@/components/BasicTable.vue'
export default {  
  layout: 'main',
  components: {
    buttonGroup,
    basicTable
  },
  data () {
    return {
      btnGroups: [{lbl: '新增', type: 'add'}, {lbl: '删除', type: 'del'}, {lbl: '上传', type: 'excel'}],
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
  mounted () {
    this.setUser(this.currentUser)
    this.$nextTick(() => {
      this.tableValue.tableData = [
        {"params": "btns", "dec": "按钮List， [{lbl: '新增', type: 'add'}, {lbl: '删除', type: 'del'}, {lbl: '上传', type: 'excel'}]"},
        {"params": "lbl", "dec": "按钮名称"},
        {"params": "type", "dec": "按钮标记， type:'excel'上传"}
      ],
      this.eventTableValue.tableData = [
        {"event": "groupBtnClick", "dec": "查询按钮 返回String"}
      ]
    })    
  },
  methods: {
    ...mapActions([
      'setUser'
    ]),
    groupBtnClick (type) {
      console.log('--------buttonGroup')
      console.log('type:' + type)
    }
  },
  computed: {
    ...mapState({
      currentUser: state => state.userCurrentUser
    })
  } 
}
</script>
