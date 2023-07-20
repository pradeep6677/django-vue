import { createApp, Vue } from 'vue'
import './index.css'
import App from './App.vue'
import Argon from '@/plugins/argon-kit'
Vue.use(Argon)
// import axios
/* import axios from 'axios'
// set a prototype for http
Vue.prototype.$http = axios; */

createApp(App).mount('#app')
