<template>
	<div>
		<h5>{{ free_article.id }}</h5>
		<p>{{ free_article.title }}</p>
		<router-link :to="{
			name: 'FreeBoardDetail',
			params: {id: free_article.id}}">
			[DETAIL]
		</router-link>
		<hr>
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

<style>

</style>