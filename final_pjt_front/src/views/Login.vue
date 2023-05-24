<template>
  <div class="loginform">
    <div class="mt-5">
      <div class="accountform">
        <h2 class="loginTitle pt-2 pb-2 ms-3 me-3">로그인</h2>
        <form @submit.prevent="login">
          <div style="width: 80%; margin: auto;">
            <div class="input-group">
              <span class="input-group-text" id="basic-addon1">Username</span>
              <input type="text" class="form-control" placeholder="Username" aria-label="Username" aria-describedby="basic-addon1" v-model="username">
            </div>
            <div class="input-group mt-1">
              <span class="input-group-text" id="basic-addon2">비밀번호</span>
              <input type="password" class="form-control" placeholder="Password" aria-label="Password" aria-describedby="basic-addon2" v-model="password">
            </div>
            
            <input class="btn btn-dark mt-2 mb-2" type="submit" value="login">
          </div>
        </form>
      </div>

    </div>
  </div>
  <!-- <div>
    <h1>LogIn Page</h1>
    <form @submit.prevent="login">
      <label for="username">username : </label>
      <input type="text" id="username" v-model="username"><br>

      <label for="password"> password : </label>
      <input type="password" id="password" v-model="password"><br>

      <input type="submit" value="logIn">
    </form>
  </div> -->
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

<style scoped>
.loginform {
  border-radius: 0.5rem;
	margin: auto;
	width: 500px;
	/* height: 75%; */
	box-shadow: 4px 4px 4px grey;
	background-color: #141414;
	margin-bottom: 15rem;
	margin-top: 5rem;
}
.input-group-text {
  width: 31%;
}
.loginTitle {
  border-bottom: solid grey 1px;
  text-align: start;
}

</style>