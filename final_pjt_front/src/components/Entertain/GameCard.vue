<template>
	<div class="card">
		<img :src="poster(movie.poster_path)" alt="">
		<p>{{movie.title}}</p>
		<p>{{ movie.popularity }}</p>
	</div>
</template>

<script>
export default {
	name: 'GameCard',
	props: {
		movie: Object,
	},
	data() {
		return {
			// poster_URL: `https://www.themoviedb.org/t/p/w300_and_h450_bestv2${this.movie.poster_path}`
		}
	},
	methods:{
		poster(path) {
			return `https://www.themoviedb.org/t/p/w300_and_h450_bestv2${path}`
		}
	}
}
</script>

<style>
.card {
	border: solid black 2px;
	width: 300px;
	height: 1500px;
}
</style>