<template>
  <!-- top bar -->
  <div id="TopBar" class="fixed bg-gray-100 w-full border-b h-[60px] flex items-center z-10">
    <router-link to="/" class="ml-2">
      <KeyboardBackspaceIcon :size="35" fillColor="#636363" />
    </router-link>

    <div class="flex-1 text-center text-white"> <!-- flex-1类会使该 div 元素扩展以填充剩余的可用空间，从而将其余内容推到顶部栏的右侧 -->

      <span class="text-teal-500 text-xl">ログイン</span>
    </div>
  </div>

  <!-- topbar下面的东西，为了不被topbar遮住，块内设置与topbar高度相同的上边距-->
  <div class="min-h-[620px] bg-green-50 pt-[60px]"> <!-- 不使用min-h-screen，屏幕下面显示 用户注册 -->
    <div class="mt-10 grid justify-items-center"> <!-- 注意grid justify-items-center, flex这里没用的, text-center也不需要了 -->
      <p class="text-2xl font-thin text-teal-500">会員登録がお済みのお客様</p> <!-- 不知道怎么精细地调日语字体 -->
      <p class="mt-5 max-w-[550px]">登録時に入力されたログインIDとパスワードをご入力の上、「ログイン」ボタンをクリックしてください。 </p> <!-- 不知道怎么精细地调日语字体 -->
    </div>

    <!-- 登录框 -->
    <div class="bg-white p-6 rounded-lg shadow-md max-w-md mx-auto">
      <h2 class="text-2xl font-semibold mb-4">用户名密码登录</h2>

      <!-- <form>
        <div class="mb-4">
          <label for="username" class="block text-sm font-medium text-gray-700">用户名</label>
          <input type="text" id="username" name="username"
            class="mt-1 p-2 block w-full rounded-md border-gray-300 focus:border-teal-500 focus:ring focus:ring-teal-500 focus:ring-opacity-50">
        </div>
        <div class="mb-6">
          <label for="password" class="block text-sm font-medium text-gray-700">密码</label>
          <input type="password" id="password" name="password"
            class="mt-1 p-2 block w-full rounded-md border-gray-300 focus:border-teal-500 focus:ring focus:ring-teal-500 focus:ring-opacity-50">
        </div>
        <div>
          <button type="submit"
            class="w-full bg-teal-500 text-white font-bold py-2 px-4 rounded hover:bg-teal-600 focus:outline-none focus:ring focus:ring-teal-500 focus:ring-opacity-50">登录</button>
        </div>
      </form> -->

      <form @submit.prevent="login" class="bg-white shadow-md rounded px-8 pt-6 pb-8 mb-4">
        <div class="mb-4">
          <label class="block text-gray-700 text-sm font-bold mb-2" for="username">
            Username
          </label>
          <input v-model="username" type="text" id="username"
            class="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
            placeholder="Username" />
        </div>
        <div class="mb-6">
          <label class="block text-gray-700 text-sm font-bold mb-2" for="password">
            Password
          </label>
          <input v-model="password" type="password" id="password"
            class="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
            placeholder="Password" />
        </div>
        <div class="flex items-center justify-between">
          <button type="submit"
            class="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded focus:outline-none focus:shadow-outline">
            Login
          </button>
        </div>
      </form>


    </div>



  </div>

  <!-- 新規ユーザ注册 -->
  <div class="bg-white min-h-[320px] p-6 flex flex-col items-center">
    <p class="text-2xl font-thin text-teal-500 mt-3">会員登録がお済みでないお客様</p>
    <p class="mt-5">まだ会員登録をされていないお客様は、新規で会員登録をし、お申込みください。</p>
    <button class="bg-emerald-300 hover:bg-slate-200 text-white py-2 px-10 rounded-full mt-3">
      <router-link to="/register">
        新規会員登録する
      </router-link>
    </button>
  </div>





</template>

<script setup>
import KeyboardBackspaceIcon from 'vue-material-design-icons/KeyboardBackspace.vue';
import axios from 'axios';

import { ref } from 'vue';

const username = ref('');
const password = ref('');

/* const login = () => {
  // 在这里实现登录逻辑，可以向后端发送请求验证用户名和密码
  console.log('登录中...');
  console.log('用户名:', username.value);
  console.log('密码:', password.value);
  // 这里可以添加更多的登录逻辑，比如使用axios向后端发送请求验证用户身份
} */

const login = async () => {
  console.log('登录中...');
  console.log('用户名:', username.value);
  console.log('密码:', password.value);
  try {
    await axios.post("http://localhost:8000/api/login/", {
      username: username.value,
      password: password.value,
    });
    console.log('Login successful');
  } catch (error) {
    console.error(error.response.data.message);
  }
};


</script>

<style>
.focus\:ring-primary-dark:focus {
  --ring-color: #4b5563;
}
</style>
