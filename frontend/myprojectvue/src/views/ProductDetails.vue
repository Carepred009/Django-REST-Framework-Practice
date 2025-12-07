<template>
  <div>
    <h1>Product Details</h1>

    <p><strong>ID:</strong> {{ product.id }}</p>
    <p><strong>Name:</strong> {{ product.name }}</p>
    <p><strong>Price:</strong> {{ product.price }}</p>
     <p><strong>Category:</strong> {{ product.category?.name }}</p>
      <p><strong>Created date:</strong> {{ product.created_at }}</p>
         <p><strong>Description:</strong> {{ product.description }}</p>
  </div>
</template>

<script>
import api from '../axios.js'; //

export default {
  data() {
    return {
      product: {}
    }
  },

  mounted() {
    const productId = this.$route.params.id; // pass the id to the variable
    console.log("ID Received:", this.$route.params.id);
    this.getProduct(productId);
  },

  methods: {
    async getProduct(id) { //accepts the id in the parameter
      try {
        const response = await api.get(`/api/display_update/${id}/`);
        this.product = response.data;  //the value will pass to the product
      } catch (error) {
        console.error(error);
      }
    }
  }
}
</script>
