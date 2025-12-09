
<template>
<div>
    <form @submit.prevent="updateProduct">
        <h1> Update Data with FK</h1>
        <label> Product Name</label>
        <input type="text" v-model="product.name">

          <label> Price</label>
        <input type="number" v-model="product.price">

             <label> Date Created</label>
        <input type="text" v-model="product.created_at">

        <select  v-model="product.category_id" required>
            <option disable value=""> Select Category</option>

            <option v-for="c in categories" :key="c.id" :value="c.id">
                {{c.name}}
            </option>
        </select>


          <label>Description </label>
        <input type="text" v-model="product.description">

        <button type="submit"> Submit</button>

    </form>
</div>
</template>
<script>

import api from "../axios.js";

export default {
  data() {
    return {
      product: {
        name: "",
        price: 0,
        created_at: "",
        description: "",
      },

      categories:[],



    };
  },

  mounted() {
    const productId = this.$route.params.id;   // FIXED
    console.log("ID Received!", productId);
    this.getProduct(productId);                // FIXED

    this.getCategories();
  },

  methods: {
  //for display the data with specific ID
    async getProduct(id) {                      // FIXED (now has parameter)
      try {
        const response = await api.get(`/api/display_update/${id}/`);
        this.product = response.data;          // FIXED (product not products)
      } catch (error) {
        console.error(error);
      }
    },
    //for display the categories
    async getCategories(){
        try{
            const response = await api.get("/api/category_list/")
            this.categories = response.data;
        }catch(error){
            console.error(error)
        }
    },

    //for update the displayed data with specific ID
     async updateProduct(){
        try{
            const productId = this.$route.params.id;
            const response = await api.put(`/api/display_update/${productId}/`, this.product);
            this.product = response.data;
             console.log("Updated!", response.data);
        }catch(error){
            console.error(error)
        }

     },



  },


};

</script>