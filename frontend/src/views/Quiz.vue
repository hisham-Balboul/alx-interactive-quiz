<template>
  <div class="flex flex-col items-center justify-center h-screen">
    <h2 class="text-2xl font-bold mb-8">Select Quiz Category</h2>
    <div v-for="(categoryName, categoryId) in categories" :key="categoryId" @click="startQuiz(categoryName)" class="bg-white shadow-md rounded-lg p-4 mb-4 w-full max-w-xs cursor-pointer transform transition duration-300 hover:scale-105">
      <h3 class="text-lg font-semibold">{{ categoryName }}</h3>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import { useStore } from 'vuex';
import { useRouter } from 'vue-router';
import axios from 'axios';

const store = useStore();
const router = useRouter();

const categories = ref([]);

onMounted(async () => {
  try {
    const response = await axios.get('http://127.0.0.1:5000/api/categories');
    categories.value = response.data;
  } catch (error) {
    console.error('Failed to fetch categories:', error);
  }
});

const startQuiz = async (categoryName) => {
  try {
    const response = await axios.get(`http://127.0.0.1:5000/api/questions/${categoryName}`);
    const quiz = response.data;
    store.dispatch('fetchCategory', categoryName);
    store.dispatch('fetchQuiz', quiz);
    router.push('/quiz/game');
  } catch (error) {
    console.error('Failed to fetch questions:', error);
  }
};
</script>
