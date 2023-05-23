<template>
	<div>
		<button v-for="genre in genre_list" :key="genre.id">{{genre.name}}</button>
		<input type="submit" @click="genres" value="으아악">
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
			genre :[14,80,18],
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
	},
	methods:{
		genres(){
			const genre = this.genre
			axios({
				method:'post',
				url : 'http://127.0.0.1:8000/api/v1/usergenre/',
				data:{
					genre
				},
				headers:{
					Authorization : `Token ${this.$store.state.token}`					
				}
			})
			.then(()=>{})
			.catch(()=>{})
		}
	}
}
</script>

<style>

</style>