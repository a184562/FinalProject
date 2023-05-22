<template>
	<div>
		<div class="container">
			<div @click="selectCard_left">
				<GameCard class="Card" :movie="movie_1" />
			</div>
			<div @click="selectCard_right">
				<GameCard class="Card" :movie="movie_2" />
			</div>
		</div>
		
		
		<h2>{{ score }}</h2>
	</div>
</template>

<script>
import GameCard from './GameCard.vue'


export default {
	name: 'GamePlay',
	
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
		}
	},
	created() {
		console.log(this.movie_list)
		const temp_movie_list = localStorage.getItem('movie_list')
		const parsed_temp_movie_list = JSON.parse(temp_movie_list)
		this.movie_list = parsed_temp_movie_list
		this.shuffle(this.movie_list)

		
		this.movie_1 = this.movie_list[this.idx_1]
		this.movie_2 = this.movie_list[this.idx_2]

		console.log(this.movie_1)
		console.log(this.movie_2)
	},
	methods: {
		shuffle(array) {
			array.sort(() => Math.random() -0.5)
		},
		selectCard_left() {
			if (this.movie_1.popularity > this.movie_2.popularity) {
				this.score += 1
				this.idx_1 = this.idx_2
				this.idx_2 += 1
				this.movie_1 = this.movie_list[this.idx_1]
				this.movie_2 = this.movie_list[this.idx_2]
				console.log(this.movie_1)
			}
			else {
				alert("틀렸습니다.")
				this.$router.push({name: 'entertain'})
			}
		}
		,
		selectCard_right() {
			if (this.movie_1.popularity < this.movie_2.popularity) {
				this.score += 1
				this.idx_1 = this.idx_2
				this.idx_2 += 1
				this.movie_1 = this.movie_list[this.idx_1]
				this.movie_2 = this.movie_list[this.idx_2]
				console.log(this.movie_1)
			}
			else {
				alert("틀렸습니다.")
				this.$router.push({name: 'entertain'})
			}
		}
		
	}
	
}
</script>

<style scoped>
.container {
	display: flex;
	margin: auto;
}

.Card {
	cursor: pointer;
}

</style>