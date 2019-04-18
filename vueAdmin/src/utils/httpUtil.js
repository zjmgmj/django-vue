import request from '@/utils/request'
import Qs from 'qs'

export function httpPost (urlApi, params) {
  const data = Qs.stringify(params)
  return request({
    url: urlApi,
    method: 'post',
    data
  })
}
