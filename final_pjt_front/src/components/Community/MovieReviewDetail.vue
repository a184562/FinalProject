<template>
	<div class="detail">
		<div class="mt-5">
			<div class="articletitle d-flex justify-content-between">
				<h1>{{ review_article?.title }}</h1>
				<div class="me-4 mt-4">
					<label for="profile">작성자</label> :
					<router-link :to="{
						name: 'otherprofile',
						params: {id: review_article?.user, username: review_article?.username}
					}">{{review_article?.username}}</router-link>
				</div>
			</div>
			
			<div class="articleContent mt-4">
				<p>{{ review_article?.content }}</p>
			</div>
			<div class="articleTime mt-4 ms-4">
				<p>작성시간 : {{ created_at }}</p>
				<p>수정시간 : {{ updated_at}}</p>
			</div>
		</div>
		
		<div v-if="review_article?.user==user_id" class="articleBtn d-flex mt-4">
			<button class="btn btn-dark ms-3" @click="$router.push({name:'review'})">목록으로</button>
			<button class="btn btn-dark ms-3" @click="putArticle">게시글 수정</button>
			<button class="btn btn-dark ms-3" @click="deleteArticle">게시글 삭제</button>
		</div>
		<div v-else class="articleBtn d-flex mt-4">
			<button class="btn btn-dark ms-3" @click="$router.push({name:'review'})">목록으로</button>
		</div>
		<div class="like">
			<p class="mt-3">좋아요 : {{review_article.like_users.length}}</p>
			<button class="btn btn-secondary" v-if="!is_liked" @click="Like" >좋아요</button>
			<button class="btn btn-secondary" v-if="is_liked" @click="Like">좋아요 취소</button>
		</div>
		<form @submit.prevent="createComment" class="pb-2">
			<div class="input-group mb-3 ms-3 me-3 mt-3" style="width: 95%;">
				<span class="input-group-text">댓글</span>
				<input class="form-control" type="text" v-model="content">
				<input class="btn btn-dark" type="submit" style="width: 75px;" value="작성">
			</div>
		</form>

		<div>
			<p>댓글 수 : {{ review_article['reviewcomment_set'].length }}</p>
			<ul v-for="(contents,index) in review_article['reviewcomment_set']" :key="index" class="commentlist">
				<li v-if="contents['user']==user_id" class="comment">
					<div class="me-4 mt-4">
						<router-link :to="{
							name: 'otherprofile',
							params: {id: contents?.user, username: contents?.username}
						}">{{contents['username']}}</router-link>
					</div>
					<div class="d-flex justify-content-between mt-3">
						<p>{{contents['content']}}</p>
						<p class="me-5">{{contents['created_at']}}</p>
					</div>
					<div class="pb-4">
						<button class="btn btn-dark btn-sm me-2" type="submit" value="댓글 수정"  @click="commentPutOn" :data="index">댓글 수정</button>
						<button class="btn btn-dark btn-sm" type="submit" value="댓글 삭제"  @click="commentDelete" :data="index">댓글 삭제</button>
						<form @submit.prevent="commentPut" class="pb-2" v-if="put_check & put_index==index" :data="index">
							<div class="input-group mb-3 ms-3 me-3 mt-3" style="width: 95%;">
								<span class="input-group-text">댓글</span>
								<input class="form-control" type="text" v-model="new_content">
								<input class="btn btn-dark" type="submit" style="width: 75px;" value="작성">
							</div>
						</form>	
					</div>
				
				</li>
				<li v-else>
					<div class="me-4 mt-4">
						<router-link :to="{
							name: 'otherprofile',
							params: {id: contents?.user, username: contents?.username}
						}">{{contents['username']}}</router-link>
					</div>
					<div class="d-flex justify-content-between mt-3">
						<p>{{contents['content']}}</p>
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
	name: "MovieReviewDetail",
	data() {
		return {
			user_id: this.$store.state.user_data.pk,
			review_article: null,
			is_liked :null,
			content : '',
			created_at : "",
			updated_at : "",
			new_content : "",
			put_check : false,
			put_index:null,
		}
	},
	
	created() {
		// 현재 로그인한 유저의 데이터가 필요하므로 axios 사용
		this.getReviewDetail()
		axios({
			method:'get',
			url:`${Django_API_URL}/api/v1/community/review/${this.$store.state.user_data.pk}/${this.$route.params.id}/likes/`
		})
		.then((res)=> this.is_liked = res.data)
	},
	methods: {
		getReviewDetail() {
			axios({
				method: 'get',
				url: `${Django_API_URL}/api/v1/community/review/${this.$route.params.id}/`,
			})
			.then((res) => {
				this.review_article = res.data
				for (let i = 0; i < res.data.created_at.length; i++) {
					if (i < 4) {
						this.created_at = this.created_at + res.data.created_at[i]
					}
					if (i === 4) {
						this.created_at = this.created_at + '년 '
					}
					if (i === 5 || i === 6 ) {
						this.created_at = this.created_at + res.data.created_at[i]
					}
					if (i === 7) {
						this.created_at = this.created_at + '월 '
					}
					if (i === 8 || i === 9 ) {
						this.created_at = this.created_at + res.data.created_at[i]
					}
					if (i === 10) {
						this.created_at = this.created_at + '일 '
					}
					if (i < 19 && i >10) {
						this.created_at = this.created_at + res.data.created_at[i]
					}
					
				}
				for (let i = 0; i < res.data.updated_at.length; i++) {
					if (i < 4) {
						this.updated_at = this.updated_at + res.data.updated_at[i]
					}
					if (i === 4) {
						this.updated_at = this.updated_at + '년 '
					}
					if (i === 5 || i === 6 ) {
						this.updated_at = this.updated_at + res.data.updated_at[i]
					}
					if (i === 7) {
						this.updated_at = this.updated_at + '월 '
					}
					if (i === 8 || i === 9 ) {
						this.updated_at = this.updated_at + res.data.updated_at[i]
					}
					if (i === 10) {
						this.updated_at = this.updated_at + '일 '
					}
					if (i < 19 && i >10) {
						this.updated_at = this.updated_at + res.data.updated_at[i]
					}
					
				}
			})
			.catch(() => {})
		},
		Like(){
			axios({
				method:'post',
				url:`${Django_API_URL}/api/v1/community/review/${this.$store.state.user_data.pk}/${this.review_article.id}/likes/`
			})
			.then((res) =>{
				this.is_liked = res.data
				this.$router.go(0)
			})
		},
		createComment(){
			const content = this.content
			const review = this.review_article.id
			axios({
				method:'post',
				url:`${Django_API_URL}/api/v1/community/review/${this.review_article.id}/comments/`,
				data:{
					content, review
				},
				headers:{
					Authorization : `Token ${this.$store.state.token}`
				}	
			})
			.then(()=>{
				this.$router.go(this.$router.currentRout).catch(() => {})
			})
			.catch(()=>{})
		},
		deleteArticle(){
			axios({
				method:'delete',
				url:`${Django_API_URL}/api/v1/community/review/${this.review_article.id}/`
			})
			.then(()=>{
				this.$router.push({name:'review'})
			})
		},
		putArticle(){
			const review = this.review_article.id
			this.$router.push({name:'moviereviewedit',params:{id:review}})
		},
		commentPutOn(a){
			if (this.put_check){
				this.put_index = null
				return this.put_check = false
			}else{
				const index = a.target.getAttribute('data')
				this.put_index = index
				return this.put_check = true
			}
		},
		commentDelete(a){
			const index = a.target.getAttribute('data')
			const comment_data = this.review_article['reviewcomment_set'][index]['id']
			axios({
				method:'delete',
				url:`${Django_API_URL}/api/v1/community/review/comment/${comment_data}/`
			})
			.then(()=>{this.$router.go(0)})
			.catch(()=>{})
		},
		commentPut(a){
			const index = a.target.getAttribute('data')
			const comment_data = this.review_article['reviewcomment_set'][index]['id']
			const content = this.new_content
			const review = this.review_article['id']
			if (!content){
				alert('변경할 내용을 입력해주세요')
				return
			}
			axios({
				method:'put',
				url:`${Django_API_URL}/api/v1/community/review/comment/${comment_data}/`,
				data:{
					content,review
				}
			})
			.then(()=>{this.$router.go(0)})
			.catch(()=>{})
		}
	}
	
}
</script>

<style scoped>
.detail {
	border-radius: 0.5rem;
	margin: auto;
	width: 1000px;
	box-shadow: 4px 4px 4px grey;
	background-color: #141414;
	margin-bottom: 15rem;
	margin-top: 5rem;
}
.articletitle {
	padding-top: 1.5rem;
	padding-left: 1.5rem;
	text-align: start;
	padding-bottom: 20px;
	border-bottom: solid grey 2px;
}
.articleContent {
	margin: auto;
	width: 95%;
	height: 400px;
	background-color: #383838;
	padding: 15px;
	text-align: start;
	border-radius: .5rem;
}
.articleTime {
	text-align: start;
}
.articleBtn {
	align-content: start;
}
div a {
	font-weight: bold;
	font-size: 20px;
	color: #ffffff;
	text-decoration-line: none;
}
.commentlist {
	text-align: start;
}
.comment {
	border-bottom: solid grey 1px;
}
.like {
	text-align: start;
	margin-top: 3px;
	padding-bottom: 25px;
	margin-left: 15px;
}
</style>