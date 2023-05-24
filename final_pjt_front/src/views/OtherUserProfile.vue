<template>
  <div class="detail">
    <div class="mt-5">
      <div class="userName">
        <h1>{{ $route.params.username }}</h1>
      </div>
      <div class="userContent mt-4">
        <h3>e-mail : {{ $route.params.email }}</h3><br>
        <h3>name : {{ $route.params.first_name }}{{ $route.params.last_name }}</h3><br>
        <h3>선호 장르 : {{  }}</h3><br>
        <h3>작성 글 : {{  }}</h3><br>
        <h5>팔로잉 : {{  }}명</h5>
        <h5>팔로워 : {{  }}명</h5>
      </div>
    </div>
    
    <div>
      <button @click="Follow" v-if="follow_check==false">팔로우</button>
      <button @click="Follow" v-else-if="follow_check==true">언팔로우</button>
    </div>
  </div>
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
        }
    },
    created(){
      axios({
        method:'get',
        url:`${Django_API_URL}/api/v1/otheruser/${this.$route.params.id}`
      })
      .then(res=>{
        this.user_data=res.data
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