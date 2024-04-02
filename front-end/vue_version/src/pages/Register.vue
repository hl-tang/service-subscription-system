<template>
  <div class="flex justify-center items-center h-screen">
    <div class="w-full max-w-xs">
      <form @submit.prevent="register" class="bg-white shadow-md rounded px-8 pt-6 pb-8 mb-4">
        <div class="mb-4">
          <label class="block text-gray-700 text-sm font-bold mb-2" for="username">
            Username
          </label>
          <input v-model="username" type="text" id="username"
            class="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
            placeholder="Username" />
        </div>
        <div class="mb-4">
          <label class="block text-gray-700 text-sm font-bold mb-2" for="password">
            Password
          </label>
          <input v-model="password" type="password" id="password"
            class="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
            placeholder="Password" />
        </div>
        <div class="mb-6">
          <label class="block text-gray-700 text-sm font-bold mb-2" for="confirmPassword">
            Confirm Password
          </label>
          <input v-model="confirmPassword" type="password" id="confirmPassword"
            class="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
            placeholder="Confirm Password" />
        </div>
        <div class="flex items-center justify-between">
          <button type="submit"
            class="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded focus:outline-none focus:shadow-outline">
            Register
          </button>
        </div>
      </form>

      <p>{{ res_data.message }}</p>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue';
import axios from 'axios';
import { routerKey } from 'vue-router';
const username = ref('');
const password = ref('');
const confirmPassword = ref('');

const res_data = ref({});

import { useRoute, useRouter } from "vue-router"
const route = useRoute()
const router = useRouter()

const register = async () => {
  if (password.value !== confirmPassword.value) {
    console.error("Passwords don't match");
    return;
  }

  try {
    await axios.post("http://localhost:8000/api/register/", {
      // request body json的key别忘了"""包む, 但好像没用"username"也对了
      username: username.value,
      password: password.value,
    }).then(res => {
      console.log("Response Data:", res.data);
      // res_data = res.data  一定注意.value
      res_data.value = res.data
      console.log(res_data.value.message)
      if (res_data.value.message === "User created successfully") {
        // router.push("/login")
        // 等待2秒后执行跳转页面的操作
        setTimeout(() => {
          router.push("/login");
        }, 2000);
      }
    });
    // console.log('Registration successful');
  } catch (error) {
    console.error(error.response.data.message);
  }
};
</script>