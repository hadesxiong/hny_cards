<template>
  <main-view></main-view>
</template>

<script>
import MainView from './view/ MainView.vue';

export default {
  name: 'App',
  components: {
    'main-view': MainView
  }
}
</script>

<style>
@import "tailwindcss";

#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
