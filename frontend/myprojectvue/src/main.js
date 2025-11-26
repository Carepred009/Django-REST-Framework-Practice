import { createApp } from 'vue'
import App from './App.vue'


//from index.js
import router from "./router"


//from FoodItem.vue
//import FoodItem from './components/FoodItem.vue'



//v-model sample
import Foods from './components/Foods.vue'

//input-field sample
import InputFields from './components/InputFields.vue'



import VForms_sample from './components/VForms_sample.vue' //import the VForms_sample.vue and pass to the object

//import router from './router'



const app = createApp(App)

//pass the data to this
app.component('v-form_sample',  VForms_sample )

//input fields
app.component('input-fields', InputFields )


app.component('food-name', Foods)




app.use(router)

app.mount('#app')
