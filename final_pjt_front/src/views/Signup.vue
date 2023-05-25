<template>
  <div class="signUpform">
    <div class="mt-5">
      <div class="accountform">
        <h2 class="signUpTitle pt-2 pb-2 ms-3 me-3">회원가입</h2>
        <!-- username, password, passwordconfirm, email, firstname, lastname 입력을 통해 가입 정보를 받을 수 있게 함 -->
        <!-- 다만, username, password, passwordconfirm정보는 필수 값으로 입력 받도록하고 나머지 값은 비워도 가입 가능하게 설정 -->
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
</template>

<script>
export default {
  name: 'SignUp',
  // 가입하는데 있어서 입력 받을 정보들을 data에 정의
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
  // 가입을 위한 데이터를 Django 서버에 보내주기 위한 함수 정의
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
      // username과 password, passwordconfirm을 입력하지 않으면 가입할 수 없도록 함수 정의
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
        // 가입 후 메인페이지로 가는 것이 아닌 유저의 선호 장르 데이터를 받기 위한 장르 선택 페이지로 이동
        this.$router.push({ name: 'genre'})
      }

      

    },
  }
}
</script>

<style scoped>
.signUpform {
  border-radius: 0.5rem;
	margin: auto;
	width: 500px;
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