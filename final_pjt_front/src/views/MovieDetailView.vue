<template>
	<div class="detail container">
		<div class="row">
			<img class="col-6 mt-4 ms-3" :src="poster_URL" alt="">
			<div class="col-6 mt-5">
				<h3>{{movie.title}}</h3><br><hr>
				<h5>개봉일 : {{movie.release_date}}</h5><br>
				<div class="d-flex">
					<h5>장르 : </h5>
					<div v-for="(genre_name,index) in genre_data" :key="index" class="ms-3">
						<h5>{{genre_name}}</h5>
					</div>
				</div>
				<hr>
				<p>{{movie.overview}}</p>
			</div>
			<div class="articleBtn d-flex mt-4">
				<button class="btn btn-dark ms-3" @click="$router.push({name:'movies'})">목록으로</button>
			</div>
			<div class="like">
				<p class="mt-3">좋아요 : {{ movie.like_users.length }}</p>
				<button class="btn btn-secondary" v-if="!is_liked" @click="Like" >좋아요</button>
				<button class="btn btn-secondary" v-if="is_liked" @click="Like">좋아요 취소</button>
			</div>
			
		</div>
		<form @submit.prevent="createMovieComment" class="pb-3">
			<div class="input-group mb-3 ms-3 me-3 mt-3" style="width: 95%;">
				<span class="input-group-text">한줄평</span>
				<input class="form-control" type="text" v-model="movie_comment">
				
				<input class="btn btn-dark" type="submit" style="width: 75px;" value="작성">
			</div>
			<div class="btn-group me-3 rank mb-3 ms-3 me-3 mt-3" role="rank" aria-label="Basic radio toggle button group">
				<label class="btn btn-outline-secondary disabled" aria-disabled="true">별점</label>
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
		</form>
		
		
		<div class="commentlist">
			<p>댓글 수 : {{ movie['comment_set'].length }}</p>
			<ul v-for="(contents,index) in movie['comment_set']" :key="index">
				<li v-if="contents['user']==user_id" class="comment">
					<div class="me-4 mt-4">
						<router-link :to="{
							name: 'otherprofile',
							params: {id: contents?.id, username: contents?.username}
						}">{{contents['username']}}</router-link>
					</div>
					<div class="d-flex justify-content-between mt-3">
						<div class="d-flex">
							<p class="me-4">별점 : {{ contents['rank'] }}</p>
							<p>{{contents['content']}}</p>
						</div>
						<p class="me-5">{{contents['created_at']}}</p>
					</div>
					<div class="pb-4">
						<button class="btn btn-dark btn-sm me-2" type="submit" value="한줄평 수정"  @click="commentPutOn" :data="index">한줄평 수정</button>
						<button class="btn btn-dark btn-sm" type="submit" value="한줄평 삭제"  @click="commentDelete" :data="index">한줄평 삭제</button>
						<form @submit.prevent="commentPut" class="pb-3" v-if="put_check & put_index==index" :data="index">
							<div class="input-group mb-3 ms-3 me-3 mt-3" style="width: 95%;">
							<span class="input-group-text">한줄평</span>
							<input class="form-control" type="text" v-model="new_content">
							<input class="btn btn-dark" type="submit" style="width: 75px;" value="작성">
							</div>
						</form>
					</div>
					
				</li>
				<li v-else class="comment">
					<div class="me-4 mt-4">
						<router-link :to="{
							name: 'otherprofile',
							params: {id: contents?.user, username: contents?.username}
						}">{{contents['username']}}</router-link>
					</div>
					<div class="d-flex justify-content-between mt-3">
						<div class="d-flex">
							<p class="me-4">별점 : {{ contents['rank'] }}</p>
							<p>{{contents['content']}}</p>
						</div>
						<p class="me-5">{{contents['created_at']}}</p>
					</div>
				</li>
			</ul>
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
			genre_list: this.$store.state.genre_list,
			user_id : this.$store.state.user_data.pk,
			put_check:false,
			new_content:'',
			put_index:null,
			genre_data: [],
		}
	},
	created() {
		this.getMovieDetail()
		// 영화 좋아요 버튼의 경우 각 영화마다 DB에서 호출할 방법을 store에서 관리할 방법을 찾지 못해 직접 호출
		axios({
			method:'get',
			url : `${Django_API_URL}/api/v1/movie/${this.$store.state.user_data.pk}/${this.$route.params.movie_id}/likes/`
		})
		.then((res)=>this.is_liked= res.data)

		
	},
	methods: {
		// 영화의 Detail 정보를 받아옴
		getMovieDetail() {
			axios({
				method: 'get',
				url: `${Django_API_URL}/api/v1/movie/${this.$route.params.movie_id}/`
			})
			.then((res) => {
				this.movie = res.data
				this.poster_URL = `https://www.themoviedb.org/t/p/w300_and_h450_bestv2${res.data.poster_path}`
				this.genreData()
			})
			.catch((err) => console.log(err))
		},
		genreData() {
			for(const obj of this.genre_list) {
				for(const genre_id of this.movie.genres) {
					if(obj['id'] === genre_id) {
						this.genre_data.push(obj['name'])
					}
				}
			}
		},
		// 영화의 좋아요 정보를 받아옴
		Like(){
			axios({
				method:'post',
				url : `${Django_API_URL}/api/v1/movie/${this.$store.state.user_data.pk}/${this.$route.params.movie_id}/likes/`
			})
			.then((res) =>{
				this.is_liked = res.data
				this.$router.go(0)
			})
		},
		// 영화에 한줄평을 추가하는 로직
		createMovieComment(){
			const content = this.movie_comment
			const radioValue = document.getElementsByName('btnradio')
			const movie = this.movie.id
			radioValue.forEach((radio) => {
				if(radio.checked) {
					this.rank = Number(radio.value)
				}
			})
			const rank = this.rank
			axios({
				method:'post',
				url: `${Django_API_URL}/api/v1/movie/${this.$route.params.movie_id}/comments/`,
				data:{
					content,rank,movie
				},
				headers:{
					Authorization : `Token ${this.$store.state.token}`
				}
			})
			.then(()=>{
				this.$router.go(0)
			})
			.catch((err)=>{
				console.log(err)
			})
		},
		// 댓글을 수정
		commentPutOn(comment){
			if (this.put_check){
				this.put_index = null
				return this.put_check = false
			}else{
				const index = comment.target.getAttribute('data')
				this.put_index = index
				return this.put_check = true
			}
		},
		commentPut(comment){
			const index = comment.target.getAttribute('data')
			const comment_data = this.movie['comment_set'][index]['id']
			const content = this.new_content
			const movie = this.movie['id']
			const rank = this.rank
			if (!content){
				alert('변경할 내용을 입력해주세요')
				return
			}
			axios({
				method:'put',
				url:`${Django_API_URL}/api/v1/comment/${comment_data}/`,
				data:{
					content,movie,rank
				}
			})
			.then(()=>{this.$router.go(0)})
			.catch(()=>{})
		},
		// 댓글 삭제
		commentDelete(comment){
			const index = comment.target.getAttribute('data')
			const comment_data = this.movie['comment_set'][index]['id']
			axios({
				method:'delete',
				url:`${Django_API_URL}/api/v1/comment/${comment_data}/`,
			})
			.then(()=>{this.$router.go(0)})
			.catch(()=>{})
		},
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
	/* height: 75%; */
	box-shadow: 4px 4px 4px grey;
	background-color: #141414;
	margin-bottom: 15rem;
	margin-top: 5rem;
}
div a {
	font-weight: bold;
	font-size: 20px;
	color: #ffffff;
	text-decoration-line: none;
}
.like {
	text-align: start;
	margin-top: 3px;
	padding-bottom: 25px;
	margin-left: 15px;
}
.rank {
	display: flex;
	width: 30%;
}
.commentlist {
	text-align: start;
}
.comment {
	border-bottom: solid grey 1px;
}
</style>