<template>
  <div>
    <h1>Vue.js + DRF + Axios Example</h1>

    <button @click="getMessage">Load API Message</button>

    <p v-if="apiMessage">
      <strong>Response:</strong> {{ apiMessage }}
    </p>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'App',
  data() {
    return {
      apiMessage: null
    }
  },
  methods: {
    async getMessage() {
      try {
        const response = await axios.get('http://127.0.0.1:8000/api/message/')
        this.apiMessage = response.data.message
      } catch (error) {
        console.error(error)
      }
    }
  }
}
</script>

<style>
h1 {
  color: #42b983;
}
</style>
