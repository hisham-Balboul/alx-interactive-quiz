<template>
    <div>
      <h2>Leaderboards</h2>
      <table>
        <thead>
          <tr>
            <th>Username</th>
            <th>Score</th>
            <th>Date</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="entry in leaderboards" :key="entry.username">
            <td>{{ entry.username }}</td>
            <td>{{ entry.score }}</td>
            <td>{{ entry.date }}</td>
          </tr>
        </tbody>
      </table>
    </div>
  </template>
  
  <script setup>
  import { ref } from 'vue';
  const leaderboards = ref([
    { username: 'User1', score: 95, date: '2024-06-19' },
    { username: 'User2', score: 89, date: '2024-06-18' },
    // Add more entries here
  ]);
  </script>
  