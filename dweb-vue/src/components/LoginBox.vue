<template>
  <div id="login" @click.self="hideSelf">
    <!-- .self只对自身启用,不会影响子节点(子节点的事件不会冒泡到当前标签)  -->
    <div v-on:keydown.enter="toLogin" id="loginbox">
      <div class="from">
        <div class="item">
          <div class="span">
            用户名:
          </div>
          <input v-model="username" type="text" name="" id="" placeholder="请输入用户名">
        </div>
        <div class="item">
          <div class="span">
            密码:
          </div>
          <input v-model="password" type="text" name="" id="" placeholder="请输入密码">
        </div>
        <div v-if="target===2" class="item">
          <div class="span">
            确认密码:
          </div>
          <input v-model="password2" type="text" name="" id="" placeholder="再次输入密码">
        </div>
        <button v-if="target===1" v-on:click="toLogin">登录</button>
        <button v-if="target===2" v-on:click="toRegister">注册</button>
      </div>
    </div>
  </div>
</template>

<script>
  import axios from "axios"
  import Qs from "qs"
  export default {
    props: ["target"],
    name: "LoginBox",
    data() {
      return {
        username: "",
        password: "",
        password2: "",
      }
    },
    methods: {
      toLogin() {
        // console.log(this.username, this.password);
        // console.log("236765");
        // axios.post("http://localhost:8000/login/", {
        //   username,
        //   password
        // }).then(res => {
        //   console.log(res);
        // })
        let username = this.username
        let password = this.password
        if (username.length > 0 && password.length > 0) {
          axios({
            url: "http://localhost:8000/login/",
            method: "POST",
            data: Qs.stringify({
              username,
              password,
            }),
            headers: {
              "Content-Type": "application/x-www-form-urlencoded"
            }
          }).then(res => {
            console.log(res);
            switch (res.data) {
              case "none":
                alert("用户名不存在");
                break;
              case "pwdeer":
                alert("密码错误")
                break;
              default:
                console.log(res.data.token);
                alert("登录成功")
            }
          })
        } else {
          alert("用户名和密码不能为空!")
        }
      },
      toRegister() {
        let username = this.username
        let password = this.password
        let password2 = this.password2
        console.log(username, password, password2);
        if (username.length > 0 && password.length > 0 && password2.length > 0) {
          if (password != password2) {
            alert("两次密码不一致")
          } else {
            axios({
              url: "http://localhost:8000/register/",
              method: "POST",
              data: Qs.stringify({
                username,
                password,
                password2
              }),
              headers: {
                "Content-Type": "application/x-www-form-urlencoded"
              }
            }).then(res => {
              // console.log(res);
              switch (res.data) {
                case "sameName":
                  alert("用户已存在")
                  break;
                default:
                  break;
              }
            })
          }
        } else {
          alert("缺少必填项")
        }
      },
      hideSelf() {
        this.$emit("hideBox")
      }
    }
  }
</script>

<style>
  #login {
    position: absolute;
    top: 0;
    width: 700px;
    height: 100vh;
    display: flex;
    justify-content: center;
    align-items: center;
    background: #00000020;
  }

  #loginbox {
    position: absolute;
    width: 300px;
    height: 300px;
    border: 1px solid #000;
    background: #00000070;
    display: flex;
    justify-content: center;
    align-items: center;
  }

  #loginbox .from .item {
    font-weight: 700;
    margin: 10px auto;
  }

  #loginbox .from .item .span {
    float: left;
    width: 80px;
  }
</style>