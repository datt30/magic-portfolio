<template>
    <div class="card">
      <div class="portfolio-container">
        <div class="img">
            <img :src="data.imageUrl">
        </div>
        <div class="infos">
          <div class="name">
              <h1>{{ data.names }} {{ data.lastNames }}</h1>
              <h4>@{{ data.twitterUser }}</h4>
          </div>
          <h3>{{ data.title }}</h3>
          <p class="text">
              {{ data.description }}
          </p>
        </div>
      </div>
      <div v-if="tweets.length" class="tweets-container">
        <div v-bind:key="tweet" v-for="tweet in tweets">
          <div class="tweet-card">
            <img src="@/assets/tweet_icon.png">
            <p class="text">
                {{ tweet }}
            </p>
          </div>
        </div>
      </div>
      <div class="options-container">
        <button class="edit" @click="showModal">Edit Portfolio</button>
      </div>
      <div class="modal-update">
        <modal-update-portfolio
          v-show="isModalVisible"
          @close="closeModal"
          @update="updatePortfolioData"
        >
          <template v-slot:header>
            Change the {{ data.names }} portfolio data!
          </template>
          <template v-slot:body>
            <input v-model="names" :placeholder="data.names">
            <input v-model="lastNames" :placeholder="data.lastNames">
            <input v-model="twitterUser" :placeholder="data.twitterUser">
            <input v-model="title" :placeholder="data.title">
            <input v-model="description" :placeholder="data.description">
            <input v-model="imageUrl" :placeholder="data.imageUrl">
          </template>
        </modal-update-portfolio>
      </div>
    </div>
</template>

<script>
import axios from "axios"
import ModalUpdatePortfolio from "../components/ModalUpdatePortfolio";

export default {
  name: 'PortfolioCard',
  components: {
    ModalUpdatePortfolio
  },
  props: {
    data: {
        type: Object,
        default: () => ({})
    }
  },
  methods: {
    getUserImg(data) {
        return ((data.imageUrl) ? data.imageUrl : '@/assets/user.png')
    },
    showModal() {
        this.isModalVisible = true;
    },
    closeModal() {
      this.isModalVisible = false;
    },
    updatePortfolioData() {
      let payload = {
        description: this.description,
        imageUrl: this.imageUrl,
        lastNames: this.lastNames,
        names: this.names,
        title: this.title,
        twitterUser: this.twitterUser
      };
      axios.put(`http://127.0.0.1:5000/magic-portfolio/v1/portfolio/${ this.data.idPortfolio }`, payload).then((result) => {
        console.log(result);
        this.isModalVisible = false;
      });
    }
  },
  data () {
    return {
      tweets: [],
      isModalVisible: false,
      description: '',
      imageUrl: '',
      lastNames: '',
      names: '',
      title: '',
      twitterUser: ''
    }
  },
  mounted() {
    axios
      .get(`http://127.0.0.1:5000/magic-portfolio/v1/tweets/${ this.data.twitterUser }`)
      .then(response => {
        this.tweets = response.data.tweets
      })
      .catch(error => {
        console.log(error)
      })
  }
}
</script>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@100;300;700&display=swap');

* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

input {
  height: 30px;
  width: 80%;
  border-radius: 10px;
  margin-top: 8px;
  margin-bottom: 8px;
}

.modal-update {
  z-index: 100;
}

img {
  width: 140px;
  height: 140px;
  display: block;
}
ul {
  list-style: none;
}

.card::after,
.card img {
  width: 140px;
  height: 140px;
  border-radius: 50%;
}

.tweet-card,
.portfolio-container {
  display: flex;
}

.tweets-container {
  margin-top: 10px;
}

.options-container {
  display: flex;
  justify-content: flex-end;
  width: 100%;
}

.card {
  padding: 2.5rem 2rem;
  border-radius: 10px;
  background-color: rgba(255, 255, 255, .5);
  max-width: 500px;
  box-shadow: 0 0 30px rgba(0, 0, 0, .15);
  margin: 1rem;
  position: relative;
  transform-style: preserve-3d;
  overflow: hidden;
}
.card::before,
.card::after {
  content: '';
  position: absolute;
  z-index: -1;
}
.card::before {
  width: 100%;
  height: 100%;
  border: 1px solid #FFF;
  border-radius: 10px;
  top: -.7rem;
  left: -.7rem;
}
.card::after {
  height: 15rem;
  width: 15rem;
  background-color: #1da1f2;
  top: -8rem;
  right: -8rem;
  box-shadow: 2rem 6rem 0 -3rem #FFF
}

.card img {
  width: 140px;
  height: 140px;
}

.tweet-card img {
  padding-top: 10px;
  width: 50px;
  height: 50px;
}

.infos {
  margin-left: 1.5rem;
  text-align: justify;  
  text-justify: auto;
}

.name {
  margin-bottom: 1rem;
}
.name h2 {
  font-size: 1.3rem;
}
.name h4 {
  font-size: .8rem;
  color: #333
}

.text {
  font-size: .9rem;
  margin-top: 1rem;
  margin-bottom: 1rem;
  text-align: justify;  
  text-justify: auto;
}

.tweet-img {
  max-width: 20px;
  max-height: 20px;
}

.options-container button {
  font-family: 'Poppins', sans-serif;
  min-width: 120px;
  padding: .5rem;
  border: 1px solid #222;
  border-radius: 5px;
  font-weight: bold;
  cursor: pointer;
  transition: all .25s linear;
}
.options-container .follow,
.options-container .edit:hover {
  background-color: #222;
  color: #FFF;
}
.options-container .edit,
.options-container .follow:hover{
  background-color: transparent;
  color: #222;
}

@media screen and (max-width: 450px) {
  .card {
    display: block;
  }
  .infos {
    margin-left: 0;
    margin-top: 1.5rem;
  }
  .options-container button {
    min-width: 100px;
  }
}
</style>