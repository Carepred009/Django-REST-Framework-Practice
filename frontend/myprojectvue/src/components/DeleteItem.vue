<template>
  <div>
    <button @click="deleteItem(4)">Delete Item 4</button>
  </div>
</template>

<script>
import axios from "axios";

export default {
  methods: {
    deleteItem(id) {
      axios
        .delete(`http://localhost:8000/item-delete/${id}/`)
        .then((response) => {
          console.log("Deleted successfully:", response);
          alert("Item deleted!");
        })
        .catch((error) => {
          console.error("Delete error:", error);
        });
    },
  },
};
</script>
