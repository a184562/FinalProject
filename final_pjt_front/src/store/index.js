import Vue from 'vue'
import Vuex from 'vuex'
import createPersistedState from 'vuex-persistedstate'
import router from '../router'

// Django 서버 요청의 경우 각 페이지에서 관리하지 않고 store에서 관리하도록하여 store에서만 axios 요청이 필요한 작업이 이루어지도록 관리하는 것을 목표
// 다만 데이터를 불러오는 과정에서 현재 로그인한 유저의 선호 장르 데이터가 필요한 경우 해당 페이지에서 처리
// movie_detail도 movie_list의 데이터와 API 요청을 통해 가져오는 Data가 서로 다르므로 따로 호출
import axios from 'axios'
const Django_API_URL = 'http://127.0.0.1:8000'

Vue.use(Vuex)


export default new Vuex.Store({
  // 새로 고침을 해도 로그인 정보가 유지되고 탭을 닫으면 로그인이 풀리도록 사용한 플러그인
  plugins: [
    createPersistedState({
      storage: window.sessionStorage,
    })],
  // axios 작업과 관련된 정보들과 로그인 여부를 state에 저장 
  state: {
    token: null,
    movie_list: [],
    free_articles: [],
    review_articles: [],
    genre_list: null,
    movie_num : 0,
    user_data : null,
    is_loggedin : false,
  },
  // 로그인 여부를 판단하기 위한 getters
  getters: {
    isLogin(state){
      return state.token ? true : false
    }
  },
  mutations: {
    SIGN_UP(state, token) {
      state.token = token
    },
    LOG_IN(state,payload){
      state.token = payload.token
      state.username = payload.username
    },
    // 해당 함수 실행으로 로그인할 수 있게 됨
    GET_USER(state, data) {
      state.user_data = data
    },
    LOG_OUT(state) {
      state.token = null
      state.user_data = null
      sessionStorage.clear()
    },
    GET_MOVIE(state, movie_data) {
      // 영화데이터를 처음 한번만 가져오기 위한 작업 -> 처리하지 않을 시 페이지를 불러올 때마다 movie_list에 무한정으로 집어 넣음
      if(state.movie_num === 0) {
        movie_data.forEach(movies => state.movie_list.push(movies))
        state.movie_num = 1
      }
    },
    GETGENRE(state, data) {
      state.genre_list = data
    },
    GET_ARTICLES(state, articles) {
      state.free_articles = []
      articles.forEach(article => {
        state.free_articles.push(article)
      })
    },
    GET_REVIEW(state, articles) {
      state.review_articles = []
      articles.forEach(article => {
        state.review_articles.push(article)
      })
    },
  },
  actions: {
    getMovie(context) {
      // api 서버에 post요청을 무한정 할 경우 과부하가 걸리므로 최초 한번만 보내도록 설정
      if (context.state.movie_num === 0) {
        context.dispatch('postMovie')
        axios({
          method: 'get',
          url: `${Django_API_URL}/api/v1/movies/`,
        })
        // 영화가 POST되고 바로 불러올 경우 DB에 완전히 저장되기 전에 데이터를 불러오는 경우가 생겨 데이터를 불러오는데 시간차를 둠
        .then((res) => {
          setTimeout(()=> {
            context.commit('GET_MOVIE', res.data)
          }, 10000)
        })
        .catch((err) => console.log(err))
      }
    },
    // Django에 tmdb 사이트로부터 데이터를 받도록 요청
    postMovie() {
      axios({
        method: 'post',
        url: `${Django_API_URL}/api/v1/moviedata/`
      })
      .then((res) => console.log(res))
      .catch((err) => console.log(err))
    },
    // 회원가입시 Django 서버에 양식에 맞춘 데이터를 보내주는 작업
    signUp(context, payload) {
      const username = payload.username
      const password1 = payload.password1
      const password2 = payload.password2
      const email = payload.email
      const firstname = payload.firstname
      const lastname = payload.lastname
      axios({
        method: 'post',
        url: `${Django_API_URL}/accounts/signup/`,
        data: {
          username, password1, password2, email, firstname, lastname
        }
      })
      .then((res) => {
        context.commit('SIGN_UP', res.data.key)
      })
      .catch((err) => console.log(err))
    },
    // login시 필요한 데이터들을 보내주는 작업
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
      .then((res)=>{
        const payload_1 = {
          token : res.data.key,
          username : payload.username
        }
        context.commit('LOG_IN', payload_1)
        context.dispatch('getUser')
      })
      .catch(()=>{
        alert('아이디나 비밀번호가 일치하지 않습니다.')
        router.push({ name: 'login'})
      })
    },
    // 실질적으로 Vue 서버에서 로그인 여부를 판단하도록 하는 작업
    getUser(context) {
      axios({
        method: 'get',
        url: `${Django_API_URL}/accounts/user/`,
        headers: {
          Authorization: `Token ${context.state.token}`
        }
      })
      .then((res) => context.commit('GET_USER', res.data))
      .catch(() => {})
    },
    logout(context) {
      context.commit("LOG_OUT")
    },
    // 게시글을 불러오는 작업들의 경우 lazy loading을 하지 않을 경우 글을 쓴 후 따로 새로고침을 해주어야 글이 불러와지므로 async 처리
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
      .catch(() => {})
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
      .catch(() => {})
    },
    // DB에서 영화의 장르 데이터를 Many To Many로 연결해 주기 위해서는 미리 장르 데이터가 필요함
    // 따라서 서버에서 POST 요청으로 DB에 장르 데이터를 넣어주기 위해 호출하는 함수
    getGenre(context) {
      if (context.state.movie_num === 0) {
        axios({
          method: 'get',
          url: `${Django_API_URL}/api/v1/movie/genres/`,
        })
        .then((res) => {
          context.commit('GETGENRE', res.data)
        })
        .catch(() => {})
      }
    },
  },
  modules: {
  }
})
