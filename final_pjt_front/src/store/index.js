import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'
// import router from '@/router'

const Django_API_URL = 'http://127.0.0.1:8000'

Vue.use(Vuex)

export default new Vuex.Store({
  
  state: {
    token: null,
    movie_list: [],
    free_articles: [],
    review_articles: [],
    genre_list: [],
    movie_num : 0,
    user_id : null,
    username : null,
  },
  getters: {
    isLogin(state){
      return state.token ? true : false
    }
  },
  mutations: {
    SIGN_UP(state, token) {
      state.token = token
    },
    SAVE_TOKEN(state,payload){
      // state.user_id = 
      state.token = payload.token
      state.username = payload.username
      // state.user_id = 
    },
    GET_ARTICLES(state, articles) {
      state.free_articles = articles
    },
    GET_REVIEW(state, articles) {
      state.review_articles = articles
    },
    GET_MOVIE(state, movie_data) {
      if(state.movie_num === 0) {
        movie_data.forEach(movies => state.movie_list.push(movies))
      }
      state.movie_num = 1
    },
    GET_USER(state, data) {
      state.user_id = data.pk
    }
  },
  

  actions: {
    async getMovie(context) {
      await axios({
        method: 'get',
        url: `${Django_API_URL}/api/v1/movies/`,
      })
      .then((res) => {
        console.log(res, context)
        context.commit('GET_MOVIE', res.data)
      })
      .catch((err) => console.log(err))
    },
    signUp(context, payload) {
      const username = payload.username
      const password1 = payload.password1
      const password2 = payload.password2

      axios({
        method: 'post',
        url: `${Django_API_URL}/accounts/signup/`,
        data: {
          username, password1, password2
        }
      })
      .then((res) => {
        context.commit('SIGN_UP', res.data.key)
        // context.commit('SAVE_TOKEN',res.data.key)
      })
      .catch((err) => console.log(err))
    },
    logIn(context,payload){
      const username = payload.username
      const password = payload.password
      axios({
        method:'post',
        url:`${Django_API_URL}/accounts/login/`,
        data:{
          username,password
        }
      })
      .then(res=>{
        console.log(res)
        const payload_1 = {
          token : res.data.key,
          username : payload.username
        
        }
        context.commit('SAVE_TOKEN', payload_1)
        context.dispatch('getUser')
      })
      .catch(err=>console.log(err))
    },
    getUser(context) {
      axios({
        method: 'get',
        url: `${Django_API_URL}/accounts/user/`,
        headers: {
          Authorization: `Token ${context.state.token}`
        }
      })
      .then((res) => context.commit('GET_USER', res.data))
      .catch((err) => console.log(err))
    },
    getArticle(context) {
      axios({
        method: 'get',
        url: `${Django_API_URL}/api/v1/community/free/`,
        headers:{
          Authorization: `Token ${ context.state.token }`
        }
      })
      .then((res) => {
        // console.log(context, res)
        context.commit('GET_ARTICLES', res.data)
      })
      .catch((err) => {
        console.log(err)
      })
    },
    getReview(context) {
      axios({
        method: 'get',
        url: `${Django_API_URL}/api/v1/community/review/`,
        headers:{
          Authorization: `Token ${ context.state.token }`
        }
      })
      .then((res) => {
        console.log(context, res)
        context.commit('GET_REVIEW', res.data)
      })
      .catch((err) => {
        console.log(err)})
    },
  },
  modules: {
  }
})
