import Vue from 'vue'
import VueRouter from 'vue-router'
import MovieListView from '../views/MovieListView.vue'
import MovieDetailView from '../views/MovieDetailView.vue'
import CommunityView from '../views/CommunityView.vue'
import FreeBoard from '../components/Community/FreeBoard.vue'
import FreeBoardDetail from '../components/Community/FreeBoardDetail.vue'
import FreeBoardCreate from  '../components/Community/FreeBoardCreate.vue'
import MovieReview from '../components/Community/MovieReview.vue'
import MovieReviewDetail from '../components/Community/MovieReviewDetail.vue'
import MovieReviewCreate from '../components/Community/MovieReviewCreate.vue'
import EntertainView from '../views/EntertainView.vue'
import GamePlay from '../components/Entertain/Game.vue'
import GenreSelectView from '../views/GenreSelectView.vue'
import SearchView from '../views/SearchView.vue'
import LogIn from '../views/Login.vue'
import SignUp from '../views/Signup.vue'
import ProfileView from '../views/ProfileView.vue'
import OtherUserProfile from '../views/OtherUserProfile.vue'
import FreeBoardEdit from '../components/Community/FreeBoardEdit.vue'
import MovieReviewEdit from '../components/Community/MovieReviewEdit'


Vue.use(VueRouter)

const routes = [
  {
    path: '/movies',
    name: 'movies',
    component: MovieListView
  },
  {
    path: '/movie/:movie_id',
    name: 'movie',
    component: MovieDetailView
  },
  {
    path: '/community',
    name: 'community',
    component: CommunityView
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
    path:'/community/free//edit/:id',
    name: 'FreeBoardEdit',
    component:FreeBoardEdit
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
    path:'/community/review/edit/:id',
    name:'moviereviewedit',
    component: MovieReviewEdit,
  },
  {
    path: '/community/review/create',
    name: 'reviewcreate',
    component: MovieReviewCreate
  },
  {
    path: '/',
    name: 'login',
    component: LogIn
  },
  {
    path: '/signup',
    name: 'signup',
    component: SignUp
  },
  {
    path: '/search',
    name: 'search',
    component: SearchView
  },
  {
    path: '/entertain',
    name: 'entertain',
    component: EntertainView
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
  },
  {
    path: '/profile',
    name: 'profile',
    component: ProfileView
  },
  {
    path: '/profile/:id',
    name: 'otherprofile',
    component: OtherUserProfile
  },
  
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
