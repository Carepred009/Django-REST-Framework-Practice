<template>

    <div>
        <h1> Delete the Product </h1>
        <ul>
        <li v-for="product in products" :key="product.id">
            {{product.name}}- {{product.price}}<br>
            {{product.description}} - {{product.created_at}}<br>
            {{product.category?.name}}
            <button @click="deleteProduct(product.id)"> Delete Product</button>
        </li>
        </ul>
    </div>
</template>


<script>

import api from '../axios.js';

export default{
    data(){
        return {
            products:[]
        };
    },

    mounted(){
        this.getProducts();
       // this.deleteProduct();  //this is not included
    },

    methods:{
        async getProducts(){
            const res = await api.get("/product_list/")
                console.log("API DATA",res.data) // show EXACT structure
                 // FIX 1: Assign to products
                 // FIX 2: Use results[] because of DRF pagination
                this.products = res.data.results;  // <-- IMPORTANT!
        },

         async deleteProduct(id) {
      if (!confirm("Are you sure you want to delete this product?")) return;

      // FIX 3: Use backticks for interpolation
      await api.delete(`/api/display_delete/${id}/`); //always put / at the beginning and at the end

      // Remove product from UI instantly
      this.products = this.products.filter(p => p.id !== id);

        }
    }
};

</script>