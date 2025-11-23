<template>
  <div>
    <h2>Two Inputs + Show on Button Click</h2>

    <label>First Name:</label>
    <input v-model="firstName" type="text" />

    <label>Last Name:</label>
    <input v-model="lastName" type="text" />

    <button @click="showText">Show Output</button>

    <h3 v-if="output">Result:</h3>
    <p>{{ output }}</p>
  </div>
</template>

<script>
export default {

  data() {
    return {
      firstName: "",
      lastName: "",
      output: ""
    };
  },

  methods: {
    showText() {
      this.output = `Hello ${this.firstName} ${this.lastName}!`;
    }
  }
};
</script>
