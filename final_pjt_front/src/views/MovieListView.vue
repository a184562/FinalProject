<template>
	<div>
		<div>
			<h1 class="menuline mt-4">Now Playing</h1>
			<div class="mt-3">
				<NowPlaying :nowplaying_movies="nowplaying_movies" />
			</div>
			<h1 class="menuline mt-4">{{ genre_data[0] }}</h1>
			<div class="mt-3">
				<GenreRecommend1 :genre="genres_1" />
			</div>
			<h1 class="menuline mt-4">{{ genre_data[1] }}</h1>
			<div class="mt-3">
				<GenreRecommend2 :genre="genres_2" />
			</div>
			<h1 class="menuline mt-4">{{ genre_data[2] }}</h1>
			<div class="mt-3">
				<GenreRecommend3 :genre="genres_3" />
			</div>
		</div>
	</div>
</template>

<script>
import GenreRecommend1 from '../components/Movie/GenreRecommend_1.vue'
import GenreRecommend2 from '../components/Movie/GenreRecommend_2.vue'
import GenreRecommend3 from '../components/Movie/GenreRecommend_3.vue'
import NowPlaying from '../components/Movie/NowPlaying.vue'

// 유저의 선호 영화 정보가 필요하므로 해당 페이지에서는 axios 사용
import axios from 'axios'
const Django_API_URL = 'http://127.0.0.1:8000'

export default {
	name: 'MovieListView',
	components: {
		NowPlaying,
		GenreRecommend1,
		GenreRecommend2,
		GenreRecommend3,
	},
	data() {
		return {
			temp_movie_list : null,
			nowplaying_movies: [],
			genres_1: [],
			genres_2: [],
			genres_3: [],
			genre_1 : null,
			genre_2 : null,
			genre_3 : null,
			like_genres: null,
			genre_data: [],
			genre_list : this.$store.state.genre_list,	
		}
	},
	// 현재 유저의 선호 장르 데이터가 필요하므로 axios 사용
	created() {
		axios({
		method:'get',
		url: `${Django_API_URL}/api/v1/user/${this.$store.state.user_data.pk}/`
		})
		.then((res) => {
			this.like_genres = res.data.genres
			for(const obj of this.genre_list){
					for(const userobj of this.like_genres){
						if (obj['id'] === userobj){
							this.genre_data.push(obj['name'])
						}
					}
				}
		})
		.catch((err) => console.log(err))
		this.getMovie()
		this.getGenre()
	},
	methods: {
		// 영화 데이터를 불러오는 과정을 2중으로 지연로딩해서 영화 데이터를 불러올 시간을 벌어줌
		getMovie() {
			this.$store.dispatch('getMovie')
			setTimeout(() => {
				this.GetMovieData()
			}, 3000)
		},
		getGenre() {
			this.$store.dispatch('getGenre')
		},
		GetMovieData() {
			this.nowplaying_movies = this.nowplaying_Movies(this.$store.state.movie_list)
			this.genres_1 = this.genres_Movie_1(this.$store.state.movie_list)
			this.genres_2 = this.genres_Movie_2(this.$store.state.movie_list)
			this.genres_3 = this.genres_Movie_3(this.$store.state.movie_list)
			this.temp_movie_list = JSON.stringify(this.$store.state.movie_list)
			// 최초 로딩 이후에는 빠르게 데이터를 불러오기 위해 로컬 스토리지에 저장
			localStorage.setItem('movie_list', this.temp_movie_list)
			localStorage.setItem('movie_list_length', this.$store.state.movie_list.length)
		},
		// 현재 상영작의 경우 최근 1달간 출시된 영화의 데이터를 실시간으로 받아 현재 상영작에 넣어준 뒤 데이터를 보내줌
		nowplaying_Movies(array) {
			// 오늘 날짜를 받아오는 과정
			let today = new Date()
			let today_year = today.getFullYear()
			let today_month = today.getMonth() + 1
			let release_date_1
			let release_date_2
			if (today_month >= 11) {
				release_date_1 = today_year.toString() + '-' + today_month.toString()
				release_date_2 = today_year.toString() + '-' + (today_month-1).toString()
			}
			else if (today_month === 10) {
				release_date_1 = today_year.toString() + '-' + today_month.toString()
				release_date_2 = today_year.toString() + '-' + '0' + (today_month-1).toString()
			}
			else {
				release_date_1 = today_year.toString() + '-' + '0' + today_month.toString()
				release_date_2 = today_year.toString() + '-' + '0' + (today_month-1).toString()
			}
			// 날짜를 받아 온 뒤 리스트에 넣어 줌
			let nowplaying_movies_list = []
			for(const movie of array) {
				if(movie.release_date.indexOf(release_date_1) !== -1 && nowplaying_movies_list.length < 30 || movie.release_date.indexOf(release_date_2) !== -1 && nowplaying_movies_list.length < 30){
					nowplaying_movies_list.push(movie)
				}
			}
			return nowplaying_movies_list
		},
		// 선호하는 장르 데이터를 받아 선호 장르 id와 영화의 genre가 겹치는 영화들의 리스트를 반환
		// 최적화를 위해서 nowplaying과 달리 12개로 제한
		genres_Movie_1(array) {
			let genre_1_list = []
			let temp_genre_1 = 35
			if(this.$store.state.token !== null) {
				temp_genre_1 = this.like_genres[0]
			}
			for(const movie of array) {
				if (movie.genres.indexOf(temp_genre_1) !== -1 && genre_1_list.length < 12) {
					genre_1_list.push(movie)
				}
			}
			return genre_1_list
		},		
		genres_Movie_2(array) {
			let genre_2_list = []
			let temp_genre_2 = 14
			if(this.$store.state.token !== null) {
				temp_genre_2 = this.like_genres[1]
			}
			for(const movie of array) {
				if (movie.genres.indexOf(temp_genre_2) !== -1 && genre_2_list.length < 12) {
					genre_2_list.push(movie)
				}
			}
			return genre_2_list
		},
		genres_Movie_3(array) {
			let genre_3_list = []
			let temp_genre_3 = 10770
			if(this.$store.state.token !== null) {
				temp_genre_3 = this.like_genres[2]
			}
			for(const movie of array) {
				if (movie.genres.indexOf(temp_genre_3) !== -1 && genre_3_list.length < 12) {
					genre_3_list.push(movie)
				}
			}
			return genre_3_list
		},
	}
}
</script>

<style scoped>
.menuline {
	text-align: start;
	margin-left: 14rem;
}

</style>