<template lang="pug"></template>
<script>
import echarts from 'echarts'
export default {
  layout: 'main',  
  data () {
    return {
      params: {
        createTime: '2019-05-08'
      },
      myChart: '',
      option: {
        legend: {
          data: ['本周', '上周'],
          inactiveColor: '#666',
          textStyle: {
            color: '#666'
          }
        },
        tooltip: {
          trigger: 'axis',
          axisPointer: {
            animation: false,
            type: 'cross',
            lineStyle: {
              color: '#376df4',
              width: 2,
              opacity: 1
            }
          }
        },
        xAxis: {
          type: 'category',
          data: ['周日', '周一', '周二', '周三', '周四', '周五', '周六']
        },
        yAxis: {
          type: 'value'
        },
        animation: false,
        series: [{
          name: '本周',
          data: [],
          type: 'line'
        }, {
          name: '上周',
          data: [],
          type: 'line'
        }]
      }
    }
  },
  mounted () {
    let me = this
    me.myChart = echarts.init(document.getElementById('week'))
    me.myChart.setOption(me.option, true)    
    me.getOrder()
    setInterval(() => {
      me.getOrder()
    }, 60000)
  },
  methods: {
    async getOrder () {
      try {
        let { data } = await this.apiStreamPost('/proxy/django/post', {url: 'http://172.16.120.235:8081/api/getWeekOrder/', params: this.params})
        console.log('------------')
        console.log(data)
        let currentWeek = data.list.currentWeek
        let lastWeek = data.list.lastWeek
        let option = this.myChart.getOption()
        let currentWeight = []
        let lastWeight = []
        for (let i=0; i<7; i++) {
          currentWeight.push(currentWeek[i]['weight'])
          lastWeight.push(lastWeek[i]['weight'])
        }
        option.series[0].data = currentWeight
        option.series[1].data = lastWeight
        this.myChart.setOption(option)
      } catch (e) {
        console.error(e)
        this.msgShow(this)
      }    
    }
  }
}
</script>

