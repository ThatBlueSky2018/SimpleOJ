<template>
    <button @click="JumpintoList">查看提交记录</button>
</template>
    
<script>
//数据传输：
export default {

    methods: {
        JumpintoList() {
            console.log("user name is:"+ this.$route.query.username);
            this.$router.push({ name: 'JudgeList', query: { id: this.$route.query.id, username: this.$route.query.username } })
        }
    }
}

</script>

<style scoped>
button {
    /* 大小指定 */
    width: 150px;
    height: 60%;
    /* 位置指定 */
    position: absolute;
    right: 70px;
    top: 10px;
    /* 指定格式 */
    background-color: #1f9aff;
    line-height: 50px;
    border: 3px solid #1f9aff;
    border-radius: 10px;
    box-sizing: content-box;
    /* 指定字体 */
    font-size: 7;
    line-height: 40px;
    font-weight: lighter;
    color: aliceblue;
}

/* 按钮颜色变化： */
button:hover {
    background-color: aquamarine;
}

button:active {
    background-color: brown;
}
</style>