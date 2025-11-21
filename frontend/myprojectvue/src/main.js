import { createApp } from 'vue'
import App from './App.vue'

//from FoodItem.vue
import FoodItem from './components/FoodItem.vue'

import AddItem from './components/AddItem.vue'

//for PATCH-PUT DRF-Vue-axios
import UpdateBook from './components/UpdateBook.vue'

//for delete PATCH-PUT DRF-Vue-axios
import DeleteItem from './components/DeleteItem.vue'

import router from './router'


const app = createApp(App)

//food-item will be use in the App.vue
app.component('food-item', FoodItem)
app.component('add-item', AddItem)

//for //for delete PATCH-PUT DRF-Vue-axios
app.component('delete-item', DeleteItem)

//for PATCH-PUT DRF-Vue-axios
app.component('update-book',UpdateBook)

app.use(router)

app.mount('#app')
