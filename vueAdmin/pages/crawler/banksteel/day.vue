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
          data: ['今日', '昨日'],
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
          data: []
        },
        yAxis: {
          type: 'value'
        },
        animation: false,
        series: [{
          name: '今日',
          data: [],
          type: 'line'
        }, {
          name: '昨日',
          data: [],
          type: 'line'
        }]
      }
    }
  },
  mounted () {
    let me = this
    me.myChart = echarts.init(document.getElementById('day'))
    me.myChart.setOption(me.option, true)    
    me.params['createTime'] = me.date2Str(new Date())
    me.getOrder()
    setInterval(() => {
      me.getOrder()
    }, 60000)
  },
  methods: {
    async getOrder () {
      try {
        let { data } = await this.apiStreamPost('/proxy/django/post', {url: 'http://172.16.120.235:8081/api/getOrder/', params: this.params})
        console.log('------------')
        console.log(data.list)
        let today = data.list.today
        let lastDay = data.list.lastDay
        let option = this.myChart.getOption()
        let xAxis = []
        let yAxisToday = []
        let yAxislastDay = []
        today.map((item) => {
          xAxis.push(item.time)
          yAxisToday.push(item.weight)
        })
        lastDay.map((item) => {
          yAxislastDay.push(item.weight)
        })
        option.series[0].data = yAxisToday
        option.series[1].data = yAxislastDay
        option.xAxis[0].data = xAxis
        this.myChart.setOption(option)
      } catch (e) {
        console.error(e)
        this.msgShow(this)
      }    
    }
  }
}
</script>

