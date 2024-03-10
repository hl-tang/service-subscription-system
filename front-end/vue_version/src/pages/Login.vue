<template>
  <div class="min-h-screen flex items-center justify-center bg-gray-200">
    <div class="bg-white p-8 rounded-lg shadow-lg max-w-xl w-full">
      <h2 class="text-2xl font-semibold mb-6">用户登录</h2>
      <form @submit.prevent="login">
        <div class="mb-4">
          <label for="username" class="block text-gray-700 font-medium">用户名</label>
          <input v-model="username" type="text" id="username" name="username" class="mt-1 block w-full rounded border-gray-300 shadow-sm focus:border-primary focus:ring focus:ring-primary focus:ring-opacity-50">
        </div>
        <div class="mb-4">
          <label for="password" class="block text-gray-700 font-medium">密码</label>
          <input v-model="password" type="password" id="password" name="password" class="mt-1 block w-full rounded border-gray-300 shadow-sm focus:border-primary focus:ring focus:ring-primary focus:ring-opacity-50">
        </div>
        <button type="submit" class="bg-primary text-white py-2 px-4 rounded-md hover:bg-primary-dark focus:outline-none focus:ring focus:ring-primary focus:ring-opacity-50 block mx-auto">登录</button>
      </form>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue';

const username = ref('');
const password = ref('');

const login = () => {
  // 在这里实现登录逻辑，可以向后端发送请求验证用户名和密码
  console.log('登录中...');
  console.log('用户名:', username.value);
  console.log('密码:', password.value);
  // 这里可以添加更多的登录逻辑，比如使用axios向后端发送请求验证用户身份
}
</script>

<style>
.focus\:ring-primary-dark:focus {
  --ring-color: #4b5563;
}
</style>
