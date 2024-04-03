<script setup>
import { ref } from 'vue';
import axios from 'axios';

const username = ref("");
username.value = $cookies.get("username")
console.log(username.value);
console.log($cookies.get("cookie"));

const logout = async () => {
  axios.get('http://localhost:8000/api/auth_logout/')
    .then(res => {
      console.log("Response Data:", res.data);
      username.value = $cookies.get("username");
      console.log("登出后 " + username.value);
    })
  // 注意axios异步操作，这样username不会等后端清除session,cookie，直接还是赋值为了当前的username
  // username = $cookies.get("username"); //要么这里赋值成null也是可以的
  // console.log("登出后 " + username);
};
console.log("最后 " +username); //也是先于axios执行
</script>

<template>
  <p v-if="!username" class="text-3xl font-bold underline">你好，游客</p>
  <p v-else class="text-3xl font-bold underline">ようこそ，{{ username }}</p>

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
