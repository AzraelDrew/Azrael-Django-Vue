<template>
  <div class="userlist">
    <div v-for="item in imgList" :key="item.pk" class="user">
      <img :src="apiurl+item.headImg" alt="">
      <p>{{item.nickName}}</p>
    </div>

  </div>
</template>

<script>
  import axios from "axios"
  export default {
    data() {
      return {
        apiurl: "http://localhost:8000/",
        imgList: [],
        menuId: 1
      }
    },
    components: {},
    watch: {
      $route(to) {
        this.menuId = to.query.menuId
        this.getUserList(this.menuId)

      }
    },
    mounted() {
      this.getUserList(this.menuId)
    },
    methods: {
      // 从这里开始后端去请求
      getUserList(id) {
        // console.log("开始获取分类列表" + id);
        // axios.get("http://localhost:8000/get-user-list/", {
        //   params: {
        //     id
        //   }

        // }).then(res => {
        //   console.log(res);
        // })
        axios({
          url: "http://localhost:8000/get-user-list/",
          type: "json",
          params: {
            id
          },
          method: "get"
        }).then(res => {
          this.imgList = res.data
        })

      }
    }
  }
</script>

<style lang='scss'>


</style>