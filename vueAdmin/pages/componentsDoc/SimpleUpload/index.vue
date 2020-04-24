<template lang="pug">
  .content
    simple-upload(v-model="pic")
      el-button(type="primary", size="medium") 上传图片
</template>
<script>
import { mapState, mapActions } from 'vuex'
import simpleUpload from '@/components/SimpleUpload.vue'
import basicTable from '@/components/BasicTable.vue'
export default {
  layout: 'main',
  components: {    
    simpleUpload
  },
  data () {
    return {
      pic: '',
      loading: false,
      tableValue: {
        page: true,
        tableData: [],
        hasCbx: false,
        tableHead: [{
          lbl: '参数',
          prop: 'params',
          width: '150px'
        }, {
          lbl: '说明',
          prop: 'dec'
        }]
      }
    }
  },
  mounted () {
    this.setUser(this.currentUser)
    this.$nextTick(() => {
      this.tableValue.tableData = [
        {"params": "action", "dec": "文件上传url"},
        {"params": "disabled", "dec": "true | false"},
        {"params": "type", "dec": "标记"}
      ]
    })    
  },
  computed: {
    ...mapState({
      currentUser: state => state.userCurrentUser,
      defaultAvatar: state => state.defaultAvatar
    })
  },
  methods: {
    ...mapActions([
      'setUser'
    ])
  }
}
</script>
