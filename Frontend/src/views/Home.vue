<template >
    <!-- 导航栏开始 -->
    <div class="nav">
        <div class="left-nav">
            <div class="logo"></div>
            <div class="OJName">SimpleOJ</div>
        </div>
        <div class="userchoices mychoices">
            <a>题目列表</a>
        </div>
        <div class="dropdown">
            <button class="dropbtn">{{ $route.query.parms }}</button>
            <div class="dropdown-content">
                <a href="#/login">登出</a>
            </div>
        </div>
    </div>

    <!-- 导航栏结束 -->
    <div class="bigbox">
        <div class="problemslistfield">
            <div class="leftpart">
                <div class="prelan">
                    <el-icon :size="50">
                        <Notebook />
                    </el-icon>
                    <span>题目列表</span>
                </div>
                <div class="searchfield">
                    <el-input v-model="search" placeholder="Type to search" :suffix-icon="Search" />
                </div>
                <el-table :data="filterTableData" @row-click="handleRowClick">
                    <el-table-column prop="id" label="id" width="500" />
                    <el-table-column prop="title" label="Name" width="300" />
                </el-table>
            </div>
            <el-pagination background layout="prev, pager, next" :total="1" />
        </div>
        <div class="Hellopart">
            <h2>Hello,{{ $route.query.parms }}</h2>
            <h2>欢迎来到本OJ</h2>
            <div class="prac">
                <p>您可以在此挑选题目练习</p>
            </div>
            <div class="intro">
                <p><span>介绍：</span>本OJ是基于vue和Django的轻量级OJ</p>
            </div>
            <div class="status">
                <p><span>状态 :</span> 正常</p>
            </div>

        </div>
    </div>
</template>
<script>
import axios from 'axios';
import { computed, ref } from 'vue'
export default {
    data() {
        return {
            problems: [],
            Tusername: '',
            search: ref(''),
            filterTableData: computed(() =>
                this.problems.filter(
                    (data) =>
                        !(this.search) ||
                        data.title.toLowerCase().includes(this.search.toLowerCase())
                )
            )
        }
    },
    mouted() {
        const username1 = this.$route.query.parms;
        this.Tusername = username1;
    },
    created() {
        this.initList()
    },
    methods: {
        async initList() {
            console.log();
            const { data: res } = await axios.get('http://127.0.0.1:8000/problem/problems/')
            console.log(res.status);
            if (res.status === 200) {
                this.problems = res.list
            }
        },
        handleRowClick(row) {
            this.$router.push({ name: 'SubmitPanel', query: { id: row.id, username: this.$route.query.parms } });
            // this.$router.push({ name: 'SubmitPanel', query: { id: "001", username: "SKY" } });
        }
    }

}
</script>
<script setup>
import { Search, Notebook } from '@element-plus/icons-vue';

</script>
<style >
@import url('https://fonts.googleapis.com/css?family=Poppins:400,400i,500,600,700|Ubuntu:400,500,700&display=swap');

* {
    padding: 0;
    margin: 0;
    box-sizing: border-box;
    font-size: 22px;
    font-family: 'Poppins', sans-serif;
}

:root {
    --linear-grad: linear-gradient(to right, #81aaf4, #0d737c);
    --grad-clr1: #81aaf4;
    --grad-clr2: #0d737c;
}

.bigBox {
    height: 100vh;
    background-color: #EDF0F2;
}

li {
    list-style: none;
}

/* 2.导航栏 */
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
    justify-content: flex-start;
    width: 200px;
}

.nav .left-nav .logo {
    width: 70px;
    border-radius: 35px;
    background-image: url(../assets/images/2.jpg);
    background-repeat: no-repeat;
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
    border-top: 1px solid blue;
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

.bigbox {
    height: 90vh;
    background-image: url(../assets/images/1.jpg);
}

.problemslistfield {
    position: absolute;
    float: left;
    left: 150px;
}

.leftpart {
    position: relative;
    top: 20px;
    width: 1000px;
    background-color: #ffffff;
    border: 1px solid #9285e8;
    border-radius: 20px;

}

/* 表格部分 */
.prelan {
    width: 600px;
    margin-top: 30px;
    margin-bottom: 20px;
    opacity: 1;
    background-color: #ffffff;
}

.prelan span {
    font-size: 30px;
}

.searchfield {
    width: 600px;
    margin: 0 auto;
    margin-bottom: 15px;
    margin-left: 10px;
}

.el-input__inner {
    height: 40px;
    font-size: 17px;
}

.el-table {
    width: 1000px;
    height: 450px;
    margin: 0 auto;
    margin-left: 10px;
    background: none;
}

.el-pagination {
    width: 200px;
    margin: 40px auto;
    margin-top: 30px;
    margin-left: 400px;
}

.is-active {
    width: 30px;
}

/* 右侧欢迎栏 */
.Hellopart {
    position: relative;
    top: 100px;
    right: 50px;
    float: right;
    /* background: linear-gradient(to bottom, #f4ebeb, #d3ddee); */
    /* background-color: rgb(248, 249, 250); */
    background: #ffffff;
    font-family: 'Poppins';
    border-radius: 10px;
    border: 1px solid #9285e8;
    width: 300px;
    height: 300px;

}

.Hellopart h2 {
    text-align: center;
    font-size: 30px;
    color: #5495c7;
    text-indent: 7px;
}

.Hellopart .prac {
    margin-top: 10px;
    text-indent: 7px;
}

.Hellopart .intro {
    margin-top: 10px;
    text-indent: 7px;
}

.Hellopart .status {
    margin-top: 10px;
    text-indent: 7px;
}
</style>