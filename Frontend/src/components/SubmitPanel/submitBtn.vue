<template>
    <button @click="submitClick">提交代码</button>
</template>

<script>
import utils from "../../api/utils.js";
export default {
    methods: {
        submitClick() {
            utils.submitCode(this.$route.query.username,this.$route.query.id);
        }
    }
}
</script>

<style scoped>
button {
    /* 大小指定 */
    width: 60%;
    height: 40px;
    /* 位置指定 */
    position: absolute;
    left: 0px;
    bottom: 50px;
    margin-left: 20%;
    /* 指定格式 */
    background-color: green;
    line-height: 50px;
    border-radius: 10px;
    box-sizing: content-box;
    /* 指定字体 */
    font-size: 7;
    line-height: 40px;
    font-weight: lighter;
    color: aliceblue;
    text-align: center;
    font-size: 20px;
}
button:hover {
    background-color:rgb(135, 238, 126);
}
</style>
