<template>
	<div>
		<h1>영화 리뷰 글</h1>
		<MovieReviewArticle
		v-for="review_article in review_articles"
		:key="review_article.id"
		:review_article="review_article"
		/>
	</div>
</template>

<script>
import MovieReviewArticle from './MovieReviewArticle.vue'


export default {
	name: 'MovieReviewList',
	components: {
		MovieReviewArticle,
	},
	computed: {
		review_articles() {
			return this.$store.state.review_articles
		}
	}
}
</script>

<style>

</style>