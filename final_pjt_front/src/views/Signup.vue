<template>
  <div>
    <h1>Sign Up Page</h1>
    <form @submit.prevent="signUp">
      <label for="username">username : </label>
      <input type="text" id="username" v-model="username"><br>

      <label for="password1"> password : </label>
      <input type="password" id="password1" v-model="password1"><br>

      <label for="password2"> password confirmation : </label>
      <input type="password" id="password2" v-model="password2">
      
      <input type="submit" value="SignUp" @click="GoToHome">
    </form>
  </div>
</template>

<script>
export default {
  name: 'SignUp',
  data() {
    return {
      username: null,
      password1 : null,
      password2 : null,
    }
  },
  methods: {
    signUp() {
      const username = this.username
      const password1 = this.password1
      const password2 = this.password2

      const payload = {
        username, password1, password2
      }

      this.$store.dispatch('signUp', payload)

    },
    GoToHome(){
      console.log(this.username)
      if(this.username==undefined || this.username==""){
        alert('아이디를 입력해주세요')
        return false
      }else if(this.password1==null || this.password1==""){
        alert('비밀번호를 입력해주세요')
        return false
      }else if(this.password1 != this.password2){
        alert('비밀번호가 일치하지 않습니다')
        return false
      }else{
        this.$router.push({ name: 'movies'})
      }
    }
  }
}
</script>
