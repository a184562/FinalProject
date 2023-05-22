<template>
	<div>
		<h1>Detail</h1>
		<p>글 번호 : {{ free_article?.id }}</p>
		<p>글 제목 : {{ free_article?.title }}</p>
		<p>내용 : {{ free_article?.content }}</p>
		<p>작성시간 : {{ free_article?.created_at }}</p>
		<p>수정시간 : {{ free_article?.updated_at }}</p>
		<button v-if="!is_liked" @click="Like" >좋아요</button>
		<button v-else @click="Like">좋아요 취소</button>
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
			free_article: null,
			is_liked : false,
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
			axios({
				method: 'post',
				url: `${Django_API_URL}/api/v1/community/free/${this.$store.state.user_id}/${this.free_article.id}/likes/`,

			})
			.then((res) => {
				this.is_liked=res.data})
			.catch((err) => console.log(err))
		}
	}
}
</script>

<style>

</style>