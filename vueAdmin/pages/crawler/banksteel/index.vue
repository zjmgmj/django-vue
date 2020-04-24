<template lang="pug">
  .content
    el-tabs(type="border-card", v-model="tabName", @tab-click="handleClick")
      el-tab-pane(label="实时", name="day")
        banksteel-day(id="day", :style="{width: '100%', height: '800px'}", v-if="tabName == 'day'")
      el-tab-pane(label="一周", name="week")
        banksteel-week(id="week",:style="{width: '100%', height: '800px'}", v-if="tabName == 'week'")
</template>
<script>
import banksteelDay from '@/pages/crawler/banksteel/day'
import banksteelWeek from '@/pages/crawler/banksteel/week'
import echarts from 'echarts'
export default {
  layout: 'main',  
  data () {
    return {
      tabName: 'day',
      params: {
        createTime: '2019-05-08'
      }
    }
  },
  components: {
    banksteelDay,
    banksteelWeek
  },
  mounted () {},
  methods: {
    handleClick(tab, event) {
      this.tabName = tab.name
    }
  }
}
</script>

