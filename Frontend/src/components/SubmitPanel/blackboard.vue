<template>
    <!-- <textarea class="h" id="codeRegion"></textarea>> -->
    <!-- <code-input></code-input> -->
    <Vue3Codemirror />
</template>

<script>
import utils from "../../api/utils.js";
// import hljs from 'highlight.js';
// import CodeInput from "../../components/SubmitPanel/CodeInput.vue";
import Vue3Codemirror from '../../components/SubmitPanel/Vue3Codemirror.vue';
console.log("执行了");
export default {
    data() {
        
        return {
            Tusername: 'SKY',
            id: '001'
        }
    },
    mounted() {
        const username1 = this.$route.query.username
        this.Tusername = username1;
        const id1 = this.$route.query.id
        this.id = id1
        utils.loadQuestion(this.id);
    }
    ,
    components: {
        Vue3Codemirror,
    }
}
</script>

<style scoped>
.h {
    /* 大小指定 */
    width: 80%;
    height: 60%;
    position: relative;
    float: top;
    top: 2%;
    left: 10%;
    /*文字样式 */
    color: azure;
    overflow: visible;
    word-break: break-all;
    /* 指定格式 */
    border-radius: 10px;
    box-sizing: content-box;
    background-color: rgb(0, 0, 0);
    /* background-color:blueviolet; */
    margin: 10px 0px 0px 0px;
    padding: 0px 0px 0px 0px;
}
</style>