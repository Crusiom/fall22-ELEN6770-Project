<template>
  <el-container>
    <el-container>
      <el-main style="height: 100vh;width: 100vw; background-color: #193562;">
        <div style="border: rgba(19,83,141,0.76) 10px solid;margin-left: calc(50vw - 400px); text-align: center; margin-top: calc(50vh - 425px); height:800px; width: 800px; background-color: white">
          <el-image src="lion.png" fit="cover" style="height: 100px;margin-top: 10px"></el-image>
          <div style="color: #193562;font-size: 30px;font-weight: bold">Columbia ChatRoom</div>
          <br>
          <div class="input-label">Name</div>
          <br>
          <el-input class="login-input" placeholder="Please enter your name" v-model="name"></el-input>
          <br><br>
          <div class="input-label">Email Address</div>
          <br>
          <el-input class="login-input" placeholder="Please enter your email address" v-model="email"></el-input>
          <br><br>
          <div class="input-label">Password</div>
          <br>
          <el-input class="login-input" placeholder="Please enter your password" v-model="password" show-password></el-input>
          <br><br>
          <div class="input-label">Renter Password</div>
          <br>
          <el-input class="login-input" placeholder="Please enter your password" v-model="password2" show-password></el-input>
          <br><br><br><br>
          <el-button class="login-bot" size="medium" @click="goToLogin()">Register</el-button>
        </div>
      </el-main>
    </el-container>
  </el-container>

</template>

<script>
export default {
  data () {
    return {
      name: 'Danling Wei',
      email: 'dw3033@columbia.edu',
      password: '123',
      password2: '123'
    }
  },
  methods: {
    goToLogin () {
      this.$router.push({
        path: '/login'
      })
    },
    register () {
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

.input-label {
  color: #193562;
  font-size: 20px;
  font-weight: bold
}

.login-input {
  display: inline-block;
  width: 60%;
  border: #193562 2px solid;
  font-size: 15px;
}
.login-bot {
  background-color: #193562;
  width: 150px;
  height: 50px;
  color: white;
  font-weight: bold;
  font-size: 20px;
}
.register-bot {
  background-color: #9FCBEA;
  width: 200px;
  height: 50px;
  color: #193562;
  font-weight: bold;
  font-size: 20px;
}
</style>
