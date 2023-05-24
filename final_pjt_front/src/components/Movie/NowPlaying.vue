<template>
	<div id="carouselExampleAutoplaying" class="carousel slide" data-bs-ride="carousel">
		<div class="carousel-inner">
			<div class="carousel-item active">
				<div class="container">
					<div class="row">
						<div class="col-2"
						v-for="(movie, index) in nowplaying_movies"	:key="index">
							<MovieCard v-if="index >= 0 && index < 6" :movie="movie" :movie_rank="index+1" class="card"/>
						</div>
					</div>
				</div>
			</div>
			<div class="carousel-item">
				<div class="container">
					<div class="row">
						<div class="col-2"
						v-for="(movie, index) in nowplaying_movies" :key="index">
							<MovieCard v-if="index >= 6 && index < 12" :movie="movie" :movie_rank="index+1" class="card"/>
						</div>
					</div>
				</div>
			</div>				
			<div class="carousel-item">
				<div class="container">
					<div class="row">
						<div class="col-2"
						v-for="(movie, index) in nowplaying_movies" :key="index">
							<MovieCard v-if="index >= 12 && index < 18" :movie="movie" :movie_rank="index+1" class="card"/>
						</div>
					</div>
				</div>
			</div>
			<div class="carousel-item">
				<div class="container">
					<div class="row">
						<div class="col-2"
						v-for="(movie, index) in nowplaying_movies" :key="index">
							<MovieCard v-if="index >= 18 && index < 24" :movie="movie" :movie_rank="index+1" class="card"/>
						</div>
					</div>
				</div>
			</div>
			<div class="carousel-item">
				<div class="container">
					<div class="row">
						<div class="col-2"
						v-for="(movie, index) in nowplaying_movies" :key="index">
							<MovieCard v-if="index >= 24" :movie="movie" :movie_rank="index+1" class="card"/>
						</div>
					</div>
				</div>
			</div>
		</div>
		<button class="carousel-control-prev" type="button" data-bs-target="#carouselExampleAutoplaying" data-bs-slide="prev">
			<span class="carousel-control-prev-icon" aria-hidden="true"></span>
			<span class="visually-hidden">Previous</span>
		</button>
		<button class="carousel-control-next" type="button" data-bs-target="#carouselExampleAutoplaying" data-bs-slide="next">
			<span class="carousel-control-next-icon" aria-hidden="true"></span>
			<span class="visually-hidden">Next</span>
		</button>
	</div>
	
</template>

<script>
import MovieCard from './MovieCard.vue'
// import axios from 'axios'

// const API_KEY = process.env.VUE_APP_MOVIE_API_KEY
// const nowplaying_URL = `https://api.themoviedb.org/3/discover/movie?include_adult=false&include_video=false&language=en-US&page=1&sort_by=popularity.desc&with_release_type=2|3&release_date.gte=2023-03-16&release_date.lte=2023-05-03&api_key=${API_KEY}`



export default {
	name: 'NowPlaying',
	components: {
		MovieCard,
	},
	props: {
		nowplaying_movies: Array,
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