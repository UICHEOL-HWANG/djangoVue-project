<script setup>
import Header from "@/components/Header.vue";
import MainVisual from "@/components/MainVisual.vue";
</script>

<template>
  <div id="home" class="home-body">
    <Header />
    <MainVisual />
  </div>
</template>

<style>
body {
  background: url(../assets/img/home_bg.jpg) 0 0 / cover no-repeat;
}
</style>
