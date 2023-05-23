<template>
	<div class="d-flex flex-row">
		<div class="board mt-3 ms-3">
			<div class="menu">
				<h3>BOARD</h3>
			</div>
			<div class="freeboardSelect">
				<router-link to="/community/free">자유게시판</router-link>
			</div>
			<div class="reviewboardSelect">
				<router-link to="/community/review">리뷰 게시판</router-link>
			</div>	
		</div>
		<div class="ArticleBoard mt-3 ms-3 me-2">
			<h1 class="boardTitle">리뷰 게시판</h1>
			<div>
				<MovieReviewList class="ms-3" />
				<button class="btn btn-secondary mt-3 ms-3 mb-3" @click="gotoReviewCreate">글쓰기</button>
			</div>
		</div>
		
	</div>
</template>

<script>
import MovieReviewList from './MovieReviewList.vue'

export default {
	name : 'MovieReview',
	components: {
		MovieReviewList,
	},
	created() {
		this.getReview()
	},
	methods: {
		getReview() {
			this.$store.dispatch('getReview')
		},
		gotoReviewCreate() {
			this.$router.push({name: 'reviewcreate'})
		}
	}
}
</script>

<style>

</style>