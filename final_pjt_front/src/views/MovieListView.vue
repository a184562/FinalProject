<template>
	<div>
		<NowPlaying />
		<h1>123456478979416545</h1>
		<GenreRecommend />
	</div>
</template>

<script>
import GenreRecommend from '../components/Movie/GenreRecommend.vue'
import NowPlaying from '../components/Movie/NowPlaying.vue'


export default {
	name: 'MovieListView',
	components: {
		NowPlaying,
		GenreRecommend,
	}
}
</script>

<style>

</style>