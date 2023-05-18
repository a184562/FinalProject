<template>
	<div>
		<h1>리뷰게시판 게시글 작성</h1>
		<form @submit.prevent="createReview">
			<label for="title">제목 : </label>
			<input type="text" id="title" v-model.trim="title"><br>
			<label for="content">내용 : </label>
			<textarea id="content" cols="30" rows="10" v-model.trim="content"></textarea><br>
			<label for="movie_title">영화 제목 : </label>
			<input type="text" id="movie_title" v-model.trim="movie_title"><br>
			<input type="submit" id="제출">
		</form>
	
	</div>
</template>

<script>
import axios from 'axios'
const Django_API_URL = 'http://127.0.0.1:8000'

export default {
	name: 'MovieReviewCreate',
	data() {
		return {
			title : null,
			content : null,
			movie_title : null,
		}
	},
	methods: {
		createReview() {
			const title = this.title
			const content = this.content
			const movie_title = this.movie_title

			if (!title) {
        alert('제목 입력해주세요')
        return
      } else if (!content){
        alert('내용 입력해주세요')
        return
      }

			// axios로 Django 데이터베이스 서버에 연결 후 작업
			axios({
				method: 'post',
				url: `${Django_API_URL}/api/v1/community/review/`,
				data: {title, content, movie_title}
			})
			.then(() => {
				this.$router.push({name:'review'})
			})
			.catch((err) => console.log(err))
		}
	}
}
</script>

<style>

</style>