<template>
    <div class="e">
        <div class="b">
            信息
        </div>
        <div class="c" id="memoryLimit">
            空间限制：
        </div>
        <div class="c" id="timeLimit">
            时间限制：
        </div>
        <dropOutBtn/>
        <!-- <div class="c"> -->
            <!-- 通过率：0/0 -->
        <!-- </div> -->
    </div>
</template>

<script>
    import dropOutBtn from "./dropOutBtn.vue"

    export default{
        components:{
            dropOutBtn:dropOutBtn
        }
    }
</script>

<style scoped>
.e{
    /* 大小指定 */
    width: 100%;
    height:20%;
    position: relative;
    float: left;
    float: top;
    /* 指定格式 */
    border-radius: 10px;
    box-sizing:content-box;
    background-color:rgb(255, 255, 255);
    /* background-color:blueviolet; */
    margin: 10px 0px 0px 0px;
    padding: 0px 0px 0px 0px;
    box-shadow: 0px 0px 10px ;
}
.b{
    line-height: 50px;
    padding-left: 10px;
    font-size: 20px;
    font-weight: lighter;
}
.c{
    line-height: 25px;
    padding-left: 30px;
    font-size: 20px;
    font-weight:bolder;
}
</style>