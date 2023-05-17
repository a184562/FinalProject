<template>
	<div>
		<GameCard />
		<GameCard />
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
			movie_list: this.$route.params.movie_list,
			
		}
	},
	
}
</script>

<style>

</style>