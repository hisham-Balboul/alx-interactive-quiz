<template>
  <div>
    <h2>Select Quiz Category</h2>
    <div v-for="category in categories" :key="category.id" @click="startQuiz(category)" class="category">
      <h3>{{ category.name }}</h3>
      <p>{{ category.description }}</p>
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

const startQuiz = async (category) => {
  try {
    const response = await axios.get(`http://127.0.0.1:5000/api/questions/${category.id}`);
    const quiz = response.data;
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
