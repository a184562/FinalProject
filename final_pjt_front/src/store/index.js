import Vue from 'vue'
import Vuex from 'vuex'

import axios from 'axios'
// import router from '@/router'


// const API_KEY = process.env.VUE_APP_MOVIE_API_KEY
// const movie_URL_1 = 'https://api.themoviedb.org/3/movie/'
// const movie_URL_2 = `?api_key=${API_KEY}`

const Django_API_URL = 'http://127.0.0.1:8000'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    free_articles: [],
    review_articles: [],
  },
  getters: {
  },
  mutations: {
    GET_ARTICLES(state, articles) {
      state.free_articles = articles
    },
    GET_REVIEW(state, articles) {
      state.review_articles = articles
    }
  },
  actions: {
    getArticle(context) {
      axios({
        method: 'get',
        url: `${Django_API_URL}/api/v1/community/free/`,
      })
      .then((res) => {
        console.log(context, res)
        context.commit('GET_ARTICLES', res.data)
      })
      .catch((err) => {
        console.log(err)})
    },
    getReview(context) {
      axios({
        method: 'get',
        url: `${Django_API_URL}/api/v1/community/review/`,
      })
      .then((res) => {
        console.log(context, res)
        context.commit('GET_REVIEW', res.data)
      })
      .catch((err) => {
        console.log(err)})
    }
  },
  modules: {
  }
})
