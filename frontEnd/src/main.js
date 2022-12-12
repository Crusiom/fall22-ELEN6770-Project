import Vue from 'vue'
import App from './App.vue'
import router from './router'
import './plugins/element.js'
import axios from 'axios'
import './assets/css/global.css'

Vue.prototype.$axios = axios
Vue.config.productionTip = false
axios.defaults.baseURL = 'https://3uwhn2ro9l.execute-api.us-east-1.amazonaws.com/start-stage/'
new Vue({
  axios,
  router,
  render: h => h(App)
}).$mount('#app')
