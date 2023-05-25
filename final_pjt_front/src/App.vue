<template>
  <div id="app">
    <nav v-if="$store.state.user_data === null">
      
      <router-link to="/">Login</router-link> |
      <router-link to="/signup">Signup</router-link> |
      <router-link to="/search">Search</router-link>
    </nav>
    <nav v-else>
      <router-link @click.native="logout" to="/logout">Logout</router-link> |
      <router-link to="/signup">Signup</router-link> |
      <router-link :to="{
        name: 'profile',
        params: {id: $store.state.user_data.pk}
      }">Profile</router-link>
    </nav>

    <nav v-if="this.$store.state.user_data">
      <router-link to="/movies">Movie</router-link> |
      <router-link to="/community">Community</router-link> |
      <router-link to="/entertain">Entertainment</router-link> |
      <router-link to="/search">Search</router-link>
    </nav>
    <router-view/>
  </div>
</template>

<script>
import axios from'axios'
const Django_API_URL = 'http://127.0.0.1:8000'
  export default {
    methods: {
      logout() {
        this.$store.dispatch('logout')
        this.$router.push({name: 'login'})
      },
      
    },
    created(){
      axios({
        method:'post',
        url:`${Django_API_URL}/api/v1/accounts/genre/`
      })
      .then(() => {})
      .catch(() => {})

      axios({
        method:'post',
        url:`${Django_API_URL}/api/v1/movie/genres/`
      })
      .then(() => {})
      .catch(() => {})
    }
    
  }
</script>






<style>
html {
  background: linear-gradient(#000000, #0c0c0c);
  background-size: cover;
  height: 100vh;
}

#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: white;
  background: linear-gradient(#000000, #0c0c0c);
  height: 100vh;
}
.title {
  text-align: left;
  color: #E50914
}
nav {
  text-align: right;
  padding: 15px;
  border: solid black 2px;
  height: 3rem;
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
