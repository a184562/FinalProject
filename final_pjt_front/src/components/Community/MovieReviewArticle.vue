<template>
	<div class="d-flex articles mt-3">
		<div class="p-2 flex-fill">
			<label for="article_num">{{ review_article.id }}. </label>
			<router-link :to="{
				name: 'reviewdetail',
				params: {id: review_article.id}}">
				[{{ review_article.movie_title }}] {{ review_article.title }}
			</router-link>
		</div>
		<div class="p-2 me-3">
			<p>작성자 : {{ review_article.username }}</p>
		</div>
		
		<hr>
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

<style scoped>
div a {
  font-weight: bold;
  color: #ffffff;
	text-decoration-line: none;
}
.articles {
	border-bottom: solid rgb(66, 66, 66) 1px;
}
</style>