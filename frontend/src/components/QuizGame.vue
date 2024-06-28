<template>
  <div>
    <div class="header">
      <span class="username">{{ store.getters.currentUser.username }}'s Turn</span>
      <span class="timer">{{ countdown }}</span>
    </div>
    <div v-if="!store.getters.isQuizCompleted">
      <h3>Question {{ store.state.currentQuestionIndex + 1 }} of {{ store.state.quiz.length }}</h3>
      <h4>{{ store.getters.currentQuestion.question_text }}</h4>
      <div v-for="(option, index) in store.getters.currentQuestion.options" :key="index">
        <button @click="answerQuestion(option)">{{ option }}</button>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted, onBeforeUnmount } from 'vue';
import { useStore } from 'vuex';
import { useRouter } from 'vue-router';

const store = useStore();
const router = useRouter();
const countdown = ref(20); // 30-second timer for each question

const answerQuestion = (selectedOption) => {
  const currentQuestion = store.getters.currentQuestion;
  const isCorrect = selectedOption === currentQuestion.correct_answer;
  store.dispatch('answerQuestion', { isCorrect });
  if (store.getters.isQuizCompleted) {
    router.push('/quiz/result'); // Navigate to the QuizResult component when the quiz is completed
  } else {
    countdown.value = 20; // Reset timer for next question
  }
};

const logout = () => {
  store.dispatch('login', null);
  router.push('/login');
};

onMounted(() => {
  const interval = setInterval(() => {
    if (countdown.value > 0) {
      countdown.value--;
    } else {
      answerQuestion(null); // Move to next question if time runs out
      countdown.value = 20; // Reset timer for next question
    }
  }, 1000);

  onBeforeUnmount(() => clearInterval(interval)); // Clear the interval when the component is unmounted
});
</script>

  <style>
  .header {
    display: flex;
    justify-content: space-between;
    padding: 10px;
  }
  
  .username, .timer {
    font-size: 1.2em;
  }
  
  .question-info {
    margin: 20px 0;
  }
  
  .options {
    display: flex;
    flex-direction: column;
    gap: 10px;
  }
  
  .option {
    background-color: #007bff;
    color: #fff;
    border: none;
    padding: 10px;
    font-size: 1em;
    border-radius: 5px;
    cursor: pointer;
    transition: background-color 0.3s ease;
  }
  
  .option:hover {
    background-color: #0056b3;
  }
  </style>
  