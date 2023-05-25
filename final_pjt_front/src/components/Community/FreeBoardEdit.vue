<template>
	<div class="detail">
		<div class="mt-5">
			<div class="articletitle pt-4">
				<h1>자유게시판 게시글 수정</h1><hr>
				<form @submit.prevent="editArticle">
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
							<button class="btn btn-dark ms-3 mb-4" @click="editArticle">수정 취소</button>
						</div>
					</div>
				</form>
			</div>
		</div>
	</div>
</template>

<script>
// 현재 로그인한 유저의 데이터가 필요하므로 axios 사용
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
		}
	}
}
</script>

<style>

</style>