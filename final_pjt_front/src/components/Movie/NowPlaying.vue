<template>
	<div class="container">
		<!-- <p>{{nowplaying_movies}}</p> -->
		<div class="item"
		v-for="movie in nowplaying_movies" :key="movie.id">
			<MovieCard :movie="movie" />
		</div>
	</div>
</template>

<script>
import MovieCard from './MovieCard.vue'
// import axios from 'axios'

// const API_KEY = process.env.VUE_APP_MOVIE_API_KEY
// const nowplaying_URL = `https://api.themoviedb.org/3/discover/movie?include_adult=false&include_video=false&language=en-US&page=1&sort_by=popularity.desc&with_release_type=2|3&release_date.gte=2023-03-16&release_date.lte=2023-05-03&api_key=${API_KEY}`



export default {
	name: 'NowPlaying',
	components: {
		MovieCard,
	},
	props: {
		nowplaying_movies: Array,
	},
	
	// data() {
	// 	return {

	// 	}
	// }
	// data() {
	// 	return {
	// 		nowplaying_movies : null,
	// 	}
	// },
	// created() {
	// 	axios({
	// 		method: 'get',
	// 		url: nowplaying_URL,
	// 	})
	// 	.then((res) => {
	// 		this.nowplaying_movies = res.data.results
	// 		this.plus()
	// 	})
	// 	.catch((err) => console.log(err))
		
		
	// },
	// methods: {
	// 	plus() {
	// 		for (const movie_data of this.nowplaying_movies) {
	// 			console.log(movie_data)
	// 			this.$store.dispatch('insertMoviedata', movie_data)
	// 		}
	// 	}
	// }
	
	
	
}
</script>

<style>
.container {
	display: grid;
	
}
</style>