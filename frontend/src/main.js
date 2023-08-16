import { createApp } from "vue";
import App from "./App.vue";
import router from "./router";
import store from "./store"; // Vuex Store를 불러옴
import axios from "axios";

axios.defaults.baseURL = "http://127.0.0.1:8000/";

const app = createApp(App);

app.use(router);
app.use(store); // Vuex Store를 앱에 연결

app.mount("#app");
