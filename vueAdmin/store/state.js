export default {
  pageSize: 10,
  // http://wechat.xingyun361.com/
  // 192.168.20.149:8080
  // fileUploadUrl: 'http://wechat.xingyun361.com/quasarserver/file/uedit/upload',
  userCurrentUser: {
    id:1,
    createAt:1544767935000,
    updateAt:1544767935000,
    name:"超级管理员",
    fkDpt:{id:1,createAt:1544767931000,updateAt:1544767931000,name:"电商平台服务部",leader:"曹玉林",status:1,remark:null,
      fkOrg:{id:1,createAt:1544767931000,updateAt:1544767931000,name:"江苏智恒达型云网络科技有限公司",simpleName:"型云",status:1,legalRept:null,remark:null}},
    loginAcct:"admin",
    pwd:"1f82c942befda29b6ed487a51da199f78fce7f05",
    phone:"88888888888",
    status:1,
    fkRole:{id:1,createAt:1544767931000,updateAt:1544767931000,name:"superadmin",auths:[],status:1},
    auths:[],
    dataLevel:"公司",
    sex:1,
    national:null,
    position:null,
    edu:null,
    professional:null,
    email:null,
    jobTitle:null,
    telephone:null,
    addr:null,
    nativePlace:null,
    maritalStatus:null,
    politicalLandscape:null,
    birthday:null,
    inTime:null,
    workGroup:null,
    remark:null,
    avatar:null,
    platformCode:null,
    demission:0,
    loginTime:1556086423969,
    ipAddress:"172.16.120.235"
  },
  qiniuOutlink: 'http://pav6lmvyn.bkt.clouddn.com/',
  bdMapAk: 'IAGOe19VLRpolXruX6o6WGNoSFEP9Gwq',
  fileUploadUrl: '/proxy/fileUpload',
  uploadFileUrl: '/proxy/uploadFile',
  searchParams: {},
  globalSuccessMsg: '',
  globalErrorMsg: '',
  currentPathIdx: '1-1',
  // 客户查询返回数据字段
  // 默认头像
  defaultAvatar: require('../static/defaultAvatar.png'),
  // 数据权限等级
  currentMenus: [],
  allMenus: [{
    title: '钢银',
    iconClass: 'el-icon-menu',
    subItems: [{
      title: 'Banksteel',
      url: '/crawler/banksteel'
    }]
  },{
      title: '组件',
      iconClass: 'el-icon-menu',
      subItems: [{
        title: 'BasicTable',
        url: '/componentsDoc/basicTable'
      }, {
        title: 'SearchForm',
        url: '/componentsDoc/searchForm'
      }, {
        title: 'Breadcrumb',
        url: '/componentsDoc/Breadcrumb'
      }, {
        title: 'ButtonGroup',
        url: '/componentsDoc/ButtonGroup'
      }, {
        title: 'GraphicCode',
        url: '/componentsDoc/GraphicCode'
      }, {
        title: 'BaiduMap',
        url: '/componentsDoc/BaiduMap'
      }, {
        title: 'SimpleUpload',
        url: '/componentsDoc/SimpleUpload'
      }]
  }]
}
