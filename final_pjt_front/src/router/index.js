import Vue from 'vue'
import VueRouter from 'vue-router'
import MovieListView from '../views/MovieListView.vue'
import CommunityView from '../views/CommunityView.vue'
import EntertainView from '../views/EntertainView.vue'
import MovieDetailView from '../views/MovieDetailView.vue'
import FreeBoard from '../components/Community/FreeBoard.vue'
import MovieReview from '../components/Community/MovieReview.vue'
import LogIn from '../views/Login.vue'
import SignUp from '../views/Signup.vue'
import GamePlay from '../components/Entertain/Game.vue'




Vue.use(VueRouter)

const routes = [
  {
    path: '/movies',
    name: 'movies',
    component: MovieListView
  },
  {
    path: '/community',
    name: 'community',
    component: CommunityView
  },
  {
    path: '/entertain',
    name: 'entertain',
    component: EntertainView
  },
  {
    path: '/movie',
    name: 'movie',
    component: MovieDetailView
  },
  {
    path: '/community/free',
    name: 'free',
    component: FreeBoard
  },
  {
    path: '/community/review',
    name: 'review',
    component: MovieReview
  },
  {
    path: '/login',
    name: 'login',
    component: LogIn
  },
  {
    path: '/signup',
    name: 'signup',
    component: SignUp
  },
  {
    path: '/entertain/game',
    name: 'game',
    component: GamePlay
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
