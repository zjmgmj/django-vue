<template lang="pug">
  div
    el-upload.crm-simple-upload(:action="fileUploadUrl", :before-upload="beforePicUpload",name="upfile", :data="{'action': action}", :on-success="uploadSuccess", :on-progress="uploadProgress", :on-error="uploadError", :file-list="fileList", :disabled="disabled")
      slot
</template>

<script>
  import { mapState } from 'vuex'
  export default {
    props: {
      value: {
        required: true
      },
      action: {
        type: String,
        default: 'avatar'
      },
      type: {
        type: String,
        default: ''
      },
      disabled: {
        type: Boolean,
        default: false
      }
    },
    computed: {
      ...mapState({
        fileUploadUrl: state => state.fileUploadUrl
      })
    },
    data () {
      return {
        fileList: []
      }
    },
    methods: {
      beforePicUpload (file) {
        var imgType = file.type === 'image/png' || file.type === 'image/jpeg'
        var imgSize = file.size / 1000000 <= 2
        if (!imgType) {
          this.$message.error('上传图片格式错误!')
        }
        if (!imgSize) {
          this.$message.error('上传图片大不能超过2M!')
        }
        return imgType && imgSize
      },
      uploadSuccess (resp, file, fileList) {
        this.$emit('input', file.response.url)
        this.$emit('fileObj', file)
        // if(this.type == 'logo') this.fileList[0] = [file]
        console.log(this.fileList)
        this.pageHide()
        this.$message.success('图片上传成功')
      },
      uploadProgress () {
        this.pageShow(this)
      },
      uploadError () {
        this.pageHide()
        this.$message.error('图片上传失败')
      }
    }

  }
</script>

<style lang="stylus" scoped>

</style>
