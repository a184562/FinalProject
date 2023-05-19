<template>
	<div>
		<div>
			<h1>Now Playing</h1>
			<NowPlaying :nowplaying_movies="nowplaying_movies" />
			<p>{{nowplaying_movies}}</p>
		</div>
		<div>
			<h1>Genre1</h1>
			<GenreRecommend />
		</div>
		<div>
			<h1>Genre2</h1>
			<GenreRecommend />
		</div>
		<div>
			<h1>Genre3</h1>
			<GenreRecommend />
		</div>
		
	</div>
</template>

<script>
import GenreRecommend from '../components/Movie/GenreRecommend.vue'
import NowPlaying from '../components/Movie/NowPlaying.vue'
// import axios from 'axios'

// const API_KEY = process.env.VUE_APP_MOVIE_API_KEY
// const nowplaying_URL = `https://api.themoviedb.org/3/discover/movie?include_adult=false&include_video=false&language=en-US&page=1&sort_by=popularity.desc&with_release_type=2|3&release_date.gte=2023-03-16&release_date.lte=2023-05-03&api_key=${API_KEY}`
// const genre_URL = `https://api.themoviedb.org/3/genre/movie/list?language=en&api_key=${API_KEY}`




export default {
	name: 'MovieListView',
	components: {
		NowPlaying,
		GenreRecommend,
	},
	data() {
		return {
			nowplaying_movies: [],
			genres: null,
		}
	},
	created() {
		this.getMovie()	
		this.nowplaying_Movies()
		
	},
	methods: {
		getMovie() {
			return this.$store.dispatch('getMovie')
		},
		nowplaying_Movies() {
			let release_date_1 = '2023'
			for(const movie of this.$store.state.movie_list) {
				if(movie.release_date.indexOf(release_date_1) !== -1){
					this.nowplaying_movies.push(movie)
				}
			}
			console.log(this.nowplaying_movies)
		}
	}
}
</script>

<style>

</style>