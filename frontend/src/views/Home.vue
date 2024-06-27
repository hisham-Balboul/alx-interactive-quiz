<template>
    <div class="home">
      <h1>Welcome to the Quiz App</h1>
      <div v-if="currentUser">
        <p>Hello, {{ currentUser.username }}!</p>
        <button @click="startQuiz">Start a New Quiz</button>
        <button @click="viewLeaderboards">View Leaderboards</button>
      </div>
      <div v-else>
        <p>Please <router-link to="/login">Login</router-link> or <router-link to="/register">Register</router-link> to continue.</p>
      </div>
    </div>
  </template>
  
  <script setup>
  import { computed } from 'vue';
  import { useStore } from 'vuex';
  import { useRouter } from 'vue-router';
  
  const store = useStore();
  const router = useRouter();
  
  const currentUser = computed(() => store.getters.currentUser);
  
  const startQuiz = () => {
    router.push('/quiz');
  };
  
  const viewLeaderboards = () => {
    router.push('/leaderboards');
  };
  </script>
  
  <style>
  .home {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    height: 100vh;
    text-align: center;
  }
  
  button {
    margin: 10px;
    padding: 10px 20px;
    font-size: 16px;
    cursor: pointer;
    border: none;
    border-radius: 5px;
    background-color: #007bff;
    color: white;
    transition: background-color 0.3s ease;
  }
  
  button:hover {
    background-color: #0056b3;
  }
  </style>
  