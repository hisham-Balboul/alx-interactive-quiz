import { createRouter, createWebHistory } from 'vue-router';
import Home from '@/views/Home.vue';
import Login from '@/components/Auth/Login.vue';
import Register from '@/components/Auth/Register.vue';
import Leaderboards from '@/views/Leaderboards.vue';
import Quiz from '@/views/Quiz.vue';
import QuizGame from '@/components/QuizGame.vue';
import QuizResult from '@/components/QuizResult.vue';

const routes = [
  { path: '/', component: Home },
  { path: '/login', component: Login },
  { path: '/register', component: Register },
  { path: '/leaderboards', component: Leaderboards },
  { path: '/quiz', component: Quiz },
  { path: '/quiz/game', component: QuizGame },
  { path: '/quiz/result', component: QuizResult },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
