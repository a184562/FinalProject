<template>
	<div class="d-flex flex-row">
		<div class="board mt-3 ms-3">
			<div class="menu">
				<h3>BOARD</h3>
			</div>
			<div class="freeboardSelect">
				<router-link to="/community/free">자유게시판</router-link>
			</div>
			<div class="reviewboardSelect">
				<router-link to="/community/review">리뷰 게시판</router-link>
			</div>	
		</div>
		<div class="ArticleBoard mt-3 ms-3 me-2">
			<h1 class="boardTitle">자유게시판</h1>
			<div>
				<FreeBoardList class="ms-3" />
				<button class="btn btn-secondary mt-3 ms-3 mb-3" @click="gotoCreate">글쓰기</button>
			</div>
		</div>
		
	</div>
</template>

<script>
import FreeBoardList from './FreeBoardList.vue'

export default {
	name: 'FreeBoard',
	components: {
		FreeBoardList,
	},
	
	created() {
		this.getArticle()
	},
	methods: {
		getArticle() {
			this.$store.dispatch('getArticle')
			
		},
		gotoCreate() {
			this.$router.push({name: 'freecreate'})
		}
	}
}
</script>

<style>
.ArticleBoard {
	border: solid white 1px;
	border-radius: 1rem;
	width: 80%;
	text-align: start;
}

.boardTitle{
	text-align: start;
	margin: 15px;
	padding-bottom: 10px;
	border-bottom: solid grey 2px;
}
</style>