<template>
	<div>
		<h1>자유게시판 게시글 작성</h1>
		<form @submit.prevent="createArticle">
			<label for="title">제목 : </label>
			<input type="text" id="title"><br>
			<label for="content">내용 : </label>
			<textarea id="content" cols="30" rows="10"></textarea><br>
			<input type="submit" id="제출">
		</form>
		
	</div>
</template>

<script>
export default {
	name: 'FreeBoardCreate',
	data() {
		return {
			title : null,
			content : null,
		}
	},
	methods: {
		createArticle() {
			const title = this.title
			const content = this.content

			if (!title) {
        alert('제목 입력해주세요')
        return
      } else if (!content){
        alert('내용 입력해주세요')
        return
      }

			// axios로 Django 데이터베이스 서버에 연결 후 작업
		}
	}
}
</script>

<style>

</style>