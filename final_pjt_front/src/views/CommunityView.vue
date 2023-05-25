<template>
	<div>
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
	</div>

</template>

<script>
export default {
	name: 'CommunityView',
	computed:{
		// 로그인이 되어 있어야만 접속할 수 있도록 처리
		isLogin(){
			return this.$store.getters.isLogin
		}
	},
	created(){
		this.getArticles()
	},
	methods:{
		getArticles(){
			if (this.isLogin){
				this.$store.dispatch('getArticle')
			}else{
				alert('로그인이 필요한 서비스 입니다.')
				this.$router.push({name:'login'})
			}
		}
	}
}
</script>

<style>
.board {
	background-color: #141414;
	color: white;
	width: 150px;
	height: 165px;
	border-radius: 1rem;
}
.menu {
	padding-top: 15px;
	padding-bottom: 5px;
	border-top-left-radius: 1rem;
	border-top-right-radius: 1rem;
	background-color: #2e2e2e;
	border-bottom: solid grey 1px;
	/* background-color: #444444; */
}
div a {
  font-weight: bold;
  color: #E50914;
	text-decoration-line: none;
}

div a.router-link-exact-active {
  color: #ffffff;
	text-decoration-line: none;
}

.freeboardSelect {
	margin-top: 15px;
	padding-bottom: 10px;
	border-bottom: solid grey 1px;
}
.reviewboardSelect {
	margin-top: 15px;
}
</style>