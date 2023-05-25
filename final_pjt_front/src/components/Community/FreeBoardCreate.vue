<template>
	<div class="detail">
		<div class="mt-5">
			<div class="articletitle pt-4">
				<h1>자유게시판 게시글 작성</h1><hr>
				<form @submit.prevent="createArticle">
					<div  style="width: 95%; margin:auto;">
						<div class="d-flex">
							<label id="title" class="form-label" for="title">제목 : </label>
						</div>
						<input class="form-control inputTitle" type="text" id="title" v-model.trim="title"><br>
						<div class="d-flex">
							<label id="content" class="form-label" for="content">내용 : </label>
						</div>
						<textarea class="form-control inputContent" id="content"  rows="10" v-model.trim="content"></textarea><br>
						<div class="d-flex">
							<input class="btn btn-dark mb-4" type="submit" value="글 작성">
							<button class="btn btn-dark ms-3 mb-4" @click="goToFree">글 쓰기 취소</button>
						</div>
						
					</div>
					
				</form>
			</div>

		</div>
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
		// userData를 보내주기 위해서 axios 사용
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
			.then(() => {
				this.$router.push({name: 'free'}).catch(() => {})
			})
			.catch(() => {})
	},
	goToFree() {
		this.$router.push({name: 'free'})
	}
}
}
</script>

<style>
.inputTitle {
	width: 750px;
	margin: auto;
}
.inputContent {
	width: 75%;
	margin: auto;
}
</style>

<style scoped>
.form-label {
	font-weight: bold;
	font-size: 20px;
}
</style>