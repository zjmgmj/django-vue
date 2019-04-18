<template lang="pug">
.app-container
  el-form(ref="form", :rules="rules", show-message, :model="form", label-width="145px", label-position="right")
    .row
      .col
        el-form-item(label="卡号", prop="cardNo")
          el-input(v-model="form.cardNo")
      .col
        el-form-item(label="跟进员工")
          el-autocomplete(v-model="form.staffNo", :fetch-suggestions="querySearchAsync", placeholder="请输入内容", @select="handleSelect")
      .col
        el-button(type="primary", size="small") 开卡
        el-button(size="small") 收购转卡
</template>
<script>
  export default {
    data() {
      return {
        form: {
          cardNo: '',
          staffNo: ''
        },
        timeout: null,
        restaurants: [],
        rules: {
          cardNo: [{ required: true, message: '不能为空', trigger: 'blur' }],
        }
      }
    },
    mounted() {
      this.restaurants = this.loadAll();
    },    
    methods: {
      loadAll() {
        return [
          { "value": "三全鲜食（北新泾店）", "address": "长宁区新渔路144号" },
          { "value": "Hot honey 首尔炸鸡（仙霞路）", "address": "上海市长宁区淞虹路661号" },
          { "value": "新旺角茶餐厅", "address": "上海市普陀区真北路988号创邑金沙谷6号楼113" }
        ];
      },
      querySearchAsync(queryString, cb) {
        var restaurants = this.restaurants;
        var results = queryString ? restaurants.filter(this.createStateFilter(queryString)) : restaurants;
        clearTimeout(this.timeout);
        this.timeout = setTimeout(() => {
          cb(results);
        }, 3000 * Math.random());
      },
      createStateFilter(queryString) {
        return (state) => {
          return (state.value.toLowerCase().indexOf(queryString.toLowerCase()) === 0);
        };
      },
      handleSelect(item) {
        console.log(item);
      }
    }
  }
</script>