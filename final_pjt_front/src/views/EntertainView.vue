<template>
	<div class="detail mt-5 pt-3 ps-3 pe-3 pb-3">
		<div class="mt-4">
			<button class="btn btn-dark" @click="gotoGame">더 많이</button>
			<button class="btn btn-dark ms-3" @click="gotoGameDate">더 먼저</button>
			<button class="btn btn-dark ms-3" @click="gotoGameRate">더 높은</button>
		</div>
		
		<div class="mt-3 mb-3 pt-5 pb-5 script">
			<h4 class="mb-3">
				원하는 주제의 위 버튼을 누를 시
			</h4>
			<h4 class="mb-3">
				게임을 시작하실 수 있습니다.
			</h4>
			<h4>
				게임 방법은 영화의 포스터와 제목을 보고
			</h4>
			<h4 class="mb-3">
				[더 많이 본/더 먼저 나온/더 높은 평정을 받은]
			</h4>
			<h4 class="mb-3">
				영화를 찾으면 되는 간단한 게임입니다.
			</h4>
		</div>
	</div>
</template>

<script>
// 각각 원하는 게임을 하는 페이지로 넘어가도록 보내주는 경로 함수
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
		gotoGameDate() {
			return this.$router.push({name: 'gamedate'})
		},
		gotoGameRate() {
			return this.$router.push({name: 'gamerate'})
		},
	}
}
</script>

<style scoped>
.detail {
	margin: auto;
}
.btn {
	width: 15rem;
	height: 5rem;
	font-size: 35px;
}
.script {
	border-radius: 1rem;
	background-color: #1b1b1b;
	width: 50rem;
	margin: auto;
}
</style>