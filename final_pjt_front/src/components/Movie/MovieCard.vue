<template>
	<div class="card" @click="GoToMovieDetail">
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
	methods: {
		GoToMovieDetail() {
			this.$router.push({
				name: 'movie',
				params:{movie_id : this.movie.id}
			})
		}
	}
}
</script>

<style scoped>
.card {
	border: solid black 2px;
	cursor: pointer;
	border-radius: 0.5rem;
	height: 25rem;
	margin: 2px;
}
img {
	width: 80%;
	height: 50%;
}
</style>