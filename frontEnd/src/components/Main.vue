<template>
  <el-container v-loading="loading">
    <el-header style="height: 120px; background-color: #193562;border-bottom: white 5px solid">
      <el-image src="lion2.png" fit="cover" style="height: 100px;margin-top: 10px;margin-left: 30px"></el-image>
      <div style="display: inline-block;font-size: 50px;transform: translate(0, -50%);color: #9FCBEA;font-weight: bold;margin-left: 20px">Columbia Chatroom</div>
      <el-button style="float: right;height: 60px; width: 200px;margin-right: 60px;margin-top: 30px;
                          font-size: 20px;font-weight: bold" type="primary" @click="joinVisible = true">Join New Group!</el-button>
      <el-drawer
        :visible.sync="joinVisible"
        direction="rtl"
        size = "50%">
        <div style="border: #193562 10px solid; height: 100%; width: 100%">
          <div style="color: #2a90e3; text-align: center;font-weight: bold; font-size: 40px;margin-top: 30px"> Join a new Group for discussion! </div>
          <div class="join-label" style="margin-top: 10%">Group ID</div>
          <br>
          <el-input class="join-input" placeholder="Please enter group ID" v-model="joinID"></el-input>
          <br>
          <div class="join-label">Group Password</div>
          <br>
          <el-input class="join-input" placeholder="Please enter group Password" v-model="joinPWD"></el-input>
          <br><br><br>
          <div style="text-align: center">
            <el-button type="primary" style="width: 200px;height: 100px; font-size: 30px" @click="joinGroup()">Join!</el-button>
          </div>
        </div>
      </el-drawer>
    </el-header>
    <el-container>
      <el-aside width="30%" style="height: calc(100vh - 120px); background-color: #9FCBEA; padding-right: 10px;border-right: white 5px solid">
        <br>
        <div v-for="(item, index) in groups" :key="index">
        <el-card class="box-card" @click.native="getMessage(item.group)">
          <div slot="header" class="clearfix">
            <span style="font-weight: bold">{{item.group}}</span>
          </div>
          <div>
            <span>Course of 2022 Fall</span>
          </div>
        </el-card><el-button style="float: right; height: 13vh; width: 70px; padding: 2px;
                  font-size: 13px;font-weight: bold" type="primary" @click="getMember(item.group)">Members</el-button>
        <br><br><br>
        </div>
      </el-aside>
      <el-main style="height: calc(100vh - 120px);background-color: #193562;padding: 15px 10px 15px 10px; ">
        <div class="chat-panel">
          <br>
          <div v-for="(item, index) in message" :key="index" style="margin-left: 10px">
            <div v-if = "item.email != email">
              <div style="width: 200px; background-color: #193562;padding: 10px; text-align: center;font-weight: bold;border-radius: 5px;color: white">{{ item.name }}</div>
              <div style="width: 35vw; background-color: #ffffff; color: #193562; padding: 10px;border-radius: 5px">{{ item.msg }}</div>
            </div>
            <div v-if = "item.email === email">
              <div style="width: 200px; background-color: #193562;padding: 10px; text-align: center;font-weight: bold;border-radius: 5px;color: white; transform: translate(54vw, 0);">{{ item.name }}</div>
              <div style="width: 35vw; background-color: #ffffff; color: #193562; padding: 10px;border-radius: 5px; transform: translate(31vw, 0);">{{ item.msg }}</div>
            </div>
              <br><br>
          </div>
        </div>
        <div class="input-panel">
          <el-input v-model="sendContent" placeholder="Feel free to say what you want!" :disabled="status === 'mute'"></el-input>
          <el-button class="send-bot" @click="sendMessage()">Send</el-button>
        </div>
      </el-main>
      <el-drawer
        :visible.sync="memberVisible"
        direction="ltr"
        size = "50%">
        <div style="border: #193562 10px solid; height: 100%; width: 100%">
          <div v-for="(item, index) in members" :key="index">
            <div class="memberSpan">
              <el-row :gutter="10">
                <el-col :span="9"><div class="grid-content bg-purple">{{item.name}}</div></el-col>
                <el-col :span="9"><div class="grid-content bg-purple">{{item.email}}</div></el-col>
                <el-col v-if="manager === 'true'" :span="6"><div class="grid-content bg-purple"><el-button v-if="item.status === 'mute'" @click="manegeMember('active', item)" class="memBot" type="success">unmute</el-button><el-button v-if="item.status === 'active'" @click="manegeMember('mute', item)" class="memBot" type="warning">mute</el-button><el-button class="memBot" type="danger" @click="manegeMember('kick', item)">kick</el-button></div></el-col>
              </el-row>
            </div>
            <hr>
          </div>
        </div>
      </el-drawer>
    </el-container>
  </el-container>

