<template>
	<div>
		<img :src="poster_URL" alt="">
		<h3>{{movie.title}}</h3>
	</div>
</template>

<script>
import axios from 'axios'

const API_KEY = process.env.VUE_APP_MOVIE_API_KEY
const movie_URL_1 = 'https://api.themoviedb.org/3/movie/'
const movie_URL_2 = `?api_key=${API_KEY}`

export default {
	name: 'MovieDetailView',
	
	data() {
		return {
			movie: null,
			movie_id : this.$route.params.movie_id,
			poster_URL : null,
		}
	},
	created() {
		axios({
			method: 'get',
			url: movie_URL_1 + `${this.movie_id}` + movie_URL_2,
		})
		.then((res) => {
			this.movie = res.data
			console.log(this.movie)
			this.poster_URL = `https://www.themoviedb.org/t/p/w300_and_h450_bestv2${this.movie.poster_path}`
		})
		.catch((err) => console.log(err))
	},
}
</script>

<style>

</style>