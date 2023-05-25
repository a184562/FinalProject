<template>
  <div class="detail">
    <div class="mt-5">
      <div class="userName">
        <h1>{{ user_data.username }}</h1>
      </div>
      <div class="userContent mt-4">
        <h3 class="ms-1">e-mail : {{ user_data.email }}</h3><br>
        <h3 class="ms-1">name : {{ user_data.last_name }}{{ user_data.first_name }}</h3><br>
				<div class="d-flex">
					<h3>선호 장르 : </h3>
					<div v-for="(genre,index) in genre_data" :key="index" class="ms-3">
						<h3>{{genre}}</h3>
					</div>
				</div>
        <h5 class="mt-3 mb-4">팔로잉 : {{ user_data.followings.length}}명</h5>
        <h5>팔로워 : {{ user_data.followers.length}}명</h5>
        <button class="btn btn-secondary mt-3" @click="Follow" v-if="follow_check==false">팔로우</button>
        <button class="btn btn-secondary mt-3" @click="Follow" v-else-if="follow_check==true">언팔로우</button>
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
    name: 'OtherUserProfile',
    // 다른 유저의 데이터이므로 팔로우할지 여부를 판단할 follow_check 데이터 추가
    data() {
        return{
            user_data: null,
            genre_list: this.$store.state.genre_list,
            genre_data: [],
            follow_check: null,
        }
    },
    created(){
      // 다른 유저의 데이터를 가져오는 과정(프로필 페이지와 동일)
      axios({
        method:'get',
        url:`${Django_API_URL}/api/v1/user/${this.$route.params.id}`
      })
      .then(res=>{
        this.user_data=res.data
        for(const obj of this.genre_list){
					for(const userobj of this.user_data.genres){
						if (obj['id'] === userobj){
							this.genre_data.push(obj['name'])
						}
					}
				}
      })
      // 현재 로그인한 계정이 프로필의 유저를 팔로우하고 있는지 판단하는 과정
      axios({
        method:'post',
        url:`${Django_API_URL}/api/v1/followcheck/${this.$route.params.id}/${this.$store.state.user_data['pk']}/`,
      })
      .then(res=>{
        this.follow_check = res.data
      })
    },
    methods:{
      // follow DB에 post 요청을 통해 DB에 넣어주는 과정
      Follow(){
        console.log()
        axios({
          method:'post',
          url:`${Django_API_URL}/api/v1/follow/${this.$route.params.id}/${this.$store.state.user_data['pk']}/`
        })
        .then(()=>{this.$router.go(0)})
        .catch(()=>{})
      }
    }
}
</script>

<style scoped>
.detail {
	border-radius: 0.5rem;
	margin: auto;
	width: 1000px;
	box-shadow: 4px 4px 4px grey;
	background-color: #141414;
	margin-bottom: 15rem;
	margin-top: 5rem;
}


</style>