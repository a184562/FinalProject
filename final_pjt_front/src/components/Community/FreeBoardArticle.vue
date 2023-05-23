<template>
	<div class="d-flex articles mt-3">
		<div class="p-2 flex-fill">
			<label for="article_num">{{ free_article.id }}. </label>
			<router-link :to="{
				name: 'freeboarddetail',
				params: {id: free_article.id}}">
				{{ free_article.title }}
			</router-link>
		</div>
		<div class="p-2 me-3">
			<p>작성자 : {{ free_article.username }}</p>
		</div>
	</div>
</template>

<script>
export default {
	name: 'FreeBoardArticle',
	props: {
		free_article: Object,
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