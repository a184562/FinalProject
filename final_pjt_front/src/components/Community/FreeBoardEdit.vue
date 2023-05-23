<template>
	<div>
		<h1>자유게시판 게시글 수정</h1>
		<form @submit.prevent="editArticle">
			<label for="title">제목 : </label>
			<input type="text" id="title" v-model="title"><br>
			<label for="content">내용 : </label>
			<textarea id="content" cols="30" rows="10" v-model="content"></textarea><br>
			<input type="submit" id="제출">
		</form>
		
	</div>
</template>

<script>
import axios from 'axios'
const Django_API_URL = 'http://127.0.0.1:8000'
export default {
	name: 'FreeBoardEdit',
	data() {
		return {
			title : null,
			content : null,
		}
	},
	methods: {
		editArticle() {
			const title = this.title
			const content = this.content
			console.log(this.$route.params.id)
			if (!title) {
				alert('제목 입력해주세요')
				return
			} else if (!content){
				alert('내용 입력해주세요')
				return
			}
		axios({
			method:'put',
			url:`${Django_API_URL}/api/v1/community/free/${this.$route.params.id}/`,
			data:{
				title,content
			}
		})
		.then(()=>{this.$router.push({name:'freeboarddetail',params:this.$route.params.id})})
			// axios로 Django 데이터베이스 서버에 연결 후 작업
		}
	}
}
</script>

<style>

</style>