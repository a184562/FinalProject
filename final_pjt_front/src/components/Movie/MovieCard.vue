<template>
	
	<div v-if="movie.title" class="card my-2" @click="GoToMovieDetail">
		<p>{{ movie_rank }}</p>
		<img :src="poster_URL" alt="" class="card-img-top">
		<div class="card-body">
			<p>{{ movie.title }}</p>
		</div>
	</div>
	<div v-else class="card my-2" @click="GoToMovieDetail">
		<p>[No Data]</p>
		<img src="../../assets/logo.png" alt="" class="card-img-top">
		<div class="card-body">
			<p>[No Data]</p>
		</div>
	</div>
</template>

<script>
export default {
	name: 'MovieCard',
	props: {
		movie: Object,
		movie_rank: Number,
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
	cursor: pointer;
	height: 450px;
	width: 200px;
	background-color: #0c0c0c;
	box-shadow: 4px 4px 4px rgb(54, 54, 54);
}

</style>