<script>
// import header_ from "./components/header.vue"
import RegionMain from "../components/JudgeList/RegionMain.vue"
import header_ from "../components/SubmitPanel/MyNav.vue"
import utils from "../api/utils.js";
export default {
    data() {

        return {
            Tusername: '',
            id: ''
        }
    },
    mounted() {
        const username1 = this.$route.query.username
        this.Tusername = username1;
        const id1 = this.$route.query.id
        this.id = id1
        utils.loadJudgeInfromation(this.id, this.Tusername);
    }
    ,
    components: {
        header_: header_,
        RegionMain: RegionMain,
    }
}
</script>

<template>
    <header_></header_>
        <RegionMain></RegionMain>
</template>

<style>
body {
    margin: 0;
    background-color: rgb(214, 223, 223);
    background-image: url(../assets/images/1.jpg);
}

template {
    margin: 0;
}
</style>
