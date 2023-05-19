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
		
		this.nowplaying_Movies()
		
		this.genres_Movie_1()
		this.genres_Movie_2()
		this.genres_Movie_3()
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
		getMovie() {
			return this.$store.dispatch('getMovie')
		},
		nowplaying_Movies() {
			let release_date_1 = '2023'
			
			for(const movie of this.$store.state.movie_list) {
				if(movie.release_date.indexOf(release_date_1) !== -1 && this.nowplaying_movies.length < 25){
					this.nowplaying_movies.push(movie)
				}
			}
			
			console.log(this.nowplaying_movies.length)
			},
		genres_Movie_1() {
			this.genre_1 = 35

			for(const movie of this.$store.state.movie_list) {
				if (movie.genres.indexOf(this.genre_1) !== -1 && this.genres_1.length < 25) {
					this.genres_1.push(movie)
				}
			}
			console.log(this.genres_1.length)
		},		
		genres_Movie_2() {
			this.genre_2 = 14
			for(const movie of this.$store.state.movie_list) {
				if (movie.genres.indexOf(this.genre_2) !== -1 && this.genres_2.length < 25) {
					this.genres_2.push(movie)
				}
			}
			console.log(this.genres_2.length)
		},
		genres_Movie_3() {
			this.genre_3 = 10770
			for(const movie of this.$store.state.movie_list) {
				if (movie.genres.indexOf(this.genre_3) !== -1 && this.genres_3.length < 25) {
					this.genres_3.push(movie)
				}
			}
			console.log(this.genres_3.length)
		}		
	}
}

</script>

<style>


</style>