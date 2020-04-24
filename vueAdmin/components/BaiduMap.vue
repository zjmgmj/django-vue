<template lang="pug">
el-dialog(title="地图", :visible.sync="dialShow", width="900", @close="cb")
  .ft-16.mb-10 {{baiduMapData.keyWord}}  
    a.text-red.ft-14(:href="search.mapUrl", target="_black") 查看更多地图信息
  baidu-map.baidu-map(:ak="bdMapAk", :center="baiduMapData.center", :zoom="baiduMapData.zoom", :scroll-wheel-zoom="scrollWheelZoom")
    bm-local-search.bm-serch(:location="baiduMapData.location", :keyword= 'baiduMapData.keyWord', :auto-viewport= "search.autoViewport", :panel= "search.panel", @searchcomplete="searchcomplete", :selectFirstResult="search.selectFirstResult")
    bm-navigation(anchor="BMAP_ANCHOR_TOP_RIGHT", :enableGeolocation= "enableGeolocation")
</template>

<script>
  import { mapState } from 'vuex'
  import BaiduMap from 'vue-baidu-map/components/map/Map.vue'
  import BmLocalSearch from 'vue-baidu-map/components/search/LocalSearch.vue'
  import BmNavigation from 'vue-baidu-map/components/controls/Navigation.vue'
  // import BmDriving from 'vue-baidu-map/components/search/Driving.vue'
  export default {
    layout: 'main',
    components: {
      BaiduMap,
      BmLocalSearch,
      BmNavigation
    },
    props: {
      baiduMapData: {
        type: Object,
        required: true
      },
      cb: {
        type: Function,
        required: true
      }
    },
    computed: {
      ...mapState({
        bdMapAk: state => state.bdMapAk
      })
    },
    data () {
      return {
        dialShow: true,
        search: {
          autoViewport: true,
          selectFirstResult: true,
          panel: false,
          mapUrl: ''
        },
        drivingS: {
          autoViewport: true,
          panel: false
        },
        scrollWheelZoom: true,
        enableGeolocation: true,
        baiduMapDataRec: []
      }
    },
    methods: {
      searchcomplete (res) {
        this.search.mapUrl = res.moreResultsUrl
        if(res.Ar.length == 0){
          this.msgShow(this, '抱歉，未找到相关地点')
          return
        }
      }
    }
  }
</script>
<style>
  .baidu-map{
    width: 100%;
    height: 550px;
  }
  .bm-serch{}
</style>