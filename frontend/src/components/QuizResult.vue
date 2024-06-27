<template>
  <div>
    <h2>Quiz Result</h2>
    <p>Your score: {{ store.state.score }}</p>
    <button @click="startNewQuiz">Start New Quiz</button>
    <button @click="viewLeaderboard">View Leaderboard</button>
  </div>
</template>

<script setup>
import { useStore } from 'vuex';
import { useRouter } from 'vue-router';

const store = useStore();
const router = useRouter();

const startNewQuiz = () => {
  router.push('/quiz');
};

const viewLeaderboard = () => {
  router.push('/leaderboards');
};
</script>

<style>
button {
  margin: 5px;
  padding: 10px;
  background-color: #007bff;
  color: white;
  border: none;
  border-radius: 5px;
  cursor: pointer;
}

button:hover {
  background-color: #0056b3;
}
</style>
