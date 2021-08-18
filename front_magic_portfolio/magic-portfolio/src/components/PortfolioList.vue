<template>
    <div id="list" class="list-portfolios">
      <div v-bind:key="portfolio" v-for="portfolio in portfolios">
        <portfolio-card :data="portfolio"/>
      </div>
    </div>
</template>

<script>
import axios from "axios"
import PortfolioCard from '../components/PortfolioCard.vue'

export default {
  name: 'PortfolioList',
  components: {
    PortfolioCard
  },
  data () {
    return {
      portfolios: Object
    }
  },
  mounted() {
    axios
      .get('http://127.0.0.1:5000/magic-portfolio/v1/portfolios/')
      .then(response => {
        this.portfolios = response.data.portfolios
      })
      .catch(error => {
        console.log(error)
      })
  }
}
</script>
<style scoped>
  .list-portfolios {
    display: flex;
    flex-wrap: wrap;
    align-content: flex-start;
    list-style: none;
    margin: 0;
    padding: 0;
  }
</style>