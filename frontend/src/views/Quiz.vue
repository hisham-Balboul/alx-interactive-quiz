<template>
  <div>
    <h2>Select Quiz Category</h2>
    <div v-for="(categoryName, categoryId) in categories" :key="categoryId" @click="startQuiz(categoryName)" class="category">
      <h3>{{ categoryName }}</h3>
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
    console.log(quiz);
    store.dispatch('fetchQuiz', quiz);
    router.push('/quiz/game');
  } catch (error) {
    console.error('Failed to fetch questions:', error);
  }
};
</script>

<style>
.category {
  border: 1px solid #ddd;
  padding: 10px;
  margin: 10px 0;
  cursor: pointer;
}
</style>
