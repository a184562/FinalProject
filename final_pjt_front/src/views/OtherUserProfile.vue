<template>
  <div>
    <p>{{ $route.params.id }}</p>
    <p>{{ $route.params.username }}</p>
    {{ this.$store.state.user_data }}
    <div v-if="$route.params.id != this.$store.state.user_data.pk">
      <button @click="Follow">팔로우</button>
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
            
        }
    },
    created(){
      
    },
    methods:{
      Follow(){
        console.log()
        axios({
          method:'post',
          url:`${Django_API_URL}/api/v1/follow/${this.$store.state.user_data['id']}/${this.$route.params.id}/`
        })
        .then(()=>{})
        .catch(()=>{})
      }
    }
}
</script>

<style>

</style>