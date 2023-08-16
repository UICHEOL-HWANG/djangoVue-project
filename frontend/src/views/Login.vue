<template>
  <div>
    <h2>Login</h2>
    <form @submit.prevent="submitForm">
      <input v-model="email" type="email" placeholder="Email" />
      <input v-model="password" type="password" placeholder="Password" />
      <button type="submit">Login</button>
    </form>
    <p v-if="errorMessage">{{ errorMessage }}</p>
  </div>
</template>

<script setup>
import { ref } from "vue";
import axios from "axios";
import { useStore } from "vuex"; // Vuex Store 사용
import { useRouter } from "vue-router";

const email = ref("");
const password = ref("");
const errorMessage = ref(null);
const store = useStore();
const router = useRouter();

const submitForm = () => {
  const userData = {
    email: email.value,
    password: password.value,
  };

  axios
    .post("http://localhost:8000/api/accounts/login/", userData)
    .then((response) => {
      console.log("User logged in successfully", response.data);
      errorMessage.value = null;
      clearForm();
      store.commit("login", response.data.user);
      store.commit("setUser", response.data.user); // 사용자 정보 업데이트
      router.push("/");
    })
    .catch((error) => {
      console.error("Error during login", error);
      errorMessage.value = "로그인 실패. 이메일과 비밀번호를 확인하세요.";
    });
};

const clearForm = () => {
  email.value = "";
  password.value = "";
};
</script>
