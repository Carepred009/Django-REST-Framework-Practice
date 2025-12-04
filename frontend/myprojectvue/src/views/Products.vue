<template>

    <div>
     <!-- Display Products -->
<ul>
  <li v-for="p in products" :key="p.id">
    {{ p.name }} - ₱{{ p.price }}
    (Category: {{ p.category ? p.category.name : "No Category" }})
    - {{ p.description }}
  </li>
</ul>



<hr>

    <form @submit.prevent="createProduct">

    <h1> Create product </h1>
        <label>  Product Name</label>
        <input v-model="newProduct.name" placeholder="Product Name"  required/>

         <label>  Product Price</label>
        <input v-model="newProduct.price" placeholder="Product Price"  required/>

        <select v-model="newProduct.category_id" required>
            <option disabled value=""> Select Category </option>

          <option v-for="c in categories" :key="c.id" :value="c.id">
                {{ c.name }}
          </option>



        </select>

        <label>  Product Description</label>
       <input v-model="newProduct.description" placeholder="Product Description" required/>

        <button type="submit"> Submit Product  </button>
    </form>
    </div>
</template>

<script>
import api from "../axios";

export default{
    data (){
        return{
            products:[],
            categories:[],
            newProduct:{
                name: "",
                price:"",
                category_id: "", //accepts the id
                description:"",
            },
        };
    },

    // use mounted here
    mounted(){
        this.loadCategories();
        this.loadProducts();
    },

    methods:{

        async loadProducts() {
               const res = await api.get("/product_list/");
                this.products = res.data;
        },

        async loadCategories(){
           const res  = await api.get("/api/category_list/") // API endpoint that connects to the backend
            this.categories = res.data;
        },

          async createProduct(){
            try{
                const res =    await api.post("/product_create/", this.newProduct);
                this.newProduct = {name: "", price:"",category:"", description:""}

            }catch(err){
                   console.log(res.data)
            }

            },
      },



};



</script>
