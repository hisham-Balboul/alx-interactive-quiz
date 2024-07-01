<template>
  <div class="flex flex-col items-center justify-center h-screen">
    <h2 class="text-2xl font-bold mb-4">Register</h2>
    <form @submit.prevent="registerUser" class="bg-white shadow-md rounded px-8 pt-6 pb-8 mb-4 w-full max-w-xs">
      <div class="mb-4">
        <label for="first_name" class="block text-gray-700 text-sm font-bold mb-2">First Name:</label>
        <input id="first_name" type="text" v-model="first_name" required class="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline">
      </div>
      <div class="mb-4">
        <label for="last_name" class="block text-gray-700 text-sm font-bold mb-2">Last Name:</label>
        <input id="last_name" type="text" v-model="last_name" required class="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline">
      </div>
      <div class="mb-4">
        <label for="username" class="block text-gray-700 text-sm font-bold mb-2">Username:</label>
        <input id="username" type="text" v-model="username" required class="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline">
      </div>
      <div class="mb-6">
        <label for="password" class="block text-gray-700 text-sm font-bold mb-2">Password:</label>
        <input id="password" type="password" v-model="password" required class="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline">
      </div>
      <button type="submit" class="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded focus:outline-none focus:shadow-outline">
        Register
      </button>
    </form>
    <p class="text-sm">Already have an account? <router-link to="/login" class="text-blue-500 hover:text-blue-800">Login</router-link>
    </p>
  </div>
</template>
  
  <script setup>
  import { ref } from 'vue';
  import { useRouter } from 'vue-router';
  import axios from 'axios';

  const router = useRouter();
  
  const first_name = ref('');
  const last_name = ref('');
  const username = ref('');
  const password = ref('');
  
  const registerUser = async () => {
    const user = {
    username: username.value,
    first_name: first_name.value,
    last_name: last_name.value,
    password: password.value
  };

  try {
    const response = await axios.post('http://127.0.0.1:5000/register', user);
    console.log(response.data);
    router.push('/login');
  } catch (error) {
    console.error('Failed to register user:', error);
  }
};
  </script>
  