<template>
  <div class="flex flex-col items-center justify-center h-screen">
    <h2 class="text-2xl font-bold mb-4">Login</h2>
    <form @submit.prevent="loginUser" class="bg-white shadow-md rounded px-8 pt-6 pb-8 mb-4 w-full max-w-xs">
      <div class="mb-4">
        <label for="username" class="block text-gray-700 text-sm font-bold mb-2">Username:</label>
        <input id="username" type="text" v-model="username" required class="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline">
      </div>
      <div class="mb-6">
        <label for="password" class="block text-gray-700 text-sm font-bold mb-2">Password:</label>
        <input id="password" type="password" v-model="password" required class="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline">
      </div>
      <button type="submit" class="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded focus:outline-none focus:shadow-outline">
        Login
      </button>
    </form>
    <p class="text-sm">Don't have an account? <router-link to="/register" class="text-blue-500 hover:text-blue-800">Register</router-link>
    </p>
  </div>
</template>
  
  <script setup>
  import { ref } from 'vue';
  import { useStore } from 'vuex';
  import { useRouter } from 'vue-router';
  
  const store = useStore();
  const router = useRouter();
  
  const username = ref('');
  const password = ref('');
  
  const loginUser = async () => {
  const user = {
    username: username.value,
    password: password.value
  };
  await store.dispatch('login',user);
  router.push('/');
};
  </script>
  