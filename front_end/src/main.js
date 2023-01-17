import { createApp } from 'vue'
import App from './App.vue'
import router from './router'

import 'bootstrap/dist/css/bootstrap.min.css'
import './assets/main.css'

import axios from 'axios'

const app = createApp(App)
// 路由
app.use(router)
// 全局配置axios
// axios.defaults.baseURL = 'http://127.0.0.1:5001'
app.config.globalProperties.$http = axios
axios.defaults.headers.post['Content-Type'] = 'application/json'

app.mount('#app')
