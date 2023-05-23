<template>
	<div>
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
	data() {
		return {
			free_articles: null,
		}
	},
	created() {
		this.getFreeArticle()
	},
	methods: {
		async getFreeArticle() {
			await this.$store.dispatch('getArticle')
			this.free_articles = this.$store.state.free_articles
		}
	}
}
</script>

<style>

</style>