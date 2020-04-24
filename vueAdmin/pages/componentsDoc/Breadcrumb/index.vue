<template lang="pug">
  .content
    breadcrumb(:breadItems="breadItems", :hasBottomLine="hasBottomLine")
    .mt-15
      basic-table(:tableValue="tableValue", :loading="loading")
</template>
<script>
import { mapState, mapActions } from 'vuex'
import breadcrumb from '@/components/Breadcrumb.vue'
import basicTable from '@/components/BasicTable.vue'
export default {
  layout: 'main',
  components: {
    breadcrumb,
    basicTable
  },
  data () {
    return {
      breadItems: ['组件', 'breadcrumb'],
      hasBottomLine: false,
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
      }
    }
  },
  mounted () {
    this.setUser(this.currentUser)
    this.$nextTick(() => {
      this.tableValue.tableData = [
        {"params": "breadItems", "dec": "菜单名称"},
        {"params": "hasBottomLine", "dec": "底部边框是否显示 true:显示， false:不显示"}
      ]
    })    
  },
  computed: {
    ...mapState({
      currentUser: state => state.userCurrentUser
    })
  },
  methods: {
    ...mapActions([
      'setUser'
    ])
  }
}
</script>
