<template>
	<div>
		<nav>
			<router-link to="/community/free">자유게시판</router-link> |
			<router-link to="/community/review">영화리뷰 게시판</router-link>
		</nav>
		<h1>영화리뷰 게시판</h1>
		<MovieReviewList />
	</div>
</template>

<script>
import MovieReviewList from './MovieReviewList.vue'

export default {
	name : 'MovieReview',
	components: {
		MovieReviewList,
	}
}
</script>

<style>

</style>