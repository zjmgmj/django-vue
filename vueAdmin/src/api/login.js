import request from '@/utils/request'
import Qs from 'qs'

export function loginByUsername(username, password) {
  const data = Qs.stringify({
    username,
    password
  })
  return request({
    url: '/api/login',
    method: 'post',
    data
  })
}

export function ajaxPost (urlApi, params) {
  const data = Qs.stringify(params)
  return request({
    url: urlApi,
    method: 'post',
    data
  })
}

export function logout() {
  return request({
    url: '/login/logout',
    method: 'post'
  })
}

export function getUserInfo(token) {
  return request({
    url: '/user/info',
    method: 'get',
    params: { token }
  })
}

