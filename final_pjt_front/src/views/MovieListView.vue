<template>
		
	<div>
		<div>
			<h1>Now Playing</h1>
			<div >
				<NowPlaying :nowplaying_movies="nowplaying_movies" />
			</div>
			<h1>{{ genre_data[0] }}</h1>
			<div >
				<!-- <h1>{{ genre_1.name }}</h1> -->
				<GenreRecommend1 :genre="genres_1" :num="1" />
			</div>
			<h1>{{ genre_data[1] }}</h1>
			<div >
				<!-- <h1>{{ genre_2.name }}</h1> -->
				<GenreRecommend2 :genre="genres_2" :num="2" />
			</div>
			<h1>{{ genre_data[2] }}</h1>
			<div >
				<!-- <h1>{{ genre_3.name }}</h1> -->
				<GenreRecommend3 :genre="genres_3" :num="3" />
			</div>
		</div>
	</div>
	
</template>

<script>
import GenreRecommend1 from '../components/Movie/GenreRecommend_1.vue'
import GenreRecommend2 from '../components/Movie/GenreRecommend_2.vue'
import GenreRecommend3 from '../components/Movie/GenreRecommend_3.vue'
import NowPlaying from '../components/Movie/NowPlaying.vue'
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
			genre_list : this.$store.state.genre_list
		}
	},
	// beforeCreate() {
		
	// },
	
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
		
		// this.getGenre()
		
		// this.nowplaying_movies = this.nowplaying_Movies()
		
		
		// if (this.genres_3.length < 25) {
		// 	while(this.genres_3.length < 25) {
		// 		this.genres_Movie_3()
		// 	}
		// }
	},
	methods: {
		// getGenre() {
		// 	return this.$stroe.dispatch('getGenre')
		// },
		async getMovie() {
			this.$store.dispatch('getMovie')
			setTimeout(() => {
				this.GetMovieData()
			}, 3000) 
			
			
		},
		GetMovieData() {
			this.nowplaying_movies = this.nowplaying_Movies(this.$store.state.movie_list)
			this.genres_1 = this.genres_Movie_1(this.$store.state.movie_list)
			this.genres_2 = this.genres_Movie_2(this.$store.state.movie_list)
			this.genres_3 = this.genres_Movie_3(this.$store.state.movie_list)
			this.temp_movie_list = JSON.stringify(this.$store.state.movie_list)
			
			localStorage.setItem('movie_list', this.temp_movie_list)
			localStorage.setItem('movie_list_length', this.$store.state.movie_list.length)
		},
		nowplaying_Movies(array) {
			let release_date_1 = '2023-05'
			let release_date_2 = '2023-04'
			let nowplaying_movies_list = []
			
			for(const movie of array) {
				if(movie.release_date.indexOf(release_date_1) !== -1 || movie.release_date.indexOf(release_date_2) !== -1 && nowplaying_movies_list.length < 30){
					nowplaying_movies_list.push(movie)
				}
			}
			console.log(nowplaying_movies_list.length)
			return nowplaying_movies_list
		},
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
			console.log(genre_1_list.length)
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
			console.log(genre_2_list.length)
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
			console.log(genre_3_list.length)
			return genre_3_list
		},
		getGenre() {
			this.$store.dispatch('getGenre')
			}		
	}
}

</script>

<style>


</style>