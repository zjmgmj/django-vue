import Vue from 'vue'

const formatNumber = (n) => {
  n = n.toString()
  return n[1] ? n : '0' + n
}

 const date2Str = (date) => {
  if (date) {
    let years = date.getFullYear()
    let month = date.getMonth() + 1
    let day = date.getDate()
    return [years, month, day].map(formatNumber).join('-')
  } else {
    return ''
  }
}

const datetime2Str = (date) => {
  if (date) {
    let years = date.getFullYear()
    let month = date.getMonth() + 1
    let day = date.getDate()
    let hours = date.getHours()
    let mins = date.getMinutes()
    let secds = date.getSeconds()
    let dateStr = [years, month, day].map(formatNumber).join('-')
    return dateStr + ' ' + [hours, mins, secds].map(formatNumber).join(':')
  } else {
    return ''
  }
}
const rowData = (value, key) => {
  switch (key) {
    case 'sellHighStatus':
      return value === 1 ? '有' : '无'
    case 'customerType':
      return value === 1 ? '公司客户' : '个人客户'
    case 'status':
      return value === 1 ? '启用' : '停用'
    case 'sex':
      return value === 1 ? '男' : value === 2 ? '女' : ''
    case 'linkDate':
      return date2Str(value)
    case 'updateAt':
    case 'createAt':
    case 'setUpDate':
    case 'planVisitTime':
    case 'delDate':
    case 'time':
    case 'billDate':
    case 'convertDate':
    case 'delayTime':
    case 'replyTime':
    case 'loginDate':
      return (value) ? datetime2Str(new Date(value)) : ''
    default:
      return value
  }
}
Vue.filter('rowData', rowData)
