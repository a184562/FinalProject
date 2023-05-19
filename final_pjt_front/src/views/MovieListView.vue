<template>
	<div>
		<div>
			<h1>Now Playing</h1>
			<NowPlaying />
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
			nowplaying_movies: null,
			genres: null,
		}
	},
	created() {
		// axios({
		// 	method: 'get',
		// 	url: nowplaying_URL,
		// })
		// .then((res) => {
		// 	// console.log(res)
		// 	this.nowplaying_movies = res.data.results
		// 	this.plusMovies()
		// })
		// .catch((err) => console.log(err))

		
	},
	methods: {
		// plusMovies() {
		// 	for (const movie_data of this.nowplaying_movies) {
		// 		// console.log(movie_data)
		// 		this.$store.dispatch('insertMoviedata', movie_data)
		// 	}
		// },
		getArticle() {
			return this.$store.dispatch('getMovie')
		}
	}
}
</script>

<style>

</style>