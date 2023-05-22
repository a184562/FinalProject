<template>
	<div>
		<h1>리뷰게시판 게시글 수정</h1>
		<form @submit.prevent="createArticle">
			<label for="title">제목 : </label>
			<input type="text" id="title"><br>
			<label for="content">내용 : </label>
			<textarea id="content" cols="30" rows="10"></textarea><br>
			<label for="movie_title">영화 제목 : </label>
			<input type="text" id="movie_title"><br>
			<input type="submit" id="제출">
		</form>
	</div>
</template>

<script>
export default {
	name: 'MovieReviewEdit',
	data() {
		return {
			title : null,
			content : null,
			movie_title : null,
		}
	},
	methods: {
		editArticle() {
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
				url: `${Django_API_URL}/api/v1/community/free/`,
				data: {title, content}
			})
			.then(() => {
				this.$router.push({name:'free'})
			})
			.catch((err) => console.log(err))
		}
	}
}
</script>

<style>

</style>