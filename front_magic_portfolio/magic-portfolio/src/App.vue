<template>
  <div>
    <app-header />
    <portfolio-list />
  </div>
</template>

<script>
import AppHeader from '@/components/AppHeader.vue'
import PortfolioList from './components/PortfolioList.vue'

export default {
  name: 'App',
  components: {
    AppHeader,
    PortfolioList
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}
body {
  background-color: #ebecec;
  min-height: 100vh;
}
</style>
