<template>
	<div>
		<h1>Detail</h1>
		<p>글 번호 : {{ review_article?.id }}</p>
		<p>글 제목 : {{ review_article?.title }}</p>
		<p>내용 : {{ review_article?.content }}</p>
		<p>작성시간 : {{ review_article?.created_at }}</p>
		<p>수정시간 : {{ review_article?.updated_at }}</p>
		<p>작성자 : {{review_article?.username}}</p>
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
			{{review_article}}
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
			review_article: null,
			is_liked :false,
			content : '',
		}
	},
	// axios로 Django 데이터베이스 서버에 연결 후 작업
	created() {
		this.getReviewDetail()
	},
	methods: {
		getReviewDetail() {
			axios({
				method: 'get',
				url: `${Django_API_URL}/api/v1/community/review/${this.$route.params.id}/`,
			})
			.then((res) => {
				console.log(res)
				this.review_article = res.data
			})
			.catch((err) => console.log(err))
		},
		Like(){
			axios({
				method:'post',
				url:`${Django_API_URL}/api/v1/community/review/${this.$store.state.user_data.pk}/${this.review_article.id}/likes/`
			})
			.then((res) =>{
				this.is_liked = res.data
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
		}	
	}
	
}
</script>

<style>

</style>