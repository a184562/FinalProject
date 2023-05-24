<template>
  <div class="detail">
    <div class="mt-5">
      <div class="userName">
        <h1>{{ user_data.username }}</h1>
		
      </div>
      <div class="userContent mt-4">
        <h3>e-mail : {{ user_data.email }}</h3><br>
        <h3>name : {{ user_data.first_name }}{{ user_data.last_name }}</h3><br>
        <h3>선호 장르 : {{  }}</h3><br>
        <h3>작성 글 : {{  }}</h3><br>
        <h5>팔로잉 : {{  }}명</h5>
        <h5>팔로워 : {{  }}명</h5>
      </div>
    </div>
    <p>팔로잉 버튼 만들 곳</p>
  </div>
</template>

<script>
export default {
    name: 'ProfileView',
    data() {
        return{
            user_data : this.$store.state.user_data
        }
    },
    method:{
      
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