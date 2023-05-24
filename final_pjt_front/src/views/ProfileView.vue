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
						<h3>{{genre}}</h3>
					</div>
				</div>
        <h3>좋아요한 영화</h3>
        <div v-for="(content,index) of user_movie" :key="index"><h3>{{content.id}}</h3></div>
        <h5 class="mb-4">팔로잉 : {{ user_data.followings.length}}명</h5>
        <h5>팔로워 : {{ user_data.followers.length}}명</h5>
      </div>
    </div>
		<br>
  </div>
</template>

<script>
import axios from 'axios'

const Django_API_URL = 'http://127.0.0.1:8000'
export default {
    name: 'ProfileView',
    created(){
      axios({
        method:'get',
        url:`${Django_API_URL}/api/v1/movies/${this.$store.state.user_data.pk}/`
      })
      .then(res =>{
        this.user_movie = res.data.like_movies
        })
      .catch((err)=>console.log(err))
      axios({
        method:'get',
        url:`${Django_API_URL}/api/v1/user/${this.$store.state.user_data.pk}/`
      })
      .then(res=>{
        this.user_data = res.data
				for(const obj of this.genre_list){
					for(const userobj of this.user_data.genres){
						if (obj['id'] === userobj){
							this.genre_data.push(obj['name'])
						}
					}
				}
      })
    },
    data() {
        return{
            user_data : null,
						genre_list : this.$store.state.genre_list,
						genre_data : [],
            user_movie:null,
        }
    },
    
    method:{
      genreName(genre) {
				for (let i = 0; i < this.genre_list.length; i++) {
					// console.log(genreObj)
					// console.log(genre)
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
	/* height: 75%; */
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