<template>
  <div id="home">
    <div>
      <button v-if="loginType===false" @click=" showLoginRegisterbox(1)">登录</button>
      <button v-if="loginType===false" @click="showLoginRegisterbox(2)">注册</button>
      <button @click="toHome" v-if="loginType">返回首页</button>
      <button @click="toUserInfo" v-if="loginType">个人中心</button>
      <button v-if="loginType===true" @click="showLoginRegisterbox(3)">修改</button>
      <div class="header">
        <h1>
          {{siteinfo.sitename}}
        </h1>
        <img :src="siteinfo.logo" alt="" />
      </div>
      <hr />
      <div class="content">
        <div class="menu">
          <div v-for="item in menuList" :key="item.id" class="item">
            <div v-if="item.id ===choosed" style="background:#777">
              <a style="color:#fff">
                {{item.text}}
              </a>
            </div>
            <div v-else @click="chooseMenu(item.id,item.text)">
              <a style="color:#000">
                {{item.text}}
              </a>
            </div>
          </div>
        </div>
        <div class="userlist">
          <p>
            {{choosed_text}}
          </p>
          <router-view @hideBox="hideLoginRegisterbox" @changUI="changeLoginType" />
        </div>
      </div>
    </div>
    <hr />
    <LoginBox v-if="boxtarget" :target="boxtarget" @hideBox="hideLoginRegisterbox"></LoginBox>
    <div class=" foot">
      Cpoyright @ 2021 Azrael
    </div>
  </div>
</template>
<script>
  import axios from 'axios'
  import LoginBox from './components/LoginBox'
  export default {
    data() {
      return {
        menuList: [],
        choosed: 1,
        choosed_text: "Django后端",
        boxtarget: 0,
        siteinfo: {},
        loginType: false
      }
    },
    components: {
      LoginBox
    },
    mounted() {
      try {
        if (window.localStorage.getItem("token").length > 0) {
          this.loginType = true;
        }
      } catch (err) {
        console.log(err);
      }
      this.getMenuList()
    },
    methods: {
      // 获取分类列表
      getMenuList() {
        console.log("开始获取分类");
        axios.get("http://localhost:8000/get-menu-list/").then(res => {
          console.log(res);
          this.menuList = res.data.menu_data;
          this.siteinfo = res.data.siteinfo
        })
      },
      chooseMenu(id, text) {
        this.choosed = id
        this.choosed_text = text
        // 进行id传惨跳转
        this.$router.push({
          path: "/",
          query: {
            menuId: id
          }
        })
      },
      // 展示登录注册框体
      showLoginRegisterbox(id) {
        this.boxtarget = id
      },
      // 隐藏登录注册框体
      hideLoginRegisterbox() {
        this.boxtarget = 0;
      },
      changeLoginType(value) {
        this.loginType = value
      },
      toUserInfo() {
        this.$router.push({
          path: "/userinfo"
        })
      },
      toHome() {
        this.$router.push({
          path: "/"
        })
      }

    }
  }
</script>

<style>

</style>