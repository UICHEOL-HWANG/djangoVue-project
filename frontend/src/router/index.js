import { createRouter, createWebHistory } from "vue-router";
import Home from "../views/Home.vue";
import Board from "../views/Board.vue";
import Contact from "../views/Contact.vue";
import Map from "../views/Map.vue";
import Sign from "../views/Sign.vue";

const routes = [
  { path: "/", component: Home },
  { path: "/board", component: Board },
  { path: "/contact", component: Contact },
  { path: "/map", component: Map },
  { path: "/sign", component: Sign },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
