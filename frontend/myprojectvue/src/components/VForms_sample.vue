<template>
  <div>
    <form @submit.prevent="addItem">
      <h1>Add Item</h1>

      <p>Item name: <input v-model="itemName" /></p>
      <p>Item number: <input v-model="itemNumber" /></p>

      <button type="submit">Add item</button>
    </form>

    <p>Shopping List:</p>
    <ul>
      <li v-for="item in shoppingList" :key="item.name">
        {{ item.name }}, {{ item.number }}
      </li>
    </ul>
  </div>
</template>

<script>
export default {
  data() {
    return {
      itemName: null,
      itemNumber: null,
      shoppingList: [
        { name: 'Tomatoes', number: 5 }
      ]
    }
  },

  methods: {
    addItem() {
      const item = {
        name: this.itemName,
        number: this.itemNumber
      }

      this.shoppingList.push(item)
      this.itemName = null
      this.itemNumber = null
    }
  }
};
</script>
