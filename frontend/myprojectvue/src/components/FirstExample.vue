<template>
  <div class="box">
    <!-- This is where your HTML UI lives -->
    <h1>{{ message }}</h1>

    <!-- Example of Vue event handling -->
    <button @click="incrementCounter">
      Click Me ({{ counter }})
    </button>
  </div>
</template>

<script>
export default {
  name: "FirstExample",

  // reactive data (Vue tracks changes automatically)
  data() {
    return {
      message: "Hello from your first Vue component!",
      counter: 0,
    };
  },

  // methods contain your functions
  methods: {
    incrementCounter() {
      this.counter++; // adds 1 per click of the button
    },
  },
};
</script>

<style scoped>
/* Style only inside this component */
.box {
  padding: 20px;
  border: 2px solid #4caf50;
  border-radius: 10px;
  width: 300px;
}
</style>
