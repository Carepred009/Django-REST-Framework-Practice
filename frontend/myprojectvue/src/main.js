import { createApp } from 'vue'
import App from './App.vue'

//from index.js
import router from "./router"


//from FoodItem.vue
//import FoodItem from './components/FoodItem.vue'

//import AddItem from './components/AddItem.vue'

//for PATCH-PUT DRF-Vue-axios
//import UpdateBook from './components/UpdateBook.vue'

//for delete PATCH-PUT DRF-Vue-axios
//import DeleteItem from './components/DeleteItem.vue'

//v-model sample
import Foods from './components/Foods.vue'

//input-field sample
import InputFields from './components/InputFields.vue'



const app = createApp(App)


//input fields
app.component('input-fields', InputFields )

//food-item will be use in the App.vue
//app.component('food-item', FoodItem)
//app.component('add-item', AddItem)

//v-model sample
app.component('food-name', Foods)



//for //for delete PATCH-PUT DRF-Vue-axios
//app.component('delete-item', DeleteItem)

//for PATCH-PUT DRF-Vue-axios
//app.component('update-book',UpdateBook)

app.use(router)

app.mount('#app')
