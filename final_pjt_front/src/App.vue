<template>
  <div id="app">
    <nav v-if="$store.state.user_data === null">
      
      <router-link to="/login">Login</router-link> |
      <router-link to="/signup">Signup</router-link> |
      <router-link to="/search">Search</router-link>
    </nav>
    <nav v-else>
      <router-link @click.native="logout" to="/logout">LogOUT</router-link> |
      <router-link to="/signup">Signup</router-link> |
      <router-link :to="{
        name: 'profile',
        params: {id: $store.state.user_data.pk}
      }">Profile</router-link> |
      <router-link to="/search">Search</router-link>
    </nav>
    <nav>
      <router-link to="/">Movie</router-link> |
      <router-link to="/community">Community</router-link> |
      <router-link to="/entertain">Entertainment</router-link>
    </nav>
    <router-view/>
  </div>
</template>

<script>
  export default {
    methods: {
      logout() {
        this.$store.dispatch('logout')
        this.$router.push({name: 'movies'})
      }
    }
  }
</script>






<style>
html {
  background: linear-gradient(#000000, #0c0c0c)
}

#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: white;
  background: linear-gradient(#000000, #0c0c0c)
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
