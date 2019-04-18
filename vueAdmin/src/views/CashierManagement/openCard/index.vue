<template lang="pug">
.app-container
  el-form(ref="form", :rules="rules", show-message, :model="form", label-width="145px", label-position="right")
    .row
      .col
        el-form-item(label="卡号", prop="cardNo")
          el-input(v-model="form.cardNo")
      .col
        el-form-item(label="跟进员工")
          el-autocomplete.full-width(v-model="form.staffNo", :fetch-suggestions="querySearchAsync", placeholder="请输入内容", @select="handleSelect")
      .col.pl-20(style="padding-top: 3px")
        el-button(type="primary", size="small") 开卡
        el-button(size="small") 收购转卡
    .row.mt-20
      .col.pr-10
        el-card(shadow="hover")
          .mb-5(slot="header")
            span 用户信息
          el-form-item(label="姓名", prop="name")
            el-input(v-model="form.name")
          el-form-item(label="性别")
            el-radio-group(v-model="form.sex")
              el-radio(label= 1) 男
              el-radio(label= 2) 女
          el-form-item(label="手机号码", prop="phone")
            el-input(v-model="form.phone")
          el-form-item(label="生日", prop="phone")
            el-date-picker(v-model="form.birth", type="date", placeholder="请选择生日")
      .col.pl-10
        el-card(shadow="hover")
          .mb-5(slot="header")
            span 会员卡信息
          el-form-item(label="卡折扣")
            el-select(v-model="form.cardDiscount" clearable placeholder="请选择")
              el-option(v-for="item in cardDiscountOptions", :key="item.value", :label="item.label", :value="item.value")
          el-form-item(label="会员级别")
            el-select(v-model="form.cardDiscount" clearable placeholder="请选择")
              el-option(v-for="item in cardDiscountOptions", :key="item.value", :label="item.label", :value="item.value")
          el-form-item(label="已付款")
            el-input(v-model="form.phone")
          el-form-item(label="欠款")
            el-date-picker(v-model="form.birth", type="date", placeholder="请选择生日")
  .row.mt-15
    el-table(border, :data="salesTableValue")
      el-table-column(label="疗程名称")
          el-autocomplete.full-width(v-model="form.staffNo", :fetch-suggestions="querySearchAsync", placeholder="请输入内容", @select="handleSelect")
      el-table-column(label="总金额")
          el-input(v-model="form.phone")
      el-table-column(label="次数")
          el-input(v-model="form.phone")
      el-table-column(label="方式")
          el-autocomplete.full-width(v-model="form.staffNo", :fetch-suggestions="querySearchAsync", placeholder="请输入内容", @select="handleSelect")
      el-table-column(label="成本方式")
          el-autocomplete.full-width(v-model="form.staffNo", :fetch-suggestions="querySearchAsync", placeholder="请输入内容", @select="handleSelect")
      el-table-column(label="扣成本")
          el-input(v-model="form.phone")
      el-table-column(label="备注")
          el-input(v-model="form.phone")
  .row.mt-5
    el-table(border, :data="salesTableValue", show-header=false)
      el-table-column(label="疗程名称")        
      el-table-column(label="总金额")        
      el-table-column(label="次数")       
      el-table-column(label="方式")      
      el-table-column(label="成本方式")      
      el-table-column(label="扣成本")      
      el-table-column(label="备注")      
</template>
<script>
  export default {
    data() {
      return {
        form: {
          cardNo: '',
          staffNo: '',
          name: '',
          sex: 1,
          phone: 15105142952,
          cardDiscount: ''
        },
        timeout: null,
        restaurants: [],
        rules: {
          cardNo: [{ required: true, message: '不能为空', trigger: 'blur' }],
        },
        cardDiscountOptions: [{label: '会员卡', value: '1'},{label: '疗程卡', value: '2'},{label: '金卡', value: '3'},{label: '钻石卡', value: '4'},{label: '银卡', value: '5'}],
        salesTableValue: []
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