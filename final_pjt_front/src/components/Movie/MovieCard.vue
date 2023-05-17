<template>
	<div class="card">
		<img :src="poster_URL" alt="">
		<h2>{{ movie.title }}</h2>
	</div>
</template>

<script>
export default {
	name: 'MovieCard',
	props: {
		movie: Object,
	},
	data() {
		return {
			poster_URL: `https://www.themoviedb.org/t/p/w300_and_h450_bestv2${this.movie.poster_path}`
		}
	},
	
}
</script>

<style scoped>
.card {
	border: solid black 2px;
}

img {
	width: 300px;
	height: 450px;
}
</style>