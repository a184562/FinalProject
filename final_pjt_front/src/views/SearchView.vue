<template>
	<div>
		<label for="keyword">검색어 : </label>
		<input type="text" id="keyword" v-model.trim="searchMovieKeyword">
		<input type="submit" id="검색" @click="searchKeyword">

		<div v-if="search_movie_list !== []">
			<div v-for="(movie, index) in search_movie_list" :key="index">
				<MovieCard :movie="movie" />
			</div>
		</div>
		<div v-else>
			<h2>검색결과가 없습니다.</h2>
		</div>
	</div>
</template>

<script>
import MovieCard from '../components/Movie/MovieCard.vue'

export default {
	name: 'SearchView',
	components: {
		MovieCard
	},
	data() {
		return {
			movie_list: this.$store.state.movie_list,
			search_movie_list: [],
			searchMovieKeyword : "",
		}
	},
	methods: {
		searchKeyword() {
			const keyword = this.searchMovieKeyword
			this.search_movie_list = []

			if(keyword==="" | keyword === undefined) {
				alert("검색 결과가 없습니다.")
				return
			}
			else {
				keyword.toLowerCase()
				this.movie_list.forEach((movie) => {
					let movie_title = movie.title.toLowerCase()
					if(movie_title.indexOf(keyword) !== -1) {
						this.search_movie_list.push(movie)
					}
				})
			}
			
			console.log(this.search_movie_list)
			console.log(this.searchMovieKeyword)
		}
	}
}
</script>

<style>

</style>