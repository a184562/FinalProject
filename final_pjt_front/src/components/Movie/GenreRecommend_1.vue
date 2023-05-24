<template>
	<div id="carouselExampleAutoplaying_1" class="carousel slide" data-bs-ride="carousel">
		<div class="carousel-inner">
			<div class="carousel-item active">
				<div class="container">
					<div class="row">
						<div class="col-2"
						v-for="(movie, index) in genre"	:key="index">
							<MovieCard v-if="index >= 0 && index < 6" :movie="movie" :movie_rank="index+1" class="card"/>
						</div>
					</div>
				</div>
			</div>
			<div class="carousel-item">
				<div class="container">
					<div class="row">
						<div class="col-2"
						v-for="(movie, index) in genre" :key="index">
							<MovieCard v-if="index >= 6 && index < 12" :movie="movie" :movie_rank="index+1" class="card"/>
						</div>
					</div>
				</div>
			</div>				
		</div>
		<button class="carousel-control-prev" type="button" data-bs-target="#carouselExampleAutoplaying_1" data-bs-slide="prev">
			<span class="carousel-control-prev-icon" aria-hidden="true"></span>
			<span class="visually-hidden">Previous</span>
		</button>
		<button class="carousel-control-next" type="button" data-bs-target="#carouselExampleAutoplaying_1" data-bs-slide="next">
			<span class="carousel-control-next-icon" aria-hidden="true"></span>
			<span class="visually-hidden">Next</span>
		</button>
	</div>
</template>

<script>
import MovieCard from './MovieCard.vue'
// import axios from 'axios'

// const API_KEY = process.env.VUE_APP_MOVIE_API_KEY
// const movies_URL = `https://api.themoviedb.org/3/discover/movie?include_adult=false&include_video=false&language=en-US&page=1&sort_by=popularity.desc&api_key=${API_KEY}`

export default {
	name: 'GenreRecommend1',
	components: {
		MovieCard,
	},
	props: {
		genre: Array,
	},
	
}
</script>

<style scoped>
.carousel {
	height: 466px;
}
.container {
	display: flex;
	flex-wrap: wrap;
}

</style>