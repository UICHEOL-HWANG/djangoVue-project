import { createStore } from "vuex";

// Vuex 스토어 생성
const store = createStore({
  state() {
    return {
      loggedIn: false, // 로그인 상태 여부를 저장하는 상태 변수
      user: null, // 로그인된 사용자 정보를 저장하는 상태 변수
    };
  },
  mutations: {
    // 로그인 처리를 위한 뮤테이션
    login(state, user) {
      state.loggedIn = true; // 로그인 상태를 true로 변경
      state.user = user; // 로그인된 사용자 정보 저장
    },
    // 로그아웃 처리를 위한 뮤테이션
    logout(state) {
      state.loggedIn = false; // 로그인 상태를 false로 변경
    },
    clearUser(state) {
      state.user = null;
    },
    // 사용자 정보 업데이트를 위한 뮤테이션
    setUser(state, user) {
      state.user = user; // 사용자 정보 업데이트
    },
  },
});

export default store;