</template>

<script>
export default {
  inject: ['reload'],
  data () {
    return {
      manager: '',
      loading: false,
      name: '',
      email: '',
      groups: [],
      message: [],
      sendContent: 'Please choose a group',
      currentGroup: '',
      joinVisible: false,
      joinID: '',
      joinPWD: '',
      memberVisible: false,
      members: [],
      status: 'mute',
      memeberGroup: ''
    }
  },
  methods: {
    getGroups () {
      const that = this
      that.loading = true
      this.$axios.post('/groups', {
        email: that.email
      }).then(res => {
        if (res.data.statusCode === 200) {
          that.groups = res.data.body
        } else {
          alert(res.data.body)
        }
        that.loading = false
      }).catch(error => {
        console.log(error)
      })
    },
    getMessage (group) {
      const that = this
      that.loading = true
      that.currentGroup = group
      this.$axios.post('/message', {
        email: that.email,
        group: group
      }).then(res => {
        if (res.data.statusCode === 200) {
          that.message = res.data.body
          that.status = res.data.status
          if (that.status === 'mute') {
            that.sendContent = 'You are muted...'
          } else {
            that.sendContent = ''
          }
        } else {
          alert(res.data.body)
        }
        that.loading = false
      }).catch(error => {
        console.log(error)
      })
    },
    sendMessage () {
      const that = this
      that.loading = true
      this.$axios.post('/send', {
        email: that.email,
        group: that.currentGroup,
        msg: that.sendContent
      }).then(res => {
        if (res.data.statusCode === 200) {
          that.getMessage(that.currentGroup)
          that.loading = false
        } else {
          alert(res.data.body)
        }
        that.loading = false
      }).catch(error => {
        console.log(error)
      })
    },
    joinGroup () {
      const that = this
      that.loading = true
      this.$axios.post('/join', {
        email: that.email,
        group: that.joinID,
        gpwd: that.joinPWD,
        name: that.name
      }).then(res => {
        if (res.data.statusCode === 200) {
          that.getGroups()
        } else {
          alert(res.data.body)
        }
        that.loading = false
      }).catch(error => {
        console.log(error)
      })
    },
    getMember (group) {
      const that = this
      that.loading = true
      that.memeberGroup = group
      this.$axios.post('/member', {
        group: group
      }).then(res => {
        if (res.data.statusCode === 200) {
          that.members = res.data.body
          that.memberVisible = true
        } else {
          alert(res.data.body)
        }
        that.loading = false
      }).catch(error => {
        console.log(error)
      })
    },
    manegeMember (action, member) {
      const that = this
      that.loading = true
      this.$axios.post('/manage', {
        email: member.email,
        group: member.group,
        action: action
      }).then(res => {
        if (res.data.statusCode === 200) {
          that.getMember(that.memeberGroup)
        } else {
          alert(res.data.body)
        }
        that.loading = false
      }).catch(error => {
        console.log(error)
      })
    }
  },
  created () {
    if (this.$route.query) {
      this.name = this.$route.query.name
      this.email = this.$route.query.email
      this.manager = this.$route.query.manager
    }
    this.getGroups()
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.el-card {
  background-color: #9FCBEA;
  color: white;
}
.chat-panel {
  background-color: #8d90a1;
  height: calc(70vh - 109px);
  border-radius: 5px;
  overflow-y: scroll;
}

.input-panel {
  margin-top: 15px;
  background-color: #f8f8f8;
  height: calc(30vh - 56px);
  border-radius: 5px;
}
.send-bot {
  background-color: #2a5da9;
  color: white;
  font-size: 18px;
  font-weight: bold;
  /*position: absolute;*/
  height: 50px;
  width: 100px;
  transform: translate(60vw, 0);
}
.box-card {
  cursor: pointer;
  color: #ffffff;
  display: inline-block;
  height: 13vh;
  width: calc(30vw - 100px);
  background-color: #193562;
  margin-left: 5px;
}

.box-card:hover {
  background-color: #647b8f;
}

div >>> .el-input > input{
  height: 18vh;
  background-color: #f8f8f8;
  border: none;
  font-size: 25px;
  color: black;
}
.join-label {
  text-align: center;
  font-size: 30px;
  font-weight: bold;
  color: #193562;
}
.join-input {
  text-align: center;
  font-size: 30px;
  font-weight: bold;
  width: 80%;
  margin-left: 10%;
  color: #193562;
}
.memberSpan {
  margin-left: 5%;
  color: #2a5da9;
  height: 30px;
  font-size: 20px;
  margin-top: 10px;
  font-weight: bold;
  line-height: 40px;
}
.memBot {
  display: inline;
  margin-bottom: 10px;
}
</style>
