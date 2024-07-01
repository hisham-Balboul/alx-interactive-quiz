<template>
  <div class="bg-gray-100 min-h-screen flex flex-col justify-center items-center">
    <div class="bg-white shadow-md p-6 mb-6 max-w-md w-full text-center">
      <h2 class="text-2xl font-semibold mb-4">Quiz Result</h2>
      <p class="text-lg mb-4">Your score: {{ store.state.score }}</p>
      <div class="flex justify-center">
        <button @click="startNewQuiz" class="bg-blue-500 text-white px-4 py-2 rounded-md mr-2 hover:bg-blue-600 focus:outline-none focus:ring-2 focus:ring-blue-500 focus:ring-opacity-50">
          Start New Quiz
        </button>
        <button @click="viewLeaderboard" class="bg-blue-500 text-white px-4 py-2 rounded-md hover:bg-blue-600 focus:outline-none focus:ring-2 focus:ring-blue-500 focus:ring-opacity-50">
          View Leaderboard
        </button>
      </div>
    </div>
  </div>
</template>

<script setup>
import { useStore } from 'vuex';
import { useRouter } from 'vue-router';
import axios from 'axios';

const store = useStore();
const router = useRouter();

const username = store.state.user?.username;
const score = store.state.score;
const category = store.state.category; 

const startNewQuiz = () => {
  router.push('/quiz');
};

const viewLeaderboard = () => {
  router.push('/leaderboards');
};

const submitQuizResult = async () => {
  try {
    await axios.post('http://127.0.0.1:5000/api/leaderboard', {
      username,
      score,
      category
    });
  } catch (error) {
    console.error('Failed to submit quiz result:', error);
  }
};

submitQuizResult();
</script>

