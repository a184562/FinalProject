<template>
	<div>
		<h3>자유게시판 글</h3>
		<FreeBoardArticle 
		v-for="free_article in free_articles" 
		:key="free_article.id"
		:free_article="free_article"
		/>
	</div>
</template>

<script>
import FreeBoardArticle from './FreeBoardArticle.vue'


export default {
	name: 'FreeBoardList',
	
	components: {
		FreeBoardArticle,
	},
	// computed: {
	// 	free_articles() {
	// 		return this.$store.state.free_articles
	// 	}
	// },
	data() {
		return {
			free_articles: this.$store.state.free_articles
		}
		
	}
}
</script>

<style>

</style>