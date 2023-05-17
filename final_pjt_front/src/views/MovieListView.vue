<template>
	<div>
		<NowPlaying />
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