<template>
  <div class="detail">
    <div class="mt-5">
      <div class="userName">
        <h1>{{ user_data.username }}</h1>
      </div>
      <div class="userContent mt-4">
        <h3 class="ms-1">e-mail : {{ user_data.email }}</h3><br>
        <!-- <h3 class="ms-1">name : {{ user_data.last_name }}{{ user_data.first_name }}</h3><br> -->
				<div class="d-flex">
					<h3>선호 장르 : </h3>
					<div v-for="(genre,index) in genre_data" :key="index" class="ms-3">
						<h3>{{genre}}</h3>
					</div>
				</div>
        <h5 class="mt-3 mb-4">팔로잉 : {{ user_data.followings.length}}명</h5>
        <h5>팔로워 : {{ user_data.followers.length}}명</h5>
      </div>
    </div>
		<br>
  </div>
</template>

<script>
// 유저의 정보는 프로필 페이지가 자신의 프로필인지 다른 유저의 프로필인지에 따라 달라지므로 개별 페이지에서 관리
import axios from 'axios'
const Django_API_URL = 'http://127.0.0.1:8000'
export default {
    name: 'ProfileView',
		data() {
        return{
            user_data : null,
						genre_list : this.$store.state.genre_list,
						genre_data : [],
        }
    },
    created(){
      axios({
        method:'get',
        url:`${Django_API_URL}/api/v1/user/${this.$store.state.user_data.pk}/`
      })
      .then(res=>{
        this.user_data = res.data
				// 장르의 정보는 Many To Many DB에서 가져와야 하므로 for문을 돌려 처리
				for(const obj of this.genre_list){
					for(const userobj of this.user_data.genres){
						if (obj['id'] === userobj){
							this.genre_data.push(obj['name'])
						}
					}
				}
      })
    },
    method:{
			// 받아온 genre 데이터가 id로 되어있으므로 name으로 바꿔주는 과정
      genreName(genre) {
				for (let i = 0; i < this.genre_list.length; i++) {
					if (this.genre_list[i].id === genre) {
						return this.genre_list[i].name
					}
				}
			}
    }
}
</script>

<style>
.detail {
	border-radius: 0.5rem;
	margin: auto;
	width: 1000px;
	box-shadow: 4px 4px 4px grey;
	background-color: #141414;
	margin-bottom: 15rem;
	margin-top: 5rem;
}
.userName {
	padding-top: 1.5rem;
	padding-left: 1.5rem;
	text-align: start;
	padding-bottom: 20px;
	border-bottom: solid grey 2px;
}
.userContent {
	margin: auto;
	width: 95%;
	height: 400px;
	background-color: #383838;
	padding: 15px;
	text-align: start;
	border-radius: .5rem;
}
</style>

<style scoped>
div a {
	font-weight: bold;
	font-size: 20px;
	color: #ffffff;
	text-decoration-line: none;
}
</style>