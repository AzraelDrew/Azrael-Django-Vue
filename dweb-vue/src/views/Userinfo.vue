<template>
  <div id="userinfo">
    <h1>我的信息</h1>
    <img :src="'http://localhost:8000/'+userinfo.headImg" alt="">
    <div>{{userinfo.nickName}}</div>
    <div>身份:管理员</div>
  </div>
</template>

<script>
  export default {
    data() {
      return {
        userinfo: {}
      }
    },
    mounted() {
      this.getUserInfo();
      this.changePageUI();
    },
    methods: {
      getUserInfo() {
        console.log("开始获取用户信息");
        this.userinfo = this.$store.state.userinfo;
      },
      changePageUI() {
        this.$emit("changUI", true)
        this.$emit("hideBox")
      }
    }
  }
</script>

<style>
  #userinfo {
    margin-bottom: 10px;
  }
</style>