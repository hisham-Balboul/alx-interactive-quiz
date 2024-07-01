<template>
  <div class="bg-gray-100 min-h-screen py-8 px-4">
    <h2 class="text-3xl font-semibold mb-4 text-center">Leaderboards</h2>

    <!-- Home Button -->
    <button @click="goHome" class="home-btn mt-4 px-4 py-2 bg-blue-500 text-white rounded-md hover:bg-blue-600 focus:outline-none focus:ring-2 focus:ring-blue-500 focus:ring-opacity-50">
      Home
    </button>
    <!-- Category Buttons -->
    <div class="flex justify-center space-x-4 mb-4">
      <button v-for="category in categories" :key="category" @click="fetchLeaderboard(category)"
              class="px-4 py-2 bg-blue-500 text-white rounded-md hover:bg-blue-600 focus:outline-none focus:ring-2 focus:ring-blue-500 focus:ring-opacity-50">
        {{ category }}
      </button>
    </div>

    <!-- Leaderboard Table -->
    <table class="w-full bg-white shadow-md rounded-md overflow-hidden">
      <thead class="bg-blue-500 text-black">
        <tr>
          <th class="px-6 py-3 text-center">Username</th>
          <th class="px-6 py-3 text-center">Score</th>
          <th class="px-6 py-3 text-center">Date</th>
        </tr>
      </thead>
      <tbody>
        <tr v-if="leaderboards.length === 0">
          <td colspan="3" class="px-6 py-4 text-center">Select a category to view the leaderboard.</td>
        </tr>
        <tr v-for="entry in leaderboards" :key="entry.id" class="bg-gray-100">
          <td class="px-6 py-4 text-center">{{ entry.username }}</td>
          <td class="px-6 py-4 text-center">{{ entry.score }}</td>
          <td class="px-6 py-4 text-center">{{ entry.date }}</td>
        </tr>
      </tbody>
    </table>

    
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import { useRouter } from 'vue-router';
import axios from 'axios';

const router = useRouter();
const categories = ref([]);
const leaderboards = ref([]);

const fetchCategories = async () => {
  try {
    const response = await axios.get('http://127.0.0.1:5000/api/leaderboard/categories');
    categories.value = response.data;
  } catch (error) {
    console.error('Failed to fetch categories:', error);
  }
};

const fetchLeaderboard = async (category) => {
  try {
    const response = await axios.get(`http://127.0.0.1:5000/api/leaderboard/${category}`);
    leaderboards.value = response.data;
  } catch (error) {
    console.error('Failed to fetch leaderboard:', error);
  }
};

const goHome = () => {
  router.push('/');
};

onMounted(() => {
  fetchCategories();
});
</script>

<style>
.home-btn {
  position: fixed;
  top: 20px;
  left: 20px;
}
.category-btn{
  margin: 5px;
  padding: 10px;
  background-color: #007bff;
  color: white;
  border: none;
  border-radius: 5px;
  cursor: pointer;
}

.category-btn:hover, .home-btn:hover {
  background-color: #0056b3;
}

table {
  width: 100%;
  border-collapse: collapse;
  margin-top: 20px;
}

th, td {
  border: 1px solid #ddd;
  padding: 8px;
}

th {
  background-color: #f2f2f2;
}
</style>