<template>
    <div class="a">
        <sub1></sub1>
        <sub2></sub2>
    </div>
</template>

<script>
    import sub1 from "./RegionSubRight1.vue"
    import sub2 from "./RegionSubRight2.vue"
    import dropOutBtn from "./dropOutBtn.vue"
    export default{
        components:{
            sub1:sub1,
            sub2:sub2,
            dropOutBtn:dropOutBtn
        }
    }
</script>

<style scoped>
.a{
    /* 大小指定 */
    width: 40%;
    height:98%;
    position: relative;
    float: left;
    float: top;
    /* 指定格式 */
    box-sizing:content-box;
    /* background-color: aqua; */
    margin: 0px 0px 100px 15px;
    padding: 0px 0px 0px 0px;

}
</style>