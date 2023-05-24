import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'
import createPersistedState from 'vuex-persistedstate'
// import router from '@/router'

const Django_API_URL = 'http://127.0.0.1:8000'

Vue.use(Vuex)


export default new Vuex.Store({
  plugins:[
    createPersistedState(),
  ],
  state: {
    token: null,
    movie_list: [],
    free_articles: [],
    review_articles: [],
    genre_list: [],
    movie_num : 0,
    user_data : null,
    is_loggedin : false,
  },
  getters: {
    isloggedin(state) {
      return !!state
    },
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
      // state.free_articles = articles
      state.free_articles = []
      articles.forEach(article => {
        
          state.free_articles.push(article)
        })
        
      console.log(state.free_articles, 1234567890)
    },
    GET_REVIEW(state, articles) {
      state.review_articles = []
      articles.forEach(article => {
        state.review_articles.push(article)
      })
    },
    GET_MOVIE(state, movie_data) {
      console.log(movie_data)
      console.log(this.movie_num)
      if(state.movie_num === 0) {
        movie_data.forEach(movies => state.movie_list.push(movies))
        state.movie_num = 1
      }
      
      
    },
    GET_USER(state, data) {
      state.user_data = data
      console.log(data)
      console.log(state.user_data)
    },
    LOG_OUT(state) {
      state.token = null
      state.user_data = null
      localStorage.clear()
    }
  },
  

  actions: {
    async getMovie(context) {
      if (context.state.movie_num === 0) {
        // context.dispatch('postMovie')
        
        await axios({
          method: 'get',
          url: `${Django_API_URL}/api/v1/movies/`,
        })
        .then((res) => {
          console.log(res, context)
          setTimeout(()=> {
            context.commit('GET_MOVIE', res.data)
          }, 10000)
          
        })
        .catch((err) => console.log(err))
         
      }
    },
    postMovie() {
      axios({
        method: 'post',
        url: `${Django_API_URL}/api/v1/moviedata/`
      })
      .then((res) => console.log(res))
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
        console.log(res.data)
        context.commit('SIGN_UP', res.data.key)
        // context.commit('SAVE_TOKEN',res.data.key)
      })
      .then(() => {
        // const payload_1 = {
        //   username, password1
        // }
        context.dispatch('getUser')
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
    logout(context) {
      context.commit("LOG_OUT")
    },
    async getArticle(context) {
      await axios({
        method: 'get',
        url: `${Django_API_URL}/api/v1/community/free/`,
        headers:{
          Authorization: `Token ${ context.state.token }`
        }
      })
      .then((res) => {
        context.commit('GET_ARTICLES', res.data)
      })
      .catch((err) => {
        console.log(err)
      })
    },
    async getReview(context) {
      await axios({
        method: 'get',
        url: `${Django_API_URL}/api/v1/community/review/`,
        headers:{
          Authorization: `Token ${ context.state.token }`
        }
      })
      .then((res) => {
        context.commit('GET_REVIEW', res.data)
      })
      .catch((err) => {
        console.log(err)})
    },
  },
  modules: {
  }
})
