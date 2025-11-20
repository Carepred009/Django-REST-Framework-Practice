import { createApp } from 'vue'
import App from './App.vue'

//from FoodItem.vue
import FoodItem from './components/FoodItem.vue'
import AddItem from './components/AddItem.vue'

import router from './router'


const app = createApp(App)

//food-item will be use in the App.vue
app.component('food-item', FoodItem)
app.component('add-item', AddItem)

app.use(router)

app.mount('#app')
