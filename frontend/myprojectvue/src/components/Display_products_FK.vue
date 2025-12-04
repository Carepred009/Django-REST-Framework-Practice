<template>
  <div v-for="product in products" :key="product.id">
    <h3>{{ product.name }}</h3>
    <p>Price: {{ product.price }}</p>
    <p>Category: {{ product.category?.name }}</p>
    <p>Description: {{ product.description }}</p>
  </div>
</template>

<script>
import api from "../axios.js";    // <-- update path if needed

export default {
  data() {
    return {
      products: []
    };
  },

  mounted() {
    this.getProducts();
  },

  methods: {
    async getProducts() {
      const res = await api.get('/product_list/');
      console.log(res.data);  // show EXACT structure
      this.products = res.data.results;  // <-- IMPORTANT!
    }
  }
};
</script>
