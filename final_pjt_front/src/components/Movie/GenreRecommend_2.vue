<template>
	<div id="carouselExampleAutoplaying_2" class="carousel slide" data-bs-ride="carousel">

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
		<button class="carousel-control-prev" type="button" data-bs-target="#carouselExampleAutoplaying_2" data-bs-slide="prev">
			<span class="carousel-control-prev-icon" aria-hidden="true"></span>
			<span class="visually-hidden">Previous</span>
		</button>
		<button class="carousel-control-next" type="button" data-bs-target="#carouselExampleAutoplaying_2" data-bs-slide="next">
			<span class="carousel-control-next-icon" aria-hidden="true"></span>
			<span class="visually-hidden">Next</span>
		</button>
	</div>
</template>

<script>
import MovieCard from './MovieCard.vue'

export default {
	name: 'GenreRecommend2',
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