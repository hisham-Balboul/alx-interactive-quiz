import { createStore } from 'vuex';

const store = createStore({
  state: {
    user: null,
    quiz: [],
    currentQuestionIndex: 0,
    score: 0,
  },
  getters: {
    currentUser: (state) => state.user,
    currentQuestion: (state) => state.quiz[state.currentQuestionIndex],
    isQuizCompleted: (state) => state.currentQuestionIndex >= state.quiz.length,
  },
  mutations: {
    setUser(state, user) {
      state.user = user;
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
    login({ commit }, user) {
      commit('setUser', user);
    },
    logout({ commit }) {
      commit('setUser', null); // Set the user to null to log out
    },
    fetchQuiz({ commit }, quiz) {
      commit('setQuiz', quiz);
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
