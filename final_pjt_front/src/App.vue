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
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

nav {
  padding: 30px;
}

nav a {
  font-weight: bold;
  color: #2c3e50;
}

nav a.router-link-exact-active {
  color: #42b983;
}
</style>
