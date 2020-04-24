// <template lang="pug">
//   .content
//     .mt-5
//       router-link(to="https://github.com/apertureless/vue-chartjs") 参考 https://github.com/apertureless/vue-chartjs
//     .mt-5
//       router-link(to="https://vue-chartjs.org/") 参考 https://vue-chartjs.org/
//     .mt-5
//       line-chart(:data="saleGoodsChartData", :options="saleGoodsChartOptions", style="width: 100%; height: 600px", ref="goodsLineChart")
// </template>
// <script>
// import { mapState, mapActions } from 'vuex'
// import lineChart from '@/components/LineChart.js'
// import basicTable from '@/components/BasicTable.vue'
// export default {
//   layout: 'main',
//   components: {
//     lineChart
//   },
//   data () {
//     return {
//       saleGoodsChartOptions: {
//         plugins:{
//           customerRating: false
//         },
//         maintainAspectRatio: false,
//         title:{
//           display:false,
//           // position: 'top',
//           // fontSize: 14,
//           // text:'H型钢销售量折线图'
//         },
//         legend: {
//           position: 'bottom'
//         },
//         elements: {
//           line: {
//             tension: 0,
//             fill: false,
//             borderWidth: 2
//           }
//         }
//       },
//       saleGoodsChartData: {
//         labels: ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'],
//         datasets: [{
//           label: "总计",
//           borderColor: '#5b9bd5',
//           data: [40, 30, 22, 59, 18, 60, 50, 80, 60, 50, 30, 84]
//         }, {
//           label: "线上",
//           borderColor: '#ed7d31',
//           data: [10, 10, 10, 29, 8, 20, 20, 50, 10, 30, 15, 24]
//         }, {
//           label: "线下",
//           borderColor: '#a5a5a5',
//           data: [30, 20, 12, 30, 10, 40, 30, 30, 50, 20, 15, 60]
//         }]
//       }
//     }
//   }
// }
// </script>

