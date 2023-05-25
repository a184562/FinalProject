<template>
  <div id="app">
    <!-- 로그인 되어있지 않다면 기능을 사용하기 위해서 로그인하도록 nav를 구분 -->
    <nav v-if="$store.state.user_data === null" class="navbot">
      <router-link to="/">Login</router-link> |
      <router-link to="/signup">Signup</router-link>
    </nav>
    <!-- 로그인 시 로그아웃, 프로필 페이지를 가장 위 nav에 표시 -->
    <nav v-else>
      <router-link @click.native="logout" to="/logout">Logout</router-link> |
      <router-link :to="{
        name: 'profile',
        params: {id: $store.state.user_data.pk}
      }">Profile</router-link>
    </nav>
    <!-- 로그인 시 다른 메뉴로 갈 수 있는 nav를 생성해줌 -->
    <nav v-if="this.$store.state.user_data" class="navbot">
      <router-link to="/movies">Movie</router-link> |
      <router-link to="/community">Community</router-link> |
      <router-link to="/entertain">Entertainment</router-link> |
      <router-link to="/search">Search</router-link>
    </nav>
    <router-view/>
  </div>
</template>

<script>
  export default {
    methods: {
      // 모든 페이지에서 위에 뜨는 nav를 통해 실행하는 함수는 logout 뿐이므로 App.vue에는 logout함수만 정의
      logout() {
        this.$store.dispatch('logout')
        this.$router.push({name: 'login'})
      },
    },
  }
</script>






<style>
@import url('https://fonts.googleapis.com/css2?family=Song+Myung&display=swap');

html {
  background: linear-gradient(#000000, #0c0c0c);
  background-size: cover;
  height: 100vh;
}

#app {
  font-family: 'Song Myung', serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: white;
  background: linear-gradient(#000000, #0c0c0c);
  height: 100vh;
  /* font-weight: bold; */
}
.title {
  text-align: left;
  color: #E50914
}
nav {
  text-align: right;
  padding: 15px;
  /* border: solid black 2px; */
  height: 3rem;
  
}
.navbot {
  box-shadow: 2px 2px 2px grey;
}
nav a {
  font-weight: bold;
  color: #E50914;
}

nav a.router-link-exact-active {
  color: #ffffff;
}





</style>
