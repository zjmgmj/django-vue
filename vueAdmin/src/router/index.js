import Vue from 'vue'
import Router from 'vue-router'

Vue.use(Router)

/* Layout */
import Layout from '@/views/layout/Layout'

/* Router Modules */
// import componentsRouter from './modules/components'
// import chartsRouter from './modules/charts'
// import tableRouter from './modules/table'
// import nestedRouter from './modules/nested'

/** note: Submenu only appear when children.length>=1
 *  detail see  https://panjiachen.github.io/vue-element-admin-site/guide/essentials/router-and-nav.html
 **/

/**
* hidden: true                   if `hidden:true` will not show in the sidebar(default is false)
* alwaysShow: true               if set true, will always show the root menu, whatever its child routes length
*                                if not set alwaysShow, only more than one route under the children
*                                it will becomes nested mode, otherwise not show the root menu
* redirect: noredirect           if `redirect:noredirect` will no redirect in the breadcrumb
* name:'router-name'             the name is used by <keep-alive> (must set!!!)
* meta : {
    roles: ['admin','editor']     will control the page roles (you can set multiple roles)
    title: 'title'               the name show in submenu and breadcrumb (recommend set)
    icon: 'svg-name'             the icon show in the sidebar,
    noCache: true                if true ,the page will no be cached(default is false)
  }
**/
export const constantRouterMap = [
  { path: '/login', component: () => import('@/views/login/index'), hidden: true },
  {
    path: '/',
    component: Layout,
    redirect: '/messageCenter',
    name: '消息中心',
    hidden: false,
    meta: { title: '消息中心', icon: 'example' },
    children: [{
      path: 'messageCenter',
      component: () => import('@/views/messageCenter/index'),
      name: '消息中心',
      meta: { title: '消息中心', icon: 'form', noCache: true }
    }]
  },
  {
    path: '/product',
    component: Layout,
    redirect: '/product/list',
    name: '产品中心',
    hidden: false,
    children: [{
      path: 'productList',
      component: () => import('@/views/product/list'),
      name: '产品列表',
      meta: { title: '产品列表', icon: 'form', noCache: true }
    }, {
      path: 'addProduct',
      hidden: true,
      component: () => import('@/views/product/form'),
      name: '新增产品',
      meta: { title: '新增产品', icon: 'form', noCache: true }
    }]
  }
  // { path: '*', redirect: '/404', hidden: true }
]

export default new Router({
  // mode: 'history', // require service support
  scrollBehavior: () => ({ y: 0 }),
  routes: constantRouterMap
})

export const asyncRouterMap = [{
    path: '/cashier',
    component: Layout,
    redirect: '/CashierManagement/openCard/index',
    name: '收银管理',
    meta: { title: '收银管理', icon: 'example'},
    children: [{
      path: 'openCard',
      component: () => import('@/views/CashierManagement/openCard/index'),
      name: '开卡',
      meta: { title: '开卡', icon: 'edit' }
    }, {
      path: 'consumption',
      component: () => import('@/views/CashierManagement/consumption/index'),
      name: '消费',
      meta: { title: '消费', icon: 'edit' }
    }]
  }]
