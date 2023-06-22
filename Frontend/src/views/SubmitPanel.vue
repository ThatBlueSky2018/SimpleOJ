<script>
// import header_ from "./components/header.vue"
import header2_ from "../components/SubmitPanel/header2.vue"
import RegionMain from "../components/SubmitPanel/RegionMain.vue"
import RegionLeft from "../components/SubmitPanel/RegionLeft.vue"
import header_1 from "../components/SubmitPanel/MyNav.vue"

export default {
  components: {
    header_: header_1,
    header2_: header2_,
    RegionMain: RegionMain,
    RegionLeft: RegionLeft
  }
}
</script>

<template>
  <header_></header_>
  <header2_></header2_>
  <RegionMain></RegionMain>
</template>

<style>
body {
  margin: 0;
}

template {
  margin: 0;
}
</style>
