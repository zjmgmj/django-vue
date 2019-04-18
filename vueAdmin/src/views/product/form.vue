<template lang="pug">
.app-container
  el-form(ref="form", :model="form", label-width="80px")
    el-form-item(label="产品名称")
      el-input(v-model="form.name")
    el-form-item(label="原价")
      el-input(v-model="form.basePrice")
    el-form-item(label="优惠价")
      el-input(v-model="form.price")
    el-form-item(label="产品图片")
      el-upload.mt-10(action="https://jsonplaceholder.typicode.com/posts/", list-type="picture-card", :on-preview="handlePictureCardPreview", :on-remove="handleRemove")
        i.el-icon-plus
    el-form-item(label="产品详情")
      tinymce
    el-form-item
      el-button(type="primary", size="small") 确认
      el-button(size="small") 重置
  el-dialog(:visible.sync="dialogVisible")
    img(width="100%", :src="dialogImageUrl", alt="")
</template>

<script>
import Tinymce from '@/components/Tinymce/index'
export default {
  components: {
    Tinymce
  },
  data() {
    return {
      form: {
        name: '',
        category: '',
        basePrice: null,
        price: null,
        imgPath: [],
        content: null
      },
      dialogImageUrl: '',
      dialogVisible: false
    }
  },
  methods: {
    handleRemove(file, fileList) {
      console.log(file, fileList)
    },
    handlePictureCardPreview(file) {
      this.dialogImageUrl = file.url
      this.dialogVisible = true
    }
  }
}
</script>
<style scoped>
  .tinymce-container.editor-container .editor-custom-btn-container{
    line-height: 14px;
  }
</style>
