<template>
  <div>
    <h1>LogIn Page</h1>
    <form @submit.prevent="login">
      <label for="username">username : </label>
      <input type="text" id="username" v-model="username"><br>

      <label for="password"> password : </label>
      <input type="password" id="password" v-model="password"><br>

      <input type="submit" value="logIn">
    </form>
  </div>
</template>

<script>
export default {
  name: 'LogIn',
  data() {
    return {
      username : null,
      password : null,
    }
  },
  methods: {
    login() {
      const username = this.username
      const password = this.password
      
      const payload = {
        username, password
      }

      if(this.username==""){
        alert('아이디를 입력해주세요')
        return false
      }
      else if(this.password==""){
        alert('비밀번호를 입력해주세요')
        return false
      }
      else {
        this.$store.dispatch('logIn', payload)
        this.$router.push({ name: 'movies'})
      }
      
    }

  }
}
</script>