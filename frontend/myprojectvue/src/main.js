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

//displya product with FK
import Display_Products from './components/Display_products_FK.vue'

//display the update to be updated
//import updateProduct from './components/updateData_FK.vue'


const app = createApp(App)

//display the product to be updated
//app.component('product-update', updateProduct)

//display products with FK
app.component('display-products', Display_Products)

//pass the data to this
app.component('v-form_sample',  VForms_sample )

//input fields
app.component('input-fields', InputFields )


app.component('food-name', Foods)




app.use(router)

app.mount('#app')
