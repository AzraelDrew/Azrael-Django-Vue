import Vue from 'vue'
import VueRouter from 'vue-router'
// import Home from '../views/Home.vue'

Vue.use(VueRouter)

const routes = [{
  path: '/',
  name: 'userlist',
  component: () => import("../views/UserList")
}, ]

const router = new VueRouter({
  routes
})

export default router