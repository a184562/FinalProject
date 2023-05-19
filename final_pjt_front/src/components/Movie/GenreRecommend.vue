<template>
	<div>
		<MovieCard v-for="movie in movies" :key="movie.id"
		:movie="movie" />
	</div>
</template>

<script>
import MovieCard from './MovieCard.vue'
// import axios from 'axios'

// const API_KEY = process.env.VUE_APP_MOVIE_API_KEY
// const movies_URL = `https://api.themoviedb.org/3/discover/movie?include_adult=false&include_video=false&language=en-US&page=1&sort_by=popularity.desc&api_key=${API_KEY}`

export default {
	name: 'GenreRecommend',
	components: {
		MovieCard,
	},
	data() {
		return {
			movies: null,
		}
	},
	created() {
	// 	axios({
	// 		method: 'get',
	// 		url: movies_URL,
	// 	})
	// 	.then((res) => {
	// 		// console.log(res)
	// 		this.movies = res.data.results
	// 	})
	// 	.catch((err) => console.log(err))
	}
}
</script>

<style>

</style>