<template>
		
	<div>
		<div>
			<h1>Now Playing</h1>
			<div >
				<NowPlaying :nowplaying_movies="nowplaying_movies" />
			</div>
			<h1>Genre1</h1>
			<div >
				<!-- <h1>{{ genre_1.name }}</h1> -->
				<GenreRecommend1 :genre="genres_1" :num="1" />
			</div>
			<h1>Genre2</h1>
			<div >
				<!-- <h1>{{ genre_2.name }}</h1> -->
				<GenreRecommend2 :genre="genres_2" :num="2" />
			</div>
			<h1>Genre3</h1>
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
		}
	},
	// beforeCreate() {
		
	// },
	
	created() {
		this.getMovie()
		
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
			this.nowplaying_movies = this.nowplaying_Movies(this.$store.state.movie_list)
			this.genres_1 = this.genres_Movie_1(this.$store.state.movie_list)
			this.genres_2 = this.genres_Movie_2(this.$store.state.movie_list)
			this.genres_3 = this.genres_Movie_3(this.$store.state.movie_list)
			this.temp_movie_list = JSON.stringify(this.$store.state.movie_list)
			
			localStorage.setItem('movie_list', this.temp_movie_list)
			localStorage.setItem('movie_list_length', this.$store.state.movie_list.length)
			
		},
		nowplaying_Movies(array) {
			let release_date_1 = '2023'
			let nowplaying_movies_list = []
			
			for(const movie of array) {
				if(movie.release_date.indexOf(release_date_1) !== -1 && nowplaying_movies_list.length < 30){
					nowplaying_movies_list.push(movie)
				}
			}
			console.log(nowplaying_movies_list.length)
			return nowplaying_movies_list
		},
		genres_Movie_1(array) {
			let genre_1_list = []

			let temp_genre_1 = 35

			for(const movie of array) {
				if (movie.genres.indexOf(temp_genre_1) !== -1 && genre_1_list.length < 30) {
					genre_1_list.push(movie)
				}
			}
			console.log(genre_1_list.length)
			return genre_1_list
		},		
		genres_Movie_2(array) {
			let genre_2_list = []

			let temp_genre_2 = 14
			for(const movie of array) {
				if (movie.genres.indexOf(temp_genre_2) !== -1 && genre_2_list.length < 30) {
					genre_2_list.push(movie)
				}
			}
			console.log(genre_2_list.length)
			return genre_2_list
		},
		genres_Movie_3(array) {
			let genre_3_list = []

			let temp_genre_3 = 10770
			for(const movie of array) {
				if (movie.genres.indexOf(temp_genre_3) !== -1 && genre_3_list.length < 30) {
					genre_3_list.push(movie)
				}
			}
			console.log(genre_3_list.length)
			return genre_3_list
		}		
	}
}

</script>

<style>


</style>