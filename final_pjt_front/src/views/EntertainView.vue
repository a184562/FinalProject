<template>
	<div class="gamestart">
		<button class="btn btn-secondary" @click="gotoGame">Game Start</button>
		<div class="pt-5">
			<h3 class="mt-5">이 게임은 화면에 뜨는 두 영화 가운데 관객수가 더 많은 영화를 찾는 게임입니다.</h3>
			<h3 class="mt-5">영화의 관객수 기준은 TMDB 데이터베이스의 popularity를 기준으로 합니다.</h3>
			<h3 class="mt-5">맞추면 화면 아래의 점수가 올라갑니다.</h3>
			
		</div>
	</div>
</template>

<script>
export default {
	name: 'EntertainView',
	data() {
		return {
			movie_list: this.$store.state.movie_list,
		}
	},
	
	methods: {
		gotoGame() {
			return this.$router.push({name: 'game'})
		},
		
	}
	
}
</script>

<style scoped>
.gamestart {
	margin: 10rem;
}
.btn {
	width: 700px;
	height: 150px;
	font-size: 50px;
}
</style>