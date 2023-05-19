<template>
	<div class="container">
		<div class="box"
		v-for="(movie, index) in genre" :key="index">
			<MovieCard :movie="movie"/>
		</div>
	
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
	props: {
		genre: Array,
	},
	// data() {
	// 	return {
	// 		movies: null,
	// 	}
	// },
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

<style scoped>
.container {
	display: flex;
	flex-wrap: wrap;
}
.box{
	width: 20%;
}
</style>