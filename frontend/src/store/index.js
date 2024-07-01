import { createStore } from 'vuex';
import axios from 'axios';

const store = createStore({
  state: {
    user: null,
    category: null,
    quiz: [],
    currentQuestionIndex: 0,
    score: 0,
  },
  getters: {
    currentUser: (state) => state.user,
    currentCategory: (state) => state.category,
    currentQuestion: (state) => state.quiz[state.currentQuestionIndex],
    isQuizCompleted: (state) => state.currentQuestionIndex >= state.quiz.length,
  },
  mutations: {
    setUser(state, user) {
      state.user = user;
    },
    setCategory(state, categoryName) {
      state.category = categoryName;
    },
    setQuiz(state, quiz) {
      state.quiz = quiz;
      state.currentQuestionIndex = 0; // Reset the question index when a new quiz is set
      state.score = 0; // Reset the score when a new quiz is set
    },
    incrementQuestionIndex(state) {
      state.currentQuestionIndex++;
    },
    incrementScore(state) {
      state.score++;
    },
  },
  actions: {
    async login({ commit }, { username, password }) {
      try {
        await axios.post('http://127.0.0.1:5000/login', { username, password, });
        password = "password";
        commit('setUser', { username, password });
      } catch (error) {
        console.error('Failed to login:', error);
      }
    },
    async logout({ commit }) {
      try {
        await axios.post('http://127.0.0.1:5000/logout');
        commit('setUser', null); // Set the user to null to log out
      } catch (error) {
        console.error('Failed to logout:', error);
      }
    },
    fetchQuiz({ commit }, quiz) {
      commit('setQuiz', quiz);
    },
    fetchCategory({ commit }, categoryName) {
      commit('setCategory', categoryName);
    },
    answerQuestion({ commit, state }, { isCorrect }) {
      if (isCorrect) {
        commit('incrementScore');
      }
        commit('incrementQuestionIndex');
    },
  },
});

export default store;
