<template>
	<div>
		<input type="submit" @click="gotoGame" value="게임시작">
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

<style>

</style>