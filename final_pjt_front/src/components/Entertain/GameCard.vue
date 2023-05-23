<template>
	<div class="card">
		<img class="gameimg" :src="poster(movie.poster_path)" alt="">
		<div class="mt-3 align-middle">
			<p class="pt-3">{{movie.title}}</p>
		</div>
		
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

<style scoped>
.card {
	display: flex;
	border: solid black 2px;
	width: 400px;
	font-size: 20px;
	font-weight: bold;
	background-color: #000000;
	height: 700px;
}
.gameimg {
	border-top-left-radius: 1rem;
	border-top-right-radius: 1rem;
	
}
</style>