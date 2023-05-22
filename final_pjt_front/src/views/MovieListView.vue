<template>
	<div>
		<h1>Now Playing</h1>
		<div >
			<NowPlaying :nowplaying_movies="nowplaying_movies" />
		</div>
		<h1>Genre1</h1>
		<div >
			<!-- <h1>{{ genre_1.name }}</h1> -->
			<GenreRecommend :genre="genres_1" />
		</div>
		<h1>Genre2</h1>
		<div >
			<!-- <h1>{{ genre_2.name }}</h1> -->
			<GenreRecommend :genre="genres_2" />
		</div>
		<h1>Genre3</h1>
		<div >
			<!-- <h1>{{ genre_3.name }}</h1> -->
			<GenreRecommend :genre="genres_3" />
		</div>
		
	</div>
</template>

<script>
import GenreRecommend from '../components/Movie/GenreRecommend.vue'
import NowPlaying from '../components/Movie/NowPlaying.vue'

export default {
	name: 'MovieListView',
	components: {
		NowPlaying,
		GenreRecommend,
	},
	data() {
		return {

			nowplaying_movies: [],
			genres_1: [],
			genres_2: [],
			genres_3: [],
			genre_1 : null,
			genre_2 : null,
			genre_3 : null,
		}
	},
	created() {
		this.getMovie()
		// this.getGenre()
		
		this.nowplaying_movies = this.nowplaying_Movies()
		
		this.genres_1 = this.genres_Movie_1()
		this.genres_2 = this.genres_Movie_2()
		this.genres_3 = this.genres_Movie_3()
		// if (this.genres_3.length < 25) {
		// 	while(this.genres_3.length < 25) {
		// 		this.genres_Movie_3()
		// 	}
		// }
	},
	computed: {
		getGenre() {
			return this.$stroe.dispatch('getGenre')
		},
		// getMovie() {
		// 	return this.$store.dispatch('getMovie')
		// },
		nowplaying_Movies() {
			let release_date_1 = '2023'
			let nowplaying_movies_list = []
			
			for(const movie of this.$store.state.movie_list) {
				if(movie.release_date.indexOf(release_date_1) !== -1 && nowplaying_movies_list.length < 25){
					nowplaying_movies_list.push(movie)
				}
			}
			console.log(nowplaying_movies_list.length)
			return nowplaying_movies_list
		},
		genres_Movie_1() {
			let genre_1_list = []

			let temp_genre_1 = 35

			for(const movie of this.$store.state.movie_list) {
				if (movie.genres.indexOf(temp_genre_1) !== -1 && genre_1_list.length < 25) {
					genre_1_list.push(movie)
				}
			}
			console.log(genre_1_list.length)
			return genre_1_list
		},		
		genres_Movie_2() {
			let genre_2_list = []

			let temp_genre_2 = 14
			for(const movie of this.$store.state.movie_list) {
				if (movie.genres.indexOf(temp_genre_2) !== -1 && genre_2_list.length < 25) {
					genre_2_list.push(movie)
				}
			}
			console.log(genre_2_list.length)
			return genre_2_list
		},
		genres_Movie_3() {
			let genre_3_list = []

			let temp_genre_3 = 10770
			for(const movie of this.$store.state.movie_list) {
				if (movie.genres.indexOf(temp_genre_3) !== -1 && genre_3_list.length < 25) {
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