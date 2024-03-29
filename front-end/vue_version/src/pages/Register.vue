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
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue';
import axios from 'axios';
const username = ref('');
const password = ref('');
const confirmPassword = ref('');

const register = async () => {
  if (password.value !== confirmPassword.value) {
    console.error("Passwords don't match");
    return;
  }

  try {
    await axios.post("http://localhost:8000/api/register/", {
      username: username.value,
      password: password.value,
    });
    console.log('Registration successful');
  } catch (error) {
    console.error(error.response.data.message);
  }
};
</script>