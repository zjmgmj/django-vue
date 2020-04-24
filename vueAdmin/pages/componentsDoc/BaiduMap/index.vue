<template lang="pug">
  .content
    button(@click="mapShow") 地图
    baidu-map(v-if="dialogMap", :baiduMapData= "baiduMapData", :cb="baiduMapCb")
    .mt-15
      basic-table(:tableValue="tableValue", :loading="loading")
</template>
<script>
import { mapState, mapActions } from 'vuex'
import baiduMap from '@/components/BaiduMap.vue'
import basicTable from '@/components/BasicTable.vue'
export default {
  layout: 'main',
  components: {
    baiduMap,
    basicTable
  },
  data () {
    return {
      baiduMapData: {
        center: {lng: 116.404, lat: 39.915},
        zoom: 6,
        location: '中国',
        keyWord: '江苏常州'
      },
      dialogMap: true,
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
  computed: {
    ...mapState({
      currentUser: state => state.userCurrentUser
    })
  },
  mounted () {
    this.setUser(this.currentUser)
    this.$nextTick(() => {
      this.tableValue.tableData = [
        {"params": "dialogMap", "dec": "true: 显示地图， false:不显示"},
        {"params": "baiduMapData", "dec": "参考https://dafrok.github.io/vue-baidu-map/#/"},
        {"params": "cb", "dec": "关闭弹框返回事件"},
      ] 
    })
  },
  methods: {
    ...mapActions([
      'setUser'
    ]),
    mapShow() {
      this.dialogMap = true
    },
    baiduMapCb() {
      this.dialogMap = false
    }
  }
}
</script>

