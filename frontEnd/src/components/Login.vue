<template>
  <el-container>
    <el-container>
      <el-main style="height: 100vh;width: 100vw; background-color: #193562;">
        <div style="border: rgba(19,83,141,0.76) 10px solid;margin-left: calc(50vw - 400px); text-align: center; margin-top: calc(50vh - 350px); height:600px; width: 800px; background-color: white">
          <el-image src="lion.png" fit="cover" style="height: 100px;margin-top: 10px"></el-image>
          <div style="color: #193562;font-size: 30px;font-weight: bold">Columbia ChatRoom</div>
          <br><br>
          <div class="input-label">Email Address</div>
          <br>
          <el-input class="login-input" placeholder="Please enter your email address" v-model="email"></el-input>
          <br><br>
          <div class="input-label">Password</div>
          <br>
          <el-input class="login-input" placeholder="Please enter your password" v-model="password" show-password></el-input>
          <br><br><br>
          <el-button class="login-bot" size="medium" @click="login()">Login</el-button>
          <br><br>
          <el-button class="register-bot" size="medium" @click="goToRegister()">Register</el-button>
        </div>
      </el-main>
    </el-container>
  </el-container>

</template>

<script>
export default {
  data () {
    return {
      email: 'dw3033@columbia.edu',
      password: '123',
      manager: '',
      name: ''
    }
  },
  methods: {
    goToMain () {
      const that = this
      this.$router.push({
        path: '/main',
        query: {
          email: that.email,
          name: that.name,
          manager: that.manager
        }
      })
    },
    goToRegister () {
      this.$router.push({
        path: '/register'
      })
    },
    login () {
      const that = this
      this.$axios.post('/login', {
        email: that.email,
        pwd: that.password
      }).then(res => {
        if (res.data.statusCode === 200) {
          that.email = res.data.body.email
          that.name = res.data.body.name
          that.manager = res.data.body.manager
          that.goToMain()
        } else {
          alert(res.data.body)
        }
      }).catch(error => {
        console.log(error)
      })
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
