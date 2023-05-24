<template>
  <div class="signUpform">
    <div class="mt-5">
      <div class="accountform">
        <h2 class="signUpTitle pt-2 pb-2 ms-3 me-3">회원가입</h2>
        <form @submit.prevent="signUp">
          <div style="width: 80%; margin: auto;">
            <div class="input-group">
              <span class="input-group-text" id="basic-addon1">Username</span>
              <input type="text" class="form-control" placeholder="Username" aria-label="Username" aria-describedby="basic-addon1" v-model="username">
            </div>
            <div class="input-group mt-1">
              <span class="input-group-text" id="basic-addon2">비밀번호</span>
              <input type="password" class="form-control" placeholder="Password" aria-label="Password" aria-describedby="basic-addon2" v-model="password1">
            </div>
            <div class="input-group mt-1">
              <span class="input-group-text" id="basic-addon1">비밀번호 확인</span>
              <input type="password" class="form-control" placeholder="Password Confirm" aria-label="Username" aria-describedby="basic-addon1" v-model="password2">
            </div>
            <div class="input-group mt-1">
              <span class="input-group-text" id="basic-addon1">E-mail</span>
              <input type="text" class="form-control" placeholder="E-mail" aria-label="Username" aria-describedby="basic-addon1" v-model="email">
            </div>
            <div class="input-group mt-1">
              <span class="input-group-text" id="basic-addon1">First Name</span>
              <input type="text" class="form-control" placeholder="First Name" aria-label="Username" aria-describedby="basic-addon1" v-model="firstname">
            </div>
            <div class="input-group mt-1">
              <span class="input-group-text" id="basic-addon1">Last Name</span>
              <input type="text" class="form-control" placeholder="Last Name" aria-label="Username" aria-describedby="basic-addon1" v-model="lastname">
            </div>
            <input class="btn btn-dark mt-2 mb-2" type="submit" value="SignUp">
          </div>
        </form>
      </div>

    </div>
  </div>
  <!-- <div>
    <h1>Sign Up Page</h1>
    <form @submit.prevent="signUp">
      <label for="username">username : </label>
      <input type="text" id="username" v-model="username"><br>

      <label for="password1"> password : </label>
      <input type="password" id="password1" v-model="password1"><br>

      <label for="password2"> password confirmation : </label>
      <input type="password" id="password2" v-model="password2">
      
      <input type="submit" value="SignUp">
    </form>
  </div> -->
</template>

<script>
export default {
  name: 'SignUp',
  data() {
    return {
      username: "",
      password1 : "",
      password2 : "",
      email: "",
      firstname: "",
      lastname: "",
    }
  },
  methods: {
    signUp() {
      const username = this.username
      const password1 = this.password1
      const password2 = this.password2
      const email = this.email
      const firstname = this.firstname
      const lastname = this.lastname

      const payload = {
        username, password1, password2, email, firstname, lastname
      }
      
      console.log(payload)
      if(this.username==""){
        alert('아이디를 입력해주세요')
        return false
      }else if(this.password1==""){
        alert('비밀번호를 입력해주세요')
        return false
      }else if(this.password1 != this.password2){
        alert('비밀번호가 일치하지 않습니다')
        return false
      }else{
        this.$store.dispatch('signUp', payload)
        this.$router.push({ name: 'movies'})
      }

      

    },
    // GoToHome(){
    //   console.log(this.username)
    //   if(this.username==""){
    //     alert('아이디를 입력해주세요')
    //     return false
    //   }else if(this.password1==""){
    //     alert('비밀번호를 입력해주세요')
    //     return false
    //   }else if(this.password1 != this.password2){
    //     alert('비밀번호가 일치하지 않습니다')
    //     return false
    //   }else{
    //     this.$router.push({ name: 'movies'})
    //   }
    // }
  }
}
</script>

<style scoped>
.signUpform {
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
.signUpTitle {
  border-bottom: solid grey 1px;
  text-align: start;
}

</style>