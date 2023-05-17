<template>
	<div>
		<GameCard />
		<GameCard />
	</div>
</template>

<script>
import GameCard from './GameCard.vue'
function range(num) {
	let arr = []
	for (let i = 0; i < num; i++) {
		arr.push(i)
	}
	return arr
}

function include(arr, num) {
	if (arr.includes(num)) {
		return
	} else {
		arr.push(num)
		return num
	}
}

function random_index_1() {
	const mmm = 'misu'
	return mmm
}

export default {
	name: 'GamePlay',
	components: {
		GameCard,
	},
	data() {
		return {
			movie_list: this.$route.params.movie_list,
			// random_index_1 : null,
			// random_index_2 : null,
			index_arr : range(this.movie_list.length),
			compare_arr : []
		}
	},
	created() {
		console.log(this.movie_list)
		// this.random_index_1 = Math.floor(Math.random() * this.movie_list.length)
		// this.random_index_2 = Math.floor(Math.random() * this.movie_list.length)
		include(this.compare_arr, 123)
		const min = random_index_1()
		console.log(min)

	}
}
</script>

<style>

</style>