<template id="ragionMain">
    <div class="class1">
        <pre>状态             提交者     使用语言    内存使用    总耗时    提交时间</pre>
        <ul id="Judgelist">
            <li>列表1</li>
            <li>列表2</li>
            <li>列表3</li>
        </ul>
    </div>

</template>

<script>

export default {
    components: {
    }
}
</script>

<style>
#id1 {
    float: left;
    position: absolute;
    left: 10px;
}

#id2 {
    float: left;
    position: absolute;
    left: 250px;
}

#id3 {
    float: left;
    position: absolute;
    left: 400px;
}

#id4 {
    float: left;
    position: absolute;
    left: 550px;
}

#id5 {
    float: left;
    position: absolute;
    left: 700px;
}

#id6 {
    float: left;
    position: absolute;
    left: 780px;
    font-size: smaller;
}

pre {
    position: relative;
    left: 0px;
    height: 20px;
    line-height: 50px;
    font-size: xx-large;
    text-align: center;
    color: rgb(135, 135, 135);
}

.class1 {
    /* 大小指定 */
    width: 80%;
    height: 700px;
    position: relative;
    top: 30px;
    left: 10%;
    /* 样式 */
    background-color: rgb(251, 251, 251);
    border-radius: 10px;
    /* 指定格式 */
    box-sizing: content-box;
    margin: 0px 0px 0px 0px;
    padding: 0px 0px 0px 0px;
    box-shadow: 0px 0px 10px;
    overflow:  auto;

}

li {
    width: 84%;
    height: 40px;
    line-height: 40px;
    text-align: center;
    font-size: x-large;
    position: absolute;
    left: 10%;
    margin-top: 30px;
    margin-bottom: 30px;
    border: 1px solid #000000;
    list-style: none;
}

li:nth-child(odd) {
    background-color: rgb(199, 199, 199);
}

li:nth-child(even) {
    background-color: rgb(236, 236, 236);
}</style>