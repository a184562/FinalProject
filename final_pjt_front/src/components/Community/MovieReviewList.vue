<template>
	<div>
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
	data() {
		return {
			review_articles: null,
		}
	},
	created() {
		this.getReview()
	},
	methods: {
		async getReview() {
			await this.$store.dispatch('getReview')
			this.review_articles = this.$store.state.review_articles
		}
	}
}
</script>

<style>

</style>