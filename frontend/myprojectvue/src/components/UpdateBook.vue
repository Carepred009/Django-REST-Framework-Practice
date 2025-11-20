<!-- UpdateBook.vue -->
<template>
  <div>
    <h2>Update Book</h2>
    <input v-model="title" placeholder="Title" />
    <input v-model="author" placeholder="Author" />
    <button @click="updateBookPut">Update (PUT)</button>
    <button @click="updateBookPatch">Update (PATCH)</button>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  data() {
    return {
        // We are just using fix id number for now
      bookId: 1,       // Example: updating book with ID 1
      title: '',
      author: '',
    }
  },
  methods: {
   //this are the button in templates
    updateBookPut() {
      axios.put(`http://127.0.0.1:8000/book/${this.bookId}/`, {
        title: this.title,
        author: this.author,
      })
      .then(res => {
        alert('Book updated with PUT!')
        console.log(res.data)
      })
      .catch(err => console.log(err))
    },
    //this are the button in templates
    updateBookPatch() {
      axios.patch(`http://127.0.0.1:8000/book/${this.bookId}/`, {
        title: this.title // only updating the title
      })
      .then(res => {
        alert('Book updated with PATCH!')
        console.log(res.data)
      })
      .catch(err => console.log(err))
    }
  }
}
</script>
