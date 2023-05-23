<template>
	<div>
		<h1>Detail</h1>
		<p>글 번호 : {{ free_article?.id }}</p>
		<p>글 제목 : {{ free_article?.title }}</p>
		<p>내용 : {{ free_article?.content }}</p>
		<p>작성시간 : {{ free_article?.created_at }}</p>
		<p>수정시간 : {{ free_article?.updated_at}}</p>
		<div v-if="free_article?.user==user_id">
			<input type="submit" value="게시글 삭제" @click="deleteArticle">
			<input type="submit" value="게시글 수정" @click="putArticle">
		</div>
		<div>
			<label for="profile">작성자 : </label>
			<router-link :to="{
				name: 'otherprofile',
				params: {id: free_article?.user, username: free_article?.username}
			}">{{free_article?.username}}</router-link>
		</div>
		<div>
		<button v-if="!is_liked" @click="Like" >좋아요</button>
		<button v-else @click="Like">좋아요 취소</button>
		</div>
		<div>
			<form @submit.prevent="createComment">
				<label for="content">내용</label>
				<input type="text" v-model="content">
				<input type="submit" id="제출">
			</form>			
		</div>
		<div>
		<div v-for="(contents,index) in free_article['comment_set']" :key="index">
			<div v-if="contents['user']==user_id">
			{{contents['content']}}
			{{contents['username']}}
			{{contents['created_at']}}
			<input type="submit" value="댓글 삭제" @click="commentDelete">
			<input type="submit" value="댓글 수정" @click="commentPut">
			</div>
			<div v-else>
			{{contents['content']}}
			{{contents['username']}}
			{{contents['created_at']}}
			</div>
		</div>
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
				this.$router.push({name: 'free'}).catch(() => {})
			})
		},
		putArticle(){
			this.$router.push({name:'free'})
		},
		commentDelete(a){
			console.log(a)
			// axios({
			// 	method:'delete',
			// 	url:`${Django_API_URL}/api/v1/community/review/comment/${this.free_article.comment_set.}/`
			// })
		},
		commentPut(){

		}
	}
}
</script>

<style>

</style>