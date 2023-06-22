<template>

    <div class="f">
    <div class="line">.
    </div>
    
    <blackboard id="codeRegion"></blackboard>
    <span><submitBtn></submitBtn></span>
    </div>
</template>

<script>
    import submitBtn from "./submitBtn.vue";
    import blackboard from "./blackboard.vue";
    import dropOutBtn from "./dropOutBtn.vue";

    export default{
        components:{
            submitBtn:submitBtn,
            blackboard:blackboard,
            dropOutBtn:dropOutBtn
        }
    }
</script>

<style scoped>
.line{
    border-color:black;
    height:1px;
    width: 100%;
    border: 2px solid #000000;
    border-left: 0px;
    border-right: 0px;
    border-top: 0px;
    color: aliceblue;
    position: absolute;
    bottom: 25%;
}
.f{
    /* 大小指定 */
    width: 100%;
    height:78%;
    position: relative;
    float: left;
    float: top;
    /* 指定格式 */
    border-radius: 10px;
    box-sizing:content-box;
    background-color:rgb(255, 255, 255);
    margin: 10px 0px 0px 0px;
    padding: 0px 0px 0px 0px;
    box-shadow: 0px 0px 10px ;
    overflow: auto;
}
</style>