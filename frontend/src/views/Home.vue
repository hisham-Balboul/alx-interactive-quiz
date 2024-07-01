<template>
  <div class="home flex flex-col items-center justify-center h-screen text-center">
    <h1 class="text-4xl font-bold mb-8">Welcome to the Quiz App</h1>
    <div v-if="currentUser">
      <p class="text-3xl mb-4">Hello, {{ currentUser.username }}!</p>
      <button @click="startQuiz" class="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded focus:outline-none focus:shadow-outline mr-4">Start a New Quiz</button>
      <button @click="viewLeaderboards" class="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded focus:outline-none focus:shadow-outline">View Leaderboards</button>
    </div>
    <div v-else>
      <p class="mb-4">Please <router-link to="/login" class="text-blue-500">Login</router-link> or <router-link to="/register" class="text-blue-500">Register</router-link> to continue.</p>
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
  