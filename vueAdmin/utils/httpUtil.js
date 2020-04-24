const axios = require('axios')
const Qs = require('qs')
const sha1 = require('sha1')
module.exports = {
  proxyToken (key) {
    const date = new Date()
    const dateStr = date.getFullYear() + '-' + ((date.getMonth() + 1) > 9 ? (date.getMonth() + 1) : '0' + (date.getMonth() + 1)) + '-' + (date.getDate() > 9 ? date.getDate() : '0' + date.getDate())
    return sha1(dateStr + key)
  },
  httpGet (url) {
    return axios({
      method: 'get',
      url: url,
      headers: {
        'zhdcrm-proxy-token': this.proxyToken('zhdcrm')
      }
    })
  },
  httpPost (url, body) {
    return axios({
      method: 'post',
      url: url,
      params: body,
      headers: {
        'zhdcrm-proxy-token': this.proxyToken('zhdcrm')
      },
      paramsSerializer: (params) => {
        return Qs.stringify(params, {arrayFormat: 'brackets'})
      }
    })
  },
  httpPostForm (url, body) {
    return axios({
      method: 'post',
      url: url,
      params: body,
      headers: {
        'zhdcrm-proxy-token': this.proxyToken('zhdcrm'),
        'Content-Type': 'multipart/form-data'
      },
      paramsSerializer: (params) => {
        return Qs.stringify(params, {arrayFormat: 'brackets'})
      }
    })
  },
  httpDelete (url, body) {
    return axios({
      method: 'delete',
      url: url,
      params: body,
      headers: {
        'zhdcrm-proxy-token': this.proxyToken('zhdcrm')
      },
      paramsSerializer: (params) => {
        return Qs.stringify(params, {arrayFormat: 'brackets'})
      }
    })
  },
  httpStreamPost (url, body) {
    return axios.post(url, body)
  }
}