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
import GameDatePlay from '../components/Entertain/GameDate.vue'
import GameRatePlay from '../components/Entertain/GameRate.vue'
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
  // 영화 리스트 페이지 (최초에 메인페이지였으나 수정)
  {
    path: '/movies',
    name: 'movies',
    component: MovieListView
  },
  // 영화 디테일 페이지
  {
    path: '/movie/:movie_id',
    name: 'movie',
    component: MovieDetailView
  },
  // 커뮤니티 메인 페이지
  {
    path: '/community',
    name: 'community',
    component: CommunityView
  },
  // 커뮤니티 자유게시판 페이지
  {
    path: '/community/free',
    name: 'free',
    component: FreeBoard
  },
  // 커뮤니티 자유게시판 게시글 페이지
  {
    path: '/community/free/:id',
    name: 'freeboarddetail',
    component: FreeBoardDetail
  },
  // 커뮤니티 자유게시판 게시글 작성 페이지
  {
    path: '/community/free/create',
    name: 'freecreate',
    component: FreeBoardCreate
  },
  // 커뮤니티 자유게시판 게시글 수정 페이지
  {
    path:'/community/free/edit/:id',
    name: 'FreeBoardEdit',
    component:FreeBoardEdit
  },
  // 커뮤니티 리뷰게시판 페이지
  {
    path: '/community/review',
    name: 'review',
    component: MovieReview
  },
  // 커뮤니티 리뷰게시판 게시글 페이지
  {
    path: '/community/review/:id',
    name: 'reviewdetail',
    component: MovieReviewDetail
  },
  // 커뮤니티 리뷰게시판 게시글 작성 페이지
  {
    path: '/community/review/create',
    name: 'reviewcreate',
    component: MovieReviewCreate
  },
  // 커뮤니티 리뷰게시판 게시글 수정 페이지
  {
    path:'/community/review/edit/:id',
    name:'moviereviewedit',
    component: MovieReviewEdit,
  },
  // 로그인 페이지(현재 메인페이지)
  {
    path: '/',
    name: 'login',
    component: LogIn
  },
  // 회원가입 페이지
  {
    path: '/signup',
    name: 'signup',
    component: SignUp
  },
  // 검색 페이지
  {
    path: '/search',
    name: 'search',
    component: SearchView
  },
  // 게임 메인 페이지
  {
    path: '/entertain',
    name: 'entertain',
    component: EntertainView
  },
  // 관객수 게임 페이지
  {
    path: '/entertain/game',
    name: 'game',
    component: GamePlay
  },
  // 출시날짜 게임 페이지
  {
    path: '/entertain/gamedate',
    name: 'gamedate',
    component: GameDatePlay
  },
  // 평점 게임 페이지
  {
    path: '/entertain/gamerate',
    name: 'gamerate',
    component: GameRatePlay
  },
  // 장르 선택 페이지
  {
    path: '/genre',
    name: 'genre',
    component: GenreSelectView
  },
  // 내 프로필 페이지
  {
    path: '/profile',
    name: 'profile',
    component: ProfileView
  },
  // 다른 유저 프로필 페이지
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
