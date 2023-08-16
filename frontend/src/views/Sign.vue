<template>
  <div>
    <form @submit.prevent="submitForm">
      <input v-model="email" type="email" placeholder="Email" />
      <input v-model="username" type="text" placeholder="Username" />
      <input v-model="password1" type="password" placeholder="Password" />
      <input
        v-model="password2"
        type="password"
        placeholder="Confirm Password"
      />
      <button type="submit">Sign Up</button>
    </form>
    <p v-if="showSuccessMessage">{{ successMessage }}</p>
  </div>
</template>

<script>
import axios from "axios";

export default {
  data() {
    return {
      email: "",
      username: "",
      password1: "",
      password2: "",
      showSuccessMessage: false,
      successMessage: "회원가입이 완료되었습니다.",
    };
  },
  methods: {
    submitForm() {
      const userData = {
        email: this.email,
        username: this.username,
        password1: this.password1,
        password2: this.password2,
      };
      axios
        .post("http://localhost:8000/api/accounts/signup/", userData) // 백엔드 서버 도메인과 포트 설정
        .then((response) => {
          console.log("User registered successfully", response.data);
          // Optionally, show a success message or redirect to a new page
          this.showSuccessMessage = true; // Success 메시지 표시
          this.clearForm(); // 폼 초기화
        })
        .catch((error) => {
          console.error("Error during registration", error);
          // Optionally, show an error message to the user
        });
    },
    clearForm() {
      this.email = "";
      this.username = "";
      this.password1 = "";
      this.password2 = "";
    },
  },
};
</script>
