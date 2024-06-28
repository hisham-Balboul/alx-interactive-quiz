<template>
    <div>
      <h2>Login</h2>
      <form @submit.prevent="loginUser">
        <div>
          <label for="username">Username:</label>
          <input type="text" v-model="username" required>
        </div>
        <div>
          <label for="password">Password:</label>
          <input type="password" v-model="password" required>
        </div>
        <button type="submit">Login</button>
      </form>
      <p>Don't have an account? <router-link to="/register">Register</router-link></p>
    </div>
  </template>
  
  <script setup>
  import { ref } from 'vue';
  import { useStore } from 'vuex';
  import { useRouter } from 'vue-router';
  import axios from 'axios';
  
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
  