<template>
	<div>
		<!-- 검색 로직의 경우 검색 키워드가 영화의 제목에 속해있을 경우 데이터가 검색되도록 로직 설정 -->
		<form @submit.prevent="searchKeyword" class="pt-4 pb-3">
			<div class="input-group mb-3 ms-3 me-3 mt-3" style="width: 95%;">
				<span class="input-group-text">검색어</span>
				<input class="form-control" type="text" v-model.trim="searchMovieKeyword">
				<input class="btn btn-dark" type="submit" style="width: 75px;" value="검색">
			</div>
		</form>
		<hr>
		<h3>검색어 : {{ tempKeyword }}</h3>
		<div v-if="search_movie_list.length > 0">
			<div id="carouselExampleAutoplaying" class="carousel slide" data-bs-ride="carousel">
				<div class="carousel-inner">
					<div class="carousel-item active">
						<div class="container">
							<div class="row">
								<div class="col-2"
								v-for="(movie, index) in search_movie_list"	:key="index">
									<MovieCard v-show="index >= 0 && index < 6" :movie="movie" :movie_rank="index+1" class="card"/>
								</div>
							</div>
						</div>
					</div>
					<div class="carousel-item">
						<div class="container">
							<div class="row">
								<div class="col-2"
								v-for="(movie, index) in search_movie_list" :key="index">
									<MovieCard v-show="index >= 6 && index < 12" :movie="movie" :movie_rank="index+1" class="card"/>
								</div>
							</div>
						</div>
					</div>				
					<div class="carousel-item">
						<div class="container">
							<div class="row">
								<div class="col-2"
								v-for="(movie, index) in search_movie_list" :key="index">
									<MovieCard v-if="index >= 12 && index < 18" :movie="movie" :movie_rank="index+1" class="card"/>
								</div>
							</div>
						</div>
					</div>
					<div class="carousel-item">
						<div class="container">
							<div class="row">
								<div class="col-2"
								v-for="(movie, index) in search_movie_list" :key="index">
									<MovieCard v-if="index >= 18 && index < 24" :movie="movie" :movie_rank="index+1" class="card"/>
								</div>
							</div>
						</div>
					</div>
					<div class="carousel-item">
						<div class="container">
							<div class="row">
								<div class="col-2"
								v-for="(movie, index) in search_movie_list" :key="index">
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
			
		</div>
		<div v-else>
			<p class="NoData">검색결과가 없습니다.</p>
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
	// 해당 검색 기능을 만들기 위해서 사용한 데이터는 store에 저장된 전체 영화 리스트가 메인이다.
	// 이 후 키워드에 따라 검색된 영화 리스트에 넣어주고 해당 영화의 정보(포스터와 제목)를 출력
	data() {
		return {
			movie_list: this.$store.state.movie_list,
			search_movie_list: [],
			searchMovieKeyword : "",
			tempKeyword : ""
		}
	},
	methods: {
		searchKeyword() {
			this.tempKeyword = ""
			const keyword = this.searchMovieKeyword
			this.search_movie_list = []
			// 검색어를 빈 공간으로 두었을 경우 알림 출력
			if(keyword==="" | keyword === undefined) {
				alert("검색 결과가 없습니다.")
				return
			}
			// 빈공간으로 두지 않았을 경우 키워드를 바탕으로 검색
			else {
				keyword.toLowerCase()
				this.movie_list.forEach((movie) => {
					let movie_title = movie.title.toLowerCase()
					if(movie_title.indexOf(keyword) !== -1) {
						this.search_movie_list.push(movie)
					}
				})
			}
			// 이후 검색창을 다시 빈 공간으로 만들어주는 작업
			this.tempKeyword = this.searchMovieKeyword
			this.searchMovieKeyword = ""
		}
	}
}
</script>

<style scoped>
.NoData {
	font-size: 50px;
}
</style>