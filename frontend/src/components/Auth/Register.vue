<template>
    <div>
      <h2>Register</h2>
      <form @submit.prevent="registerUser">
        <div>
        <label for="first_name">First Name:</label>
        <input type="text" v-model="first_name" required>
      </div>
      <div>
        <label for="last_name">Last Name:</label>
        <input type="text" v-model="last_name" required>
      </div>
        <div>
          <label for="username">Username:</label>
          <input type="text" v-model="username" required>
        </div>
        <div>
          <label for="password">Password:</label>
          <input type="password" v-model="password" required>
        </div>
        <button type="submit">Register</button>
      </form>
      <p>Already have an account? <router-link to="/login">Login</router-link></p>
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
  