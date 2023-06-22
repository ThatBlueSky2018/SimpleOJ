<script>
export default {
  methods: {
    clickDrop(event) {
      console.log("ok");
      var ele = document.getElementById("dropBtn1");
      ele.innerText = event.target.innerText;
    },
  },
};
</script>

<template>
  <div class="dropdown">
    <!-- 下拉按钮触发器 -->
    <button id="dropBtn1" class="dropdown-trigger">选取语言</button>

    <!-- 下拉内容 -->
    <div class="dropdown-content">
      <a @click="clickDrop">C</a>
      <a @click="clickDrop">C++</a>
    </div>
  </div>
</template>

<style scoped>
.dropdown {
  position: relative;
  display: inline-block;
}

/* 下拉按钮触发器样式 */
.dropdown-trigger {
  background-color: #f1f1f1;
  color: #333333;
  padding: 8px;
  border: none;
  cursor: pointer;
  border-radius: 20% 20% 0 0;
}

/* 下拉内容样式（默认隐藏） */
.dropdown-content {
  display: none;
  position: absolute;
  background-color: #f9f9f9;
  min-width: 160px;
  box-shadow: 0px 8px 16px 0px rgba(0, 0, 0, 0.2);
  z-index: 1;
}

/* 下拉内容项样式 */
.dropdown-content a {
  color: #333333;
  padding: 12px 16px;
  text-decoration: none;
  display: block;
}

/* 下拉内容项悬停样式 */
.dropdown-content a:hover {
  background-color: #f1f1f1;
}

/* 显示下拉内容 */
.dropdown:hover .dropdown-content {
  display: block;
}
</style>
