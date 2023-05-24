<template>
  <div class="detail">
    <div class="mt-5">
      <div class="userName">
        <h1>{{ user_data.username }}</h1>
		
      </div>
      <div class="userContent mt-4">
        <h3 class="ms-1">e-mail : {{ user_data.email }}</h3><br>
        <h3 class="ms-1">name : {{ user_data.first_name }}{{ user_data.last_name }}</h3><br>
				<div class="d-flex">
					<h3>선호 장르 : </h3>
					<div v-for="(genre,index) in genre_data" :key="index" class="ms-3">
                  <router-link :to="{
                  name: 'freeboarddetail',
                  params: {id: genre.index.id}}">
                </router-link>
        </div>
		<div class="p-2 me-3">
					</div>
				</div>
        <h3 class="mt-3">작성 글 : {{  }}</h3><br>
        <h5 class="mb-4">팔로잉 : {{ user_data.followings.length}}명</h5>
        <h5>팔로워 : {{ user_data.followers.length}}명</h5>
        <button class="btn btn-secondary mt-2" @click="Follow" v-if="follow_check==false">팔로우</button>
        <button class="btn btn-secondary mt-2" @click="Follow" v-else-if="follow_check==true">언팔로우</button>
      </div>
      
    </div>
		<br>
  </div>
  <!-- <div>
    <p>{{ $route.params.id }}</p>
    <h1>{{ $route.params.username }}</h1>
    {{ this.$store.state.user_data.pk }}
    {{user_data}}
    <p>팔로워 수: {{ user_data.followings.length }}명</p>
    <p>팔로잉 수: {{user_data.followers.length}} 명</p>
    <div>
      <button @click="Follow" v-if="follow_check==false">팔로우</button>
      <button @click="Follow" v-else-if="follow_check==true">언팔로우</button>
    </div>
  </div> -->
</template>

<script>
import axios from 'axios'
const Django_API_URL = 'http://127.0.0.1:8000'
export default {
    name: 'OtherUserProfile',
    data() {
        return{
            user_data: null,
            follow_check: null,
            user_datas:null,
            genre_list: this.$store.state.genre_list,
            genre_data: []
        }
    },
    created(){
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
      axios({
        method:'post',
        url:`${Django_API_URL}/api/v1/followcheck/${this.$route.params.id}/${this.$store.state.user_data['pk']}/`,
      })
      .then(res=>{
        console.log(res)
        this.follow_check = res.data
      })
    },
    methods:{
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
	/* height: 75%; */
	box-shadow: 4px 4px 4px grey;
	background-color: #141414;
	margin-bottom: 15rem;
	margin-top: 5rem;
}


</style>