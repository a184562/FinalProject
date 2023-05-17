<template>
	<div>
		<nav>
			<router-link to="/community/free">자유게시판</router-link> |
			<router-link to="/community/review">영화리뷰 게시판</router-link>
		</nav>
		<h1>자유게시판</h1>
		<FreeBoardList />
	</div>
</template>

<script>
import FreeBoardList from './FreeBoardList.vue'

export default {
	name: 'FreeBoard',
	components: {
		FreeBoardList,
	}
}
</script>

<style>

</style>