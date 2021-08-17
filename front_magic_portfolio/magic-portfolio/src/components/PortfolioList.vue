<template>
    <div id="list">
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
  methods: {
    updatePortfolio () {
      let payload = {
        title: 'foo',
        body: 'bar',
        userId: 1
      };
      axios.put("http://127.0.0.1:5000/magic-portfolio/v1/portfolios/", payload).then((result) => {
        console.log(result);
      });
    }
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