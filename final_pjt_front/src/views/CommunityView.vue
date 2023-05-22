<template>
	<div id="app">
		<nav>
			<router-link to="/community/free">자유게시판</router-link> |
			<router-link to="/community/review">영화리뷰 게시판</router-link>
		</nav>
		
		
		

	</div>

</template>

<script>
export default {
	name: 'CommunityView',
	computed:{
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

</style>