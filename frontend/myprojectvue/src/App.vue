



<template>
  <div id="app">
    <router-view />

    <!--
             <router-view /> is a built-in placeholder.
            With router (recommended):

        ✔ URL controls which view appears
        ✔ Pages automatically load in <router-view/>
        ✔ Cleaner main.js
        ✔ Organized folder structure
        ✔ Professional app architecture

    -->
  </div>

  <div>
    <h1>
        <v-form_sample/>
    </h1>

  </div>

</template>

<script>

export default {
  name: "App"
};
</script>

<style>
  #app > div {
    border: dashed black 1px;
    display: inline-block;
    width: 120px;
    margin: 10px;
    padding: 10px;
    background-color: lightgreen;
  }
</style>
