<template>
	<div>
		<nav>
			<router-link to="/community/free">자유게시판</router-link> |
			<router-link to="/community/review">리뷰 게시판</router-link>
		</nav>
		<h1>리뷰 게시판</h1>
		<MovieReviewList />
		<button @click="gotoReviewCreate">글쓰기</button>
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