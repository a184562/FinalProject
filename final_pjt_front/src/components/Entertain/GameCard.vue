<template>
	<div class="card">
		<img :src="poster(movie.poster_path)" alt="">
		<p>{{movie.title}}</p>
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
			// max_num : this.movie.popularity
		}
	},
	methods:{
		poster(path) {
			return `https://www.themoviedb.org/t/p/w300_and_h450_bestv2${path}`
		},
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