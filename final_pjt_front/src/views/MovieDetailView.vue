<template>
	<div>
		<div>
		<img :src="poster_URL" alt="">
		<h3>{{movie.title}}</h3>
		<h4>{{movie.release_date}}</h4>
		<h4>{{movie.genres}}</h4>
		<h4>{{movie.overview}}</h4>
		<h4>{{movie.like_users}}</h4>
		<h4>{{movie.comment_set}}</h4>
		<button v-if="!is_liked" @click="Like" >좋아요</button>
		<button v-else @click="Like">좋아요 취소</button>
		</div>
		<div>
			<form @submit.prevent="createMovieComment">
				<label for="movie_comment">한줄평</label>
				<input type="text" v-model="movie_comment">
				<input type="number" name="rank" min="1" max="5" v-model="rank">
				<input type="submit" value="제출">
			</form>
		</div>
	</div>
</template>

<script>
import axios from 'axios'
const Django_API_URL = 'http://127.0.0.1:8000'

export default {
	name: 'MovieDetailView',
	
	data() {
		return {
			movie: '',
			poster_URL: '',
			is_liked: false,
			movie_comment:null,
			rank:1,
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
		},
		Like(){
			axios({
				method:'post',
				url : `${Django_API_URL}/api/v1/movie/${this.$store.state.user_id}/${this.$route.params.movie_id}/likes/`
			})
			.then((res) =>{
				this.is_liked = res.data
			})
		},
		createMovieComment(){
			const content = this.movie_comment
			const rank = this.rank

			axios({
				method:'post',
				url: `${Django_API_URL}/api/v1/movie/${this.$route.params.movie_id}/comments/`,
				data:{
					content,rank
				},

				// headers: {
				// 	Authorization: `Token ${this.$store.state.token}`
				// }		
			})
			.then((res)=>{
				console.log(res)
			})
			.catch((err)=>{
				console.log(err)
			})
		}
	}
}
</script>

<style>

</style>