<template>
	<div class="gameTable">
		<div class="container justify-content-around pt-5">
			<div @click="selectCard_left">
				<GameCard class="Card" :movie="movie_1" />
				<div id="rate_1" class="mt-5 rate">
					0
				</div>
			</div>
			<div @click="selectCard_right">
				<GameCard class="Card" :movie="movie_2" />
				<div id="rate_2" class="mt-5 rate">
					0
				</div>
			</div>
		</div>
		
		
		<h1 class="mt-5">점수 : {{ score }}</h1>
	</div>
</template>

<script>
import GameCard from './GameCard.vue'


export default {
	name: 'GamePlayRate',
	components: {
		GameCard,
	},
	data() {
		return {
			movie_list : null,
			movie_1: null,
			movie_2: null,
			idx_1 : 0,
			idx_2 : 1,
			score : 0,
			counting_num_1 : 0,
			counting_num_2 : 0,
		}
	},
	created() {
		// 영화 리스트 데이터를 받아오고
		const temp_movie_list = localStorage.getItem('movie_list')
		const parsed_temp_movie_list = JSON.parse(temp_movie_list)
		this.movie_list = parsed_temp_movie_list

		// 랜덤으로 섞어줌
		this.shuffle(this.movie_list)
		this.movie_1 = this.movie_list[this.idx_1]
		this.movie_2 = this.movie_list[this.idx_2]
		this.counting_num_1 = this.movie_1.vote_average
		this.counting_num_2 = this.movie_2.vote_average
	},
	methods: {
		shuffle(array) {
			array.sort(() => Math.random() -0.5)
		},
		// 왼쪽 카드를 선택시 오른쪽 카드가 왼쪽으로 이동하고 정답일 때 점수를 올려줌
		async selectCard_left() {
			this.countingNum_1(this.counting_num_1)
			this.countingNum_2(this.counting_num_2)
			setTimeout(() => {
				if (this.movie_1.vote_average > this.movie_2.vote_average) {
					this.score += 1
					this.idx_1 = this.idx_2
					this.idx_2 += 1
					this.movie_1 = this.movie_list[this.idx_1]
					this.movie_2 = this.movie_list[this.idx_2]
					this.counting_num_1 = this.movie_1.vote_average
					this.counting_num_2 = this.movie_2.vote_average
					document.querySelector("#rate_1").innerHTML = this.counting_num_1
					document.querySelector("#rate_2").innerHTML = 0
				}
				else {
					alert("틀렸습니다.")
					this.$router.push({name: 'entertain'})
				}
			}, 1000)
		},
		// 오른쪽 카드를 선택시 오른쪽 카드가 왼쪽으로 이동하고 정답일 때 점수를 올려줌
		async selectCard_right() {
			this.countingNum_1(this.counting_num_1)
			this.countingNum_2(this.counting_num_2)
			setTimeout(() => {
				if (this.movie_1.vote_average < this.movie_2.vote_average) {
					this.score += 1
					this.idx_1 = this.idx_2
					this.idx_2 += 1
					this.movie_1 = this.movie_list[this.idx_1]
					this.movie_2 = this.movie_list[this.idx_2]
					this.counting_num_1 = this.movie_1.vote_average
					this.counting_num_2 = this.movie_2.vote_average
					document.querySelector("#rate_1").innerHTML = this.counting_num_1
					document.querySelector("#rate_2").innerHTML = 0
				}
				else {
					alert("틀렸습니다.")
					this.$router.push({name: 'entertain'})
				}
			}, 1000)
		},
		// 숫자가 카운팅되도록 하는 함수
		countingNum_1(num) {
			const element = document.querySelector('#rate_1')
			if(num == 0) {
				element.innerHTML = '0'
			}
			else {
				const each = Math.ceil(num/25)
				let time = 0
			for(let i = 0; i <= num; i += each) {
				setTimeout(() => {
					element.innerHTML = i
				}, 20*time)
				if(i+each > num) {
					setTimeout(() => {
						element.innerHTML = num
					}, 20*(time+1))
				}
				time++
			}}
		},
		countingNum_2(num) {
			const element = document.querySelector('#rate_2')
			if(num == 0) {
				element.innerHTML = '0'
			}
			else {
				const each = Math.ceil(num/25)
				let time = 0
			for(let i = 0; i <= num; i += each) {
				setTimeout(() => {
					element.innerHTML = i
				}, 20*time)
				if(i+each > num) {
					setTimeout(() => {
						element.innerHTML = num
					}, 20*(time+1))
				}
				time++
			}}
		},
}}
</script>

<style scoped>
.container {
	display: flex;
	margin: auto;
	
	height: 850px;
}

.Card {
	cursor: pointer;
	border-radius: 1rem;
	background-color: #313131;
}
.gameTable {
	border-radius: 0.5rem;
	margin: auto;
	width: 1200px;
	box-shadow: 4px 4px 4px grey;
	background-color: #141414;
	margin-bottom: 15rem;
	margin-top: 5rem;
}
.rate {
	font-size: 30px;
}
</style>