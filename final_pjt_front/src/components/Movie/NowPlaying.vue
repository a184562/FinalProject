<template>
	<div>
		<MovieCard />
		<p>1234</p>
	</div>
</template>

<script>
import MovieCard from './MovieCard.vue'
import axios from 'axios'

const API_KEY = process.env.VUE_APP_MOVIE_API_KEY
const nowplaying_URL = `https://api.themoviedb.org/3/discover/movie?include_adult=false&include_video=false&language=en-US&page=1&sort_by=popularity.desc&with_release_type=2|3&release_date.gte=2023-03-16&release_date.lte=2023-05-03&api_key=${API_KEY}`

export default {
	name: 'NowPlaying',
	components: {
		MovieCard,
	},
	created() {
		axios(nowplaying_URL, {
		
		})
		.then((res) => {
			console.log(res)
		})
		.catch((err) => console.log(err))
	},
	
	
}
</script>

<style>

</style>