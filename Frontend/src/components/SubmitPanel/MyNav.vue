<template>
    <div class="nav">
        <div class="left-nav">
            <div class="logo"></div>
            <div class="OJName">SimpleOJ</div>
        </div>
        <div class="userchoices">
            <a @click="showList">题目列表</a>
        </div>
        <div class="dropdown">
            <button class="dropbtn" id="nameSaver">{{ $route.query.username }}</button>
            <div class="dropdown-content">
                <a @click="showList">主页</a>
                <a href="/index.html">登出</a>
            </div>
        </div>
    </div>
</template>

<script>
// import Router from "../../api/router/Router.js"

import router from '@/router';

export default{
	// name: 'MyNav'
    methods: {
    showList(){
        this.$router.push({ name: 'home', query: { parms: this.$route.query.username } })//跳转新页面
}

}
}

</script>

<style scoped>
body {
    margin: 0;
}

.nav {
    position: sticky;
    top: 0;
    z-index: 2;
    height: 70px;
    border-bottom: 1px solid #777777;
    background-color: #FFFFFF;
    line-height: 70px;
    box-shadow: 0px 2px 2px 1px rgb(21, 4, 4, .5);
}

.nav .left-nav {
    float: left;
    display: flex;
    justify-content: start;
    width: 200px;
}

.nav .left-nav .logo {
    width: 70px;
    border-radius: 35px;
    /*    background-image: url(/images/middlepic.jpg); */
}

/* 导航栏的选项 */
.nav .userchoices {
    float: left;
    padding-left: 100px;
}

.nav .userchoices a {

    /* a属于行内元素 此时必须要转换 行内块元素 */
    display: inline-block;
    height: 70px;
    padding: 0 20px;
    font-size: 20px;
    color: #4c4c4c;
    text-decoration: none;
}

.nav a:hover {
    background-color: #eee;
    color: #ff8500;
}

/* 下拉列表 */
.dropbtn {
    width: 150px;
    background-color: #b7d5ec;
    color: black;
    padding: 16px;
    font-size: 20px;
    border: none;
    cursor: pointer;
    border-radius: 8px;
}

.dropdown {
    float: right;
    position: relative;
    right: 10px;
}

.dropdown-content {
    display: none;
    position: absolute;
    right: 0px;
    text-align: center;
    background-color: #f9f9f9;
    min-width: 150px;
    box-shadow: 0px 8px 16px 0px rgba(0, 0, 0, 0.2);
    z-index: 1;
}

.dropdown-content a {
    color: black;
    /* padding: 12px 16px; */
    text-decoration: none;
    display: block;
}

.dropdown-content a:hover {
    background-color: #f1f1f1
}

.dropdown:hover .dropdown-content {
    display: block;
}

.dropdown:hover .dropbtn {
    background-color: #3e8e41;
}
</style>