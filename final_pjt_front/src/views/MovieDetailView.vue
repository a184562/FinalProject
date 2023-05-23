<template>
	<div class="detail container">
		<div class="row">
			<img class="col-6 mt-4 ms-3" :src="poster_URL" alt="">
			<div class="col-6 mt-5">
				<h3>{{movie.title}}</h3><br><hr>
				<h5>개봉일 : {{movie.release_date}}</h5><br>
				<h5>{{movie.genres}}</h5><br>
				<hr>
				<p>{{movie.overview}}</p>
			</div>
			<div class="comment">
				<p class="mt-3">좋아요 : {{movie.like_users.length}}</p>
				<p>댓글 : {{movie.comment_set.length}}</p>
				<button class="btn btn-secondary" v-if="!is_liked" @click="Like" >좋아요</button>
				<button class="btn btn-secondary" v-else @click="Like">좋아요 취소</button>
			</div>
			
		</div>
		<div>
			<form class="mt-4 mb-5 comment" @submit.prevent="createMovieComment">
				<label class="me-2" for="movie_comment">한줄평 : </label>
				<input class="me-3" type="text" v-model="movie_comment">
				<div class="btn-group me-3" role="rank" aria-label="Basic radio toggle button group">
					<input type="radio" class="btn-check" name="btnradio" id="btnradio1" value=1 autocomplete="off">
					<label class="btn btn-outline-secondary" for="btnradio1">1</label>

					<input type="radio" class="btn-check" name="btnradio" id="btnradio2" value=2 autocomplete="off">
					<label class="btn btn-outline-secondary" for="btnradio2">2</label>

					<input type="radio" class="btn-check" name="btnradio" id="btnradio3" value=3 autocomplete="off">
					<label class="btn btn-outline-secondary" for="btnradio3">3</label>

					<input type="radio" class="btn-check" name="btnradio" id="btnradio4" value=4 autocomplete="off">
					<label class="btn btn-outline-secondary" for="btnradio4">4</label>

					<input type="radio" class="btn-check" name="btnradio" id="btnradio5" value=5 autocomplete="off">
					<label class="btn btn-outline-secondary" for="btnradio5">5</label>
				</div>
				<input class="btn btn-secondary" type="submit" value="제출">
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
			rank: 1,
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
				url : `${Django_API_URL}/api/v1/movie/${this.$store.state.user_data.pk}/${this.$route.params.movie_id}/likes/`
			})
			.then((res) =>{
				this.is_liked = res.data
			})
		},
		createMovieComment(){
			const content = this.movie_comment
			let rank = this.rank
			const radioValue = document.getElementByName('btnradio')
			radioValue.forEach((radio) => {
				if(radio.checked) {
					rank = radio.value
				}
			})

			axios({
				method:'post',
				url: `${Django_API_URL}/api/v1/movie/${this.$route.params.movie_id}/comments/`,
				data:{
					content,rank
				},
				headers:{
					Authorization : `Token ${this.$store.state.token}`
				}
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

<style scoped>


img {
	border-radius: 1rem;
	width: 450px;
	height: 600px;
}
.detail {
	border-radius: 0.5rem;
	margin: auto;
	width: 1000px;
	height: 75%;
	box-shadow: 4px 4px 4px grey;
	background-color: #141414;
	margin-bottom: 15rem;
	margin-top: 5rem;
}
.comment {
	text-align: start;
	margin-top: 3px;
	padding-bottom: 25px;
	margin-left: 15px;
}

</style>