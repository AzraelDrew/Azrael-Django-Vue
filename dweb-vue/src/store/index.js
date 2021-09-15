import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    userinfo: {}
  },
  mutations: {
    editUserInfo(state, user) {
      state.userinfo = user;
      console.log(state);
    }
  },
  actions: {},
  modules: {}
})