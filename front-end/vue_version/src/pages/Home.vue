<script setup>
import axios from 'axios';

const username = $cookies.get("info");
console.log(username);

const logout = async () => {
  axios.get('http://localhost:8000/api/auth_logout/')
  .then(res => {
    console.log("Response Data:", res.data);
  })
};
</script>

<template>
  <p class="text-3xl font-bold underline">我是home</p>

  <div class="m-2 p-2">
    <router-link to="/login">
      <v-btn class="me-2 text-none" color="#ffd900" prepend-icon="mdi-export-variant" variant="flat">
        login
      </v-btn>
    </router-link>
  </div>

  <div class="m-2 p-2">
    <v-btn @click="logout" class="me-2 text-none" color="#ffd900" prepend-icon="mdi-export-variant" variant="flat">
      logout
    </v-btn>
  </div>


</template>

<style scoped></style>
