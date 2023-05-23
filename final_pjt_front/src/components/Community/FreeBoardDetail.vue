<template>
	<div class="detail">
		<div class="mt-5">
			<div class="articletitle d-flex justify-content-between">
				<h1>{{ free_article?.title }}</h1>
				<div class="me-4 mt-4">
					<label for="profile">작성자</label> :
					<router-link :to="{
						name: 'otherprofile',
						params: {id: free_article?.user, username: free_article?.username}
					}">{{free_article?.username}}</router-link>
				</div>
			</div>
			
			<div class="articleContent mt-4">
				<p>{{ free_article?.content }}</p>
			</div>
			<div class="articleTime mt-4 ms-4">
				<p>작성시간 : {{ created_at }}</p>
				<p>수정시간 : {{ updated_at}}</p>
			</div>
		</div>
		
		<div v-if="free_article?.user==user_id" class="articleBtn d-flex mt-4">
			<button class="btn btn-dark ms-3" @click="$router.push({name:'free'})">목록으로</button>
			<button class="btn btn-dark ms-3" @click="putArticle">게시글 수정</button>
			<button class="btn btn-dark ms-3" @click="deleteArticle">게시글 삭제</button>
		</div>
		<div v-else class="articleBtn d-flex mt-4">
			<button class="btn btn-dark ms-3" @click="$router.push({name:'free'})">목록으로</button>
		</div>
		
		<div class="d-flex ms-3 mt-3">
			<button class="btn btn-dark" v-if="!is_liked" @click="Like" >좋아요</button>
			<button class="btn btn-dark" v-else @click="Like">좋아요 취소</button>
		</div>
		<form @submit.prevent="createComment" class="pb-3">
			<div class="input-group mb-3 ms-3 me-3 mt-3" style="width: 95%;">
			<span class="input-group-text">댓글</span>
			<input class="form-control" type="text" v-model="content">
			<input class="btn btn-dark" type="submit" style="width: 75px;" value="작성">
		</div>
		</form>
		
		
		<div>
			<p>댓글 수 : {{ free_article['comment_set'].length }}</p>
			<ul v-for="(contents,index) in free_article['comment_set']" :key="index" class="commentlist">
				<li v-if="contents['user']==user_id" class="comment">
					<div class="me-4 mt-4">
						<router-link :to="{
							name: 'otherprofile',
							params: {id: free_article?.user, username: free_article?.username}
						}">{{contents['username']}}</router-link>
					</div>
					<div class="d-flex justify-content-between mt-3">
						<p>{{contents['content']}}</p>
						<p class="me-5">{{contents['created_at']}}</p>
					</div>
					<div class="pb-4">
						<button class="btn btn-dark btn-sm me-2" type="submit" value="댓글 수정"  @click="commentPutOn" :data="index">댓글 수정</button>
						<button class="btn btn-dark btn-sm" type="submit" value="댓글 삭제"  @click="commentDelete" :data="index">댓글 삭제</button>
						<form @submit.prevent="commentPut" class="pb-3" v-if="put_check" :data="index">
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
							params: {id: free_article?.user, username: free_article?.username}
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

// is_liked 처음 들어왔을 때, user에 따라 false, true 구현
export default {
	name: "FreeBoardDetail",
	data() {
		return {
			user_id : this.$store.state.user_data.pk,
			free_article: null,
			is_liked : false,
			content : '',
			created_at : "",
			updated_at : "",
			new_content : "",
			put_check : false,
		}
	},
	// axios로 Django 데이터베이스 서버에 연결 후 작업
	created() {
		this.getArticleDetail()
	},
	methods: {
		getArticleDetail() {
			axios({
				method: 'get',
				url: `${Django_API_URL}/api/v1/community/free/${this.$route.params.id}/`,
			})
			.then((res) => {
				console.log(res)
				this.free_article = res.data
				console.log(res.data.created_at)
				for (let i = 0; i < res.data.created_at.length; i++) {
					console.log(res.data.created_at[i])
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
					console.log(this.created_at)
					
				}
				for (let i = 0; i < res.data.updated_at.length; i++) {
					console.log(res.data.updated_at[i])
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
					console.log(this.created_at_Time)
					
				}
				// this.created_at = res.data.created_at
				// this.updated_at = res.data.updated_at
			})
			.catch((err) => console.log(err))
		},
		
		Like() {
			console.log(this.user_id)
			axios({
				method: 'post',
				url: `${Django_API_URL}/api/v1/community/free/${this.$store.state.user_data.pk}/${this.free_article.id}/likes/`,

			})
			.then((res) => {
				this.is_liked=res.data})
			.catch((err) => console.log(err))
		},
		createComment(){
			const content = this.content
			const article = this.free_article.id
			axios({
				method:'post',
				url:`${Django_API_URL}/api/v1/community/free/${this.free_article.id}/comments/`,
				data:{
					content, article
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
				url:`${Django_API_URL}/api/v1/community/free/${this.free_article.id}/`
			})
			.then((res) => {
				console.log(res)
				this.$router.go(0)
			})
		},
		putArticle(){
			const article_id = this.free_article.id
			this.$router.push({
				name: 'FreeBoardEdit',
				params:{id : article_id},
			})
		},
		commentPutOn(){
			if (this.put_check){
				return this.put_check = false
			}else{
				return this.put_check = true
			}
		},
		commentDelete(a){
			const index = a.target.getAttribute('data')
			const comment_data = this.free_article['comment_set'][index]['id']

			axios({
				method:'delete',
				url:`${Django_API_URL}/api/v1/community/free/comment/${comment_data}/`
			})
			.then(()=>{this.$router.go(0)})
			.catch(()=>{})
			
		},
		commentPut(a){
			const index = a.target.getAttribute('data')
			const comment_data = this.free_article['comment_set'][index]['id']
			const content = this.new_content
			const article = this.free_article['id']
			if (!content){
				alert('변경할 내용을 입력해주세요')
				return
			}
			axios({
				method:'put',
				url:`${Django_API_URL}/api/v1/community/free/comment/${comment_data}/`,
				data:{
					content,article
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
	/* height: 75%; */
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
</style>