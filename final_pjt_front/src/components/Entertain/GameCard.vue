<template>
	<div class="card">
		<img :src="poster_URL" alt="">
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
			poster_URL: `https://www.themoviedb.org/t/p/w300_and_h450_bestv2${this.movie.poster_path}`
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