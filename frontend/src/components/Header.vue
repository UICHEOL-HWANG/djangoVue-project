<script setup>
// import { headerNav } from "@/constrant/index";
</script>

<template>
  <header id="header">
    <div class="inner">
      <nav>
        <h1 class="logo"><a href="#">Winestagram</a></h1>
        <ul class="gnb">
          <li><router-link to="/" class="nav-link">홈</router-link></li>
          <li>
            <router-link to="/board" class="nav-link">게시판</router-link>
          </li>
          <li><router-link to="/map" class="nav-link">와인맵</router-link></li>
          <li>
            <router-link to="/contact" class="nav-link">컨택트</router-link>
          </li>
        </ul>
        <div class="utll-menu">
          <router-link to="/sign" class="sign-link">
            <i class="ri-user-line"></i>
            <i class="hidden">로그인</i></router-link
          >
        </div>
      </nav>
    </div>
  </header>
</template>

<style lang="scss">
@import "@/assets/scss/reset";
@import url("https://fonts.googleapis.com/css2?family=Yellowtail&display=swap");

.inner {
  width: 1344px;
  height: 100%;
  margin: 0 auto;
}

.inner nav {
  display: flex;
  justify-content: space-between;
  align-items: center;
  height: 95px;
}
.logo {
  display: block;
  cursor: pointer;
}
.logo a {
  text-decoration: none;
  font-family: "Yellowtail", cursive;

  color: darkblue;
  font-weight: 700;
}

.logo a:hover {
  color: brown;
  cursor: pointer;
}

.gnb {
  display: flex;
  margin-right: 150px;
  gap: 10px;
}
.gnb li {
  padding: 10px 30px;
  display: block;
  font-weight: 300;
  font-size: 20px;
  font-family: "Pretendard";
  color: darkblue;
}
li:hover {
  color: brown;
  cursor: pointer;
  background: #fff0f5;
  border-radius: 5px;
}
.utll-menu {
  width: 30px;
  height: 30px;
  border-radius: 50%;
  border: 1px solid darkblue;

  display: flex;
  align-items: center;
  justify-content: center;
  color: darkblue;
  cursor: pointer;
}

.utll-menu:hover {
  color: brown;
  border: 1px solid brown;
}
.logo::before {
  display: flex;
  align-items: center;
  justify-content: center;
  content: "";
  position: absolute;
  mix-blend-mode: multiply;
  background: url(../assets/img/wine1.png) 0 0 / cover no-repeat;
  border-radius: 40px;
  top: 30px;
  left: 250px;
  width: 40px;
  height: 40px;
}
.nav-link {
  text-decoration: none;
}
</style>
