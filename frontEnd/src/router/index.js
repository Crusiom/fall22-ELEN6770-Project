import Vue from 'vue'
import VueRouter from 'vue-router'
import Main from '../components/Main'
import Login from '../components/Login'
import Register from '../components/Register'

Vue.use(VueRouter)

const routes = [
  { path: '/login', component: Login },
  { path: '/register', component: Register },
  { path: '/main', component: Main },
  { path: '/', redirect: '/login' }
]

const router = new VueRouter({
  routes
})

export default router
