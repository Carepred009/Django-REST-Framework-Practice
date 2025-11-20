<template>
  <div>
    <h2>Add New Item</h2>

    <form @submit.prevent="submitItem">
      <input v-model="name" placeholder="Item Name" />
      <textarea v-model="description" placeholder="Description"></textarea>
      <button type="submit">Submit</button>
    </form>

    <p v-if="message">{{ message }}</p>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "AddItem",

  data() {
    return {
      name: "",
      description: "",
      message: ""
    };
  },

  methods: {
    async submitItem() {
      try {
        const response = await axios.post("http://127.0.0.1:8000/api/create_item/", { //line 32
          name: this.name,
          description: this.description
        });

        this.message = "Item created successfully!";
        console.log(response.data);
      } catch (error) {
        this.message = "Error creating item";
        console.log(error.response); //this line 41
      }
    }
  }
};
</script>
