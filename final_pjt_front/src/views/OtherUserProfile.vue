<template>
  <div>
    <p>{{ $route.params.id }}</p>
    <p>{{ $route.params.username }}</p>
    {{ this.$store.state.user_data.pk }}
    <p>팔로워 수: {{ user_data.followings.length}}명</p>
    <p>팔로잉 수: {{}} 명</p>
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

<style>

</style>