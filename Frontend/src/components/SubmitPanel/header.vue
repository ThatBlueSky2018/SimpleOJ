<template>
    <h3>    
        <logo></logo>
        <upBtn1></upBtn1>
        <upBtn2></upBtn2>
        <userName></userName>
    </h3>


</template>

<script>
    import logo from "./logo.vue";
    import upBtn1 from "./upBtn1.vue";
    import upBtn2 from "./upBtn2.vue";
    import userName from "./userName.vue";
    export default{
        components:{
            logo:logo,
            upBtn1:upBtn1,
            upBtn2:upBtn2,
            userName:userName
        }
    }
</script>

<style scoped>
h3{
    /* 大小指定 */
    width: 100%;
    height: 50px;
    float:top;
    position: relative;
    /* 指定格式 */
    border: 5px solid #999;
    text-align: center;
    line-height: 70px;
    box-sizing:content-box;
    border-left: 0px;
    border-right: 0px;
    border-top: 0px;
    border-bottom: 0px;
    margin: 0px 0px 0px 0px;
    padding: 0px 0px 0px 0px;
    box-shadow: 0px 5px 10px #888888;

}
</style>