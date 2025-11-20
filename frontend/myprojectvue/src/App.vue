<template>
  <div>
    <h1>Vue.js + DRF + Axios Example</h1>

    <button @click="getMessage">Load API Message</button>

    <p v-if="apiMessage">
      <strong>Response:</strong> {{ apiMessage }}
    </p>

  </div>

<!--<food-ite/> is from main.js -->
  <div>
    <h1> Food</h1>
    <food-item/>
    <food-item/>
    <food-item/>

  </div>

  <div>
  <h1> ADD Item</h1>
   <add-item/>

  </div>


<!-- for PATCH-PUT DRF-Vue-axios -->
  <div>
  <h1> Update the book model</h1>
    <update-book/>
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

#app > div {
    border: dashed black 1px;
    display: inline-block;
    margin: 10px;
    padding: 10px;
    background-color: lightgreen;

}

#app > div:hover {
  cursor: pointer;
}


h1 {
  color: #42b983;
}
</style>
