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
import FreeBoardDetail from '../components/Community/FreeBoardDetail.vue'
import MovieReviewDetail from '../components/Community/MovieReviewDetail.vue'
import GenreSelectView from '../views/GenreSelectView.vue'
import FreeBoardCreate from  '../components/Community/FreeBoardCreate.vue'
import MovieReviewCreate from '../components/Community/MovieReviewCreate.vue'




Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'movies',
    component: MovieListView
  },
  {
    path: '/movie',
    name: 'movie',
    component: MovieDetailView
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
    path: '/community/free',
    name: 'free',
    component: FreeBoard
  },
  {
    path: '/community/free/:id',
    name: 'freeboarddetail',
    component: FreeBoardDetail
  },
  {
    path: '/community/free/create',
    name: 'freecreate',
    component: FreeBoardCreate
  },
  {
    path: '/community/review',
    name: 'review',
    component: MovieReview
  },
  {
    path: '/community/review/:id',
    name: 'reviewdetail',
    component: MovieReviewDetail
  },
  {
    path: '/community/review/create',
    name: 'reviewcreate',
    component: MovieReviewCreate
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
  },
  {
    path: '/genre',
    name: 'genre',
    component: GenreSelectView
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
