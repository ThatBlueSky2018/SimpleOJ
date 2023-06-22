<template>
  <h3>
    <TextShower1></TextShower1>
    <TextShower1></TextShower1>
    <upBtn3></upBtn3>
  </h3>
</template>

<script>
import TextShower1 from "./TextShower1.vue";
import upBtn3 from "./upBtn3.vue";
export default {
  components: {
    TextShower1: TextShower1,
    upBtn3: upBtn3,
  },
};
</script>

<style scoped>
h3 {
  /* 大小指定 */
  width: 100%;
  height: 70px;
  float: top;
  position: relative;
  /* 指定格式 */
  border: 1px solid #000000;
  text-align: center;
  line-height: 70px;
  box-sizing: content-box;
  border-left: 0px;
  border-right: 0px;
  border-top: 0px;
  margin: 0px 0px 0px 0px;
  background-color: #ffffff;
}
</style>
