<template>
	<div>
		<div>
			<button @click="selectOne">1</button>
			<button @click="selectTwo">2</button>
			<button @click="selectThree">3</button>
		</div>
		<input type="submit" @click="gotoGame" value="게임시작">
	</div>
</template>

<script>
import axios from 'axios'

const API_KEY = process.env.VUE_APP_MOVIE_API_KEY
const popular_Movie_URL = `https://api.themoviedb.org/3/discover/movie?include_adult=false&include_video=false&language=en-US&page=1&sort_by=popularity.desc&api_key=${API_KEY}`
const nowplaying_Movie_URL = `https://api.themoviedb.org/3/discover/movie?include_adult=false&include_video=false&language=en-US&page=1&sort_by=popularity.desc&with_release_type=2|3&release_date.gte=2023-03-16&release_date.lte=2023-05-03&api_key=${API_KEY}`
const toprated_Movie_URL = `https://api.themoviedb.org/3/discover/movie?include_adult=false&include_video=false&language=en-US&page=1&sort_by=vote_average.desc&without_genres=99,10755&vote_count.gte=200&api_key=${API_KEY}`

let selectURL
let selectNum = 1



export default {
	name: 'EntertainView',
	data() {
		return {
			movie_list : null,
		}
	},
	methods: {
		selectOne() {
			selectNum = 1
		},
		selectTwo() {
			selectNum = 2
			
		},
		selectThree() {
			selectNum = 3
			
		},
		gotoGame() {
			if (selectNum === 1) {
				selectURL = popular_Movie_URL
			} else if (selectNum === 2) {
				selectURL = nowplaying_Movie_URL
			} else {
				selectURL = toprated_Movie_URL
			}
			axios({
				method: 'get',
				url: selectURL,
			})
			.then((res) => {
				// console.log(res)
				this.movie_list = res.data.results
				// console.log(this.movie_list)
				this.$router.push({
				name: 'game',
				params: {movie_list : this.movie_list}
				})
			})
			.catch((err) => console.log(err))

			
			// console.log(this.movie_list)
		}
	}
}
</script>

<style>

</style>