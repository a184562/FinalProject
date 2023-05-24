<template>
	<div class="detail">
		<div class="mt-5">
			<div class="articletitle pt-4">
				<h1>리뷰게시판 게시글 작성</h1><hr>
				<form @submit.prevent="createReview">
					<div  style="width: 95%; margin:auto;">
						<div class="d-flex">
							<label id="movie_title" class="form-label" for="movie_title">영화 제목 : </label>
						</div>
						<input class="form-control inputTitle" type="text" id="title" v-model.trim="movie_title"><br>
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
							<button class="btn btn-dark ms-3 mb-4" @click="goToReview">글 쓰기 취소</button>
						</div>
						
					</div>
					
				</form>
			</div>

		</div>
	</div>
	<!-- <div>
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
	
	</div> -->
</template>

<script>
import axios from 'axios'

const Django_API_URL = 'http://127.0.0.1:8000'

export default {
	name: 'MovieReviewCreate',
	data() {
		return {
			title : "",
			content : "",
			movie_title : "",
		}
	},
	methods: {
		createReview() {
			const title = this.title
			const content = this.content
			const movie_title = this.movie_title

			if(this.title=="") {
				alert('제목을 입력하세요')
				return
			}
			else if (this.content == "") {
				alert('내용을 입력하세요')
				return
			}
			else if (this.movie_title == "") {
				alert('영화제목을 입력하세요')
				return
			}
			else {
				this.$router.push({name: 'review'})
			}

			axios({
				method: 'post',
				url: `${Django_API_URL}/api/v1/community/review/`,
				data: {
					title, content, movie_title
				},
				headers:{
						Authorization : `Token ${this.$store.state.token}`
					}
			})
			.then(() => {
				this.$router.push({name: 'review'}).catch(() => {})
			})
			.catch((err) => console.log(err))
		},
		goToReview() {
			this.$router.push({name:'review'})
		}
	}
}

</script>

<style>

</style>