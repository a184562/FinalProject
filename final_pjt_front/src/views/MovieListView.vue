<template>
	<div>
		<div>
			<h1>Now Playing</h1>
			<NowPlaying />
		</div>
		<div>
			<h1>Genre1</h1>
			<GenreRecommend />
		</div>
		<div>
			<h1>Genre2</h1>
			<GenreRecommend />
		</div>
		<div>
			<h1>Genre3</h1>
			<GenreRecommend />
		</div>
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