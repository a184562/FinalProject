<template>
  <div id="app">
    <nav>
      <a href="http://localhost:8080/login">Login</a> |
      <a href="http://localhost:8080/signup">Signup</a> |
      <a href="#">Profile</a>
    </nav>
    <nav>
      <router-link to="/">Movie</router-link> |
      <router-link to="/community">Community</router-link> |
      <router-link to="/entertain">Entertainment</router-link>
    </nav>
    <router-view/>
  </div>
</template>






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
