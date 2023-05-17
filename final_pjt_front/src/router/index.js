import Vue from 'vue'
import VueRouter from 'vue-router'
import MovieListView from '../views/MovieListView.vue'
import CommunityView from '../views/CommunityView.vue'
import EntertainView from '../views/EntertainView.vue'
import MovieDetailView from '../views/MovieDetailView.vue'
import FreeBoard from '../components/Community/FreeBoard.vue'
import MovieReview from '../components/Community/MovieReview.vue'

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
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
