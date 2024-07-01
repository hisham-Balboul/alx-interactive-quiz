<template>
  <div class="bg-gray-100 min-h-screen">
    <div class="bg-white shadow-md p-10 mb-4 flex">
      <span class="text-lg font-semibold flex-1">{{ store.getters.currentUser?.username }}'s Turn</span>
      <span class="ml-auto text-3xl font-bold flex-1">{{ countdown }}</span>
    </div>

    <div class="max-w-lg mx-auto p-4">
      <div v-if="!store.getters.isQuizCompleted">
        <h3 class="text-xl font-semibold mb-4">Question {{ store.state.currentQuestionIndex + 1 }} of {{ store.state.quiz.length }}</h3>
        <h4 class="text-lg mb-4">{{ store.getters.currentQuestion.question_text }}</h4>
        <div class="space-y-4">
          <button v-for="(option, index) in store.getters.currentQuestion.options" :key="index"
                  @click="answerQuestion(option)"
                  class="block w-full px-4 py-2 text-white bg-blue-500 rounded-md hover:bg-blue-600 focus:outline-none focus:ring-2 focus:ring-blue-500 focus:ring-opacity-50">
            {{ option }}
          </button>
        </div>
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

  