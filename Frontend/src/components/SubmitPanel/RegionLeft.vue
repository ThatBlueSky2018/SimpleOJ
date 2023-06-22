<template>
    <div class="a" id="questionRegion">
        <p class="title1">题目描述：</p>
        <p class="content1" id="description"></p>
        <p class="title1">输入：</p>
        <p class="content1" id="input"></p>
        <p class="title1">输出：</p>
        <p class="content1" id="output"></p>
        <p class="title1">输入样例：</p>
        <p class="content2" id="inputExample"></p>
        <p class="title1">输出样例：</p>
        <p class="content2" id="outputExample"></p>
        <!-- <p id="id_saver" v-cloak>{{ $route.query.id }}</p> -->

    </div>
</template>

<script>
export default {
    components: {
    }
}
</script>

<style scoped>
.title1 {
    color: black;
    font-size: larger;
    font-weight: bold;
    position: relative;
    left: 10px;
}

.content1 {
    text-align: left;
    margin-left: 30px;
}

#inputExample {
    margin: 4%;
    background-color: rgb(227, 227, 227);
}

#outputExample {

    margin: 4%;

    background-color: rgb(227, 227, 227);
    ;
}

.a {
    /* 大小指定 */
    width: 40%;
    height: 98%;
    position: relative;
    float: left;
    float: top;
    /* 指定格式 */
    border-radius: 10px;
    box-sizing: content-box;
    margin: 7px 0px 0px 100px;
    padding: 0px 0px 0px 0px;
    background-color: rgb(255, 255, 255);
    box-shadow: 0px 0px 10px;
}
</style>