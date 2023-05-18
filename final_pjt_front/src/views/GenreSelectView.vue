<template>
	<div>
		<button v-for="genre in genre_list" :key="genre.id">{{genre.name}}</button>
	</div>
</template>

<script>
import axios from 'axios'

const API_KEY = process.env.VUE_APP_MOVIE_API_KEY
const Genre_URL = `https://api.themoviedb.org/3/genre/movie/list?api_key=${API_KEY}`

export default {
	name: 'GenreSelect',
	data() {
		return {
			genre_list : null,
		}
	},
	created() {
		axios({
			method: 'get',
			url: Genre_URL,
		})
		.then((res) => {
			this.genre_list = res.data.genres
		})
		.catch((err) => console.log(err))
	}
}
</script>

<style>

</style>