<template>
    <div>
     <form @submit.prevent="updateProduct">
     <h1> Update data with FK </h1>
    <label> Name </label>
    <input type="text" v-model="product.name">

     <label> Price </label>
    <input type="number" v-model="product.price">

    <label> Category </label>
    <select v-model="product.category_id">
      <option v-for="cat in categories" :key="cat.id" :value="cat.id">{{cat.name}} </option>

    </select>
     <label> Data Created</label>
    <input type="text" v-model="product.created_at">


     <label> Description</label>
    <input type="text" v-model="product.description">

     <button type="submit"> Update Product</button>
    </form>
    </div>


</template>


<script>

import api from "../axios.js";

export default{
    //
    props: ['productId'], //receives the id from the parent

    data(){
        return {
            product:{
                name:"",
                price:0,
                created_at:"",
                category_id:null,
                description:"",
            },
            categories:{
                id:41 //example ID
            }
        };

    },


    mounted(){
        this.productUpdate();

    },

methods: {
  async productUpdate() {
    const res = await api.get(`/api/display_update/${this.productId}/`);
    console.log("API data", res.data);
    this.product = res.data;
  },
},





};

</script>