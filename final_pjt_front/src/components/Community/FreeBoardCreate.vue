<template>
	<div>
		<h1>자유게시판 게시글 작성</h1>
		<form @submit.prevent="createArticle">
			<label for="title">제목 : </label>
			<input type="text" id="title" v-model.trim="title"><br>
			<label for="content">내용 : </label>
			<textarea id="content" cols="30" rows="10" v-model.trim="content"></textarea><br>
			<input type="submit" id="제출">
		</form>
		
	</div>
</template>

<script>
import axios from 'axios'

const Django_API_URL = 'http://127.0.0.1:8000'


export default {
	name: 'FreeBoardCreate',
	data() {
		return {
			title : "",
			content : "",
		}
	},
	methods: {
		createArticle() {
			const title = this.title
			const content = this.content

			if(this.title=="") {
				alert('제목을 입력하세요')
				return
			}
			else if (this.content == "") {
				alert('내용을 입력하세요')
				return
			}
			
			
			axios({
				method: 'post',
				url: `${Django_API_URL}/api/v1/community/free/`,
				data: {
					title, content,
				},
				headers:{
						Authorization : `Token ${this.$store.state.token}`
					}
			})
			.then((res) => {
				console.log(res)
				this.$router.push({name: 'free'}).catch(() => {})
			})
			.catch((err) => console.log(err))

	}
}
}
</script>

<style>

</style>