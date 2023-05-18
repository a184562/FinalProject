<template>
	<div>
		<h5>{{ review_article.id }}</h5>
		<p>{{ review_article.title }}</p>
		<router-link :to="{
			name: 'MovieReviewDetail',
			params: {id: review_article.id}}">
			[DETAIL]
		</router-link>
	</div>
</template>

<script>
export default {
	name: 'MovieReviewArticle',
	props: {
		review_article: Object,
	}
}
</script>

<style>

</style>