<template>
  <div class="login-box">
    <h2>Login</h2>

    <div>
      <label>Username:</label>
      <input v-model="username" type="text" />
    </div>

    <div>
      <label>Password:</label>
      <input v-model="password" type="password" />
    </div>

    <button @click="loginUser">Login</button>

    <p v-if="errorMessage" style="color:red">{{ errorMessage }}</p>
  </div>
</template>

<script>
import api from "../axios"; //axios instance

export default {
  data() {
    return {
      username: "",      //store username from the input field
      password: "",       //store password from the input field
      errorMessage: "",    //show error when the login fails
    };
  },

  methods: {
    async loginUser() {      //this will trigger when you click the button
      try {
        const response = await api.post("/api/token/", {  //connects to the backend
          username: this.username,     //sends username to the backend
          password: this.password,    //sends password to the backend
        });

        // Save access token
        localStorage.setItem("access", response.data.access);
        localStorage.setItem("refresh", response.data.refresh);

        this.$router.push("/dashboard"); // redirect
      } catch (error) {
        this.errorMessage = "Invalid username or password";
      }
    },
  },
};
</script>
