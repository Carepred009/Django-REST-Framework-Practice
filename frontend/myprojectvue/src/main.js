import { createApp } from 'vue'
import App from './App.vue'

//from FoodItem.vue
import FoodItem from './components/FoodItem.vue'

import router from './router'


const app = createApp(App)

//food-item will be use in the App.vue
app.component('food-item', FoodItem)

app.use(router)

app.mount('#app')
