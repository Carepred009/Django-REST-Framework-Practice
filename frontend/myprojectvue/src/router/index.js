//import { createRouter, createWebHistory } from 'vue-router'

//const router = createRouter({
  //history: createWebHistory(import.meta.env.BASE_URL),
  //routes: [],
//})
//export default router

//createRouter → creates the router object.
//createWebHistory → allows pretty URLs (no # hash).
import { createRouter, createWebHistory } from "vue-router";


//When the user visits /, show the Login.vue page.
//When the user visits /dashboard, show the Dashboard.vue page.
import Login from "../views/Login.vue";
import Dashboard from "../views/Dashboard.vue";

const routes = [
  { path: "/", component: Login },
  { path: "/dashboard", component: Dashboard },
];


//Creates the router instance.
//Makes the router available to the entire app.
//Also enables you to use:

//This is how your login page redirects after successful login.
//this.$router.push("/dashboard");
export default createRouter({
  history: createWebHistory(),
  routes,
});
