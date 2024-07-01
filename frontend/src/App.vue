<template>
  <div id="app">
    <router-view></router-view>
    <button v-if="currentUser" @click="logout" class="logout-btn mt-4 px-4 py-2 bg-blue-500 text-white rounded-md hover:bg-blue-600 focus:outline-none focus:ring-2 focus:ring-blue-500 focus:ring-opacity-50">Logout</button>
  </div>
</template>

<script setup>
import { computed } from 'vue';
import { useStore } from 'vuex';
import { useRouter } from 'vue-router';

const store = useStore();
const router = useRouter();

const currentUser = computed(() => store.getters.currentUser);

const logout = async () => {
  await store.dispatch('logout');
  router.push('/login');
};
</script>

<style>
.logout-btn {
  position: fixed;
  top: 20px;
  right: 20px;
}
</style>
