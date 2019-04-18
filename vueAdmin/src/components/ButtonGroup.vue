<template lang="pug">
  el-button-group
    template(v-for="(btn,idx) in actionBtns")
      excel-upload.float-left(v-if="btn.type == 'excel'", :dataType="btn.dataType", @uploadSuccess="fileUploadSuccess")
        el-button(size="small") {{btn.lbl}}
      el-button(:type="getBtnClass(btn, idx)", size="small", @click="btnGroupClick(btn.type)", v-else) {{btn.lbl}}
</template>

<script>
  import { mapState } from 'vuex'
  export default {
    props: {
      btns: {
        type: Array,
        required: true
      }
    },
    data () {
      return {
        actionBtns: []
      }
    },
    beforeMount () {
      this.$nextTick(() => {
      	this.actionBtns = this.btns
      })
    },
    methods: {
      btnGroupClick (type) {
        this.$emit('groupBtnClick', type)
      },
      fileUploadSuccess () {
        this.$emit('fileUploadSuccess')
      },
      getBtnClass (btn, idx) {
        if (btn.class) {
          return btn.class
        } else {
          if (idx === 0)
            return 'primary'
          else if (idx === 1)
            return 'success'
          else if (idx === 2)
            return 'danger'
          else
            return 'default'
        }
      }
    }
  }
</script>

<style lang="stylus", scoped>

</style>
