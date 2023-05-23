<template>
  <div id="app">
    <nav v-if="$store.state.user_data === null">
      <h1 class="title">TITLE</h1>
      <p>1234564</p>
      <router-link to="/login">Login</router-link> |
      <router-link to="/signup">Signup</router-link> |
      <router-link to="/search">Search</router-link>
    </nav>
    <nav v-else>
      <h1 class="title">TITLE</h1>
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
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: white;
  background-color: #000000;
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
  /* background-color: #E50914; */
}

nav a {
  font-weight: bold;
  color: #E50914;
}

nav a.router-link-exact-active {
  color: #42b983;
}





</style>
