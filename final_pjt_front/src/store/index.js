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
    movie_data: null,
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
    getMovie(context) {
      axios({
        method: 'get',
        url: `${Django_API_URL}/api/v1/movies/`,
      })
      .then((res) => {
        console.log(res, context)
      })
      .catch((err) => console.log(err))
    },
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
    },
    // insertMoviedata(context, movie_data) {
    //   const movie_id = movie_data.id
    //   const title = movie_data.title
    //   const original_title = movie_data.original_title
    //   const poster_path = movie_data.poster_path
    //   const overview = movie_data.overview
    //   const vote_average = movie_data.vote_average
    //   const release_date = movie_data.release_date
    //   const popularity = movie_data.popularity
    //   const genres = movie_data.genre_ids
    //   // const runtime = movie_data.runtime
    //   // console.log(title, original_title, poster_path, overview,
    //   //   vote_average, release_date, popularity)
    //   axios({
    //     method: 'post',
    //     url: `${Django_API_URL}/api/v1/movies/`,
    //     data: {
    //       "pk" : movie_id,
    //       "model" : "Movie.movie",
    //       "fields":{
    //         "title":title,
    //         "original_title":original_title,
    //         "poster_path": poster_path,
    //         "overview": overview,
    //         "vote_average": vote_average,
    //         "release_date": release_date,
    //         "popularity": popularity,
    //         "genres": genres,
    //       }
    //     }
    //   })
    //   .then(() => {
    //     console.log(movie_data)
    //   })
    //   .catch(() => console.log(movie_data))
    // },
    
  },
  modules: {
  }
})
