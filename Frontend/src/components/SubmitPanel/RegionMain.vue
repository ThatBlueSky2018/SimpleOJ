<template>
    <div class="mainRegion">
        <RegionLeft></RegionLeft>
        <RegionRight></RegionRight>
    </div>
</template>

<script>
    import RegionLeft from "./RegionLeft.vue";
    import RegionRight from "./RegionRight.vue";
    export default{
        components:{
            RegionLeft:RegionLeft,
            RegionRight:RegionRight
        }
    }
</script>

<style scoped>
.mainRegion{
    /* 大小指定 */
    width: 100%;
    height:700px;
    float: top;
    position: relative;
    /* 指定格式 */
    box-sizing:content-box;
    margin: 0px 0px 0px 0px;
    padding: 0px 0px 0px 0px;
    /* background-color: rgb(214, 223, 223);    */
    background-image: url(../../assets/images/1.jpg);
}
.RegionLeft{
    animation: scale 5s ease-in-out;
}
@keyframes scale{
    from {  height: 0; }
    to { height: 100px; }
}
</style>