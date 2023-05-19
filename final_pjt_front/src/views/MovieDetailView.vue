<template>
	<div>
		<img :src="poster_URL" alt="">
		<h3>{{movie.title}}</h3>
	</div>
</template>

<script>
import axios from 'axios'
const Django_API_URL = 'http://127.0.0.1:8000'

export default {
	name: 'MovieDetailView',
	
	data() {
		return {
			movie: null,
			poster_URL: ''
		}
	},
	created() {
		this.getMovieDetail()
	},
	methods: {
		getMovieDetail() {
			axios({
				method: 'get',
				url: `${Django_API_URL}/api/v1/movie/${this.$route.params.movie_id}/`
			})
			.then((res) => {
				console.log(res)
				this.movie = res.data
				this.poster_URL = `https://www.themoviedb.org/t/p/w300_and_h450_bestv2${res.data.poster_path}`
			})
			.catch((err) => console.log(err))
		}	
	}
}
</script>

<style>

</style>