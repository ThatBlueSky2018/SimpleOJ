<template>
    <div class="bigBox">
        <!-- 导航栏开始 -->
        <div class="nav">
            <div class="left-nav">
                <div class="logo"></div>
                <div class="OJName">SimpleOJ</div>
            </div>
            <div class="userchoices mychoices">
                <a @click="loginwarning">题目列表</a>
                <a @click="loginwarning">提交记录</a>
                <!-- 仅仅为了测试 -->
            </div>
            <div class="dropdown">
                <button class="dropbtn">用户昵称</button>
                <div class="dropdown-content">
                    <a @click="loginwarning">主页</a>
                    <a>登出</a>
                </div>
            </div>
        </div>
        <!-- 导航栏结束 -->
        <!-- 中间的图片开始 -->
        <!-- <div class="middle-pic">
    </div> -->
        <!-- 中间的图片结束 -->
        <!-- 登录注册部分开始 -->
        <div class="loginfield">
            <div class="container" id="container" ref="container">
                <div class="form-container sign-up-container">
                    <form action="#">
                        <h1>创建您的账号</h1>
                        <span>欢迎您进行注册</span>
                        <el-form ref="RegisterFormRef" :model="RegisterForm" :rules="rules" label-width="5px">
                            <el-form-item prop="username" label=" ">
                                <el-input type="text" placeholder="用户名" :suffix-icon="User"
                                    v-model="RegisterForm.username" />
                            </el-form-item>
                            <el-form-item prop="password" label=" ">
                                <el-input type="password" placeholder="密码" :suffix-icon="Lock"
                                    v-model="RegisterForm.password"></el-input>
                            </el-form-item>

                            <el-form-item prop="confirmpassword" label=" ">
                                <el-input type="password" placeholder="确认密码" :suffix-icon="Lock"
                                    v-model="RegisterForm.confirmpassword"></el-input>
                            </el-form-item>

                        </el-form>
                        <button @click="register">注册</button>
                    </form>
                </div>
                <div class="form-container sign-in-container">
                    <form action="#">
                        <h1>登录</h1>
                        <span>使用您的账号</span>
                        <el-form ref="LoginFormRef" :model="LoginForm" :rules="rules" label-width="5px">
                            <el-form-item prop="username" label=" ">
                                <el-input type="text" placeholder="用户名" :suffix-icon="User" v-model="LoginForm.username" />
                            </el-form-item>
                            <el-form-item prop="password" label=" ">
                                <el-input type="password" placeholder="密码" :suffix-icon="Lock"
                                    v-model="LoginForm.password"></el-input>
                            </el-form-item>
                        </el-form>
                        <button @click="login">登录</button>
                    </form>
                </div>
                <div class="overlay-container" id="overlayCon" ref="overlayCon">
                    <div class="overlay">
                        <div class="overlay-panel overlay-left">
                            <h1>欢迎回来!</h1>
                            <p>为了与我们保持联系，请使用您的个人信息登录</p>
                            <button>登录</button>
                        </div>
                        <div class="overlay-panel overlay-right">
                            <h1>欢迎加入本OJ!</h1>
                            <p>输入您的个人详细信息并开始我们的旅程</p>
                            <button>注册</button>
                        </div>
                    </div>
                    <button id="overlayBtn" ref="overlayBtn"></button>
                </div>
            </div>
        </div>
        <!-- 登录注册部分结束 -->
    </div>
</template>

<script>
export default {
    mounted() {
        const container = this.$refs.container;
        const overlayBtn = this.$refs.overlayBtn;

        overlayBtn.addEventListener('click', () => {
            container.classList.toggle('right-panel-active');
            overlayBtn.classList.remove('btnScaled');
            window.requestAnimationFrame(() => {
                overlayBtn.classList.add('btnScaled');
            });
        });
    },
    methods: {
        toggleOverlay() {
            const container = this.$refs.container;
            const overlayBtn = this.$refs.overlayBtn;

            container.classList.toggle('right-panel-active');
            overlayBtn.classList.remove('btnScaled');
            window.requestAnimationFrame(() => {
                overlayBtn.classList.add('btnScaled');
            });
        },
    },
}
</script>
<script setup>
import { Lock, User } from '@element-plus/icons-vue'
import api from '@/api/login.js'
import { reactive, ref } from 'vue';
import { ElMessage } from 'element-plus';
import { useRouter } from 'vue-router';
const LoginForm = reactive({
    username: '',
    password: ''
})
const LoginFormRef = ref('')
const RegisterFormRef = ref('')
const RegisterForm = reactive({
    username: '',
    password: '',
    confirmpassword: ''
})
const validateConfirmPassword = (rule, value, callback) => {
    if (value !== RegisterForm.password) {
        callback(new Error('Passwords do not match'));
    } else {
        callback();
    }
};
const rules = reactive({
    username: [
        { required: true, message: 'Please input username', trigger: 'blur' },
        { min: 3, max: 5, message: 'Length should be 3 to 5', trigger: 'blur' },
    ],
    password: [
        { required: true, message: 'Please input password', trigger: 'blur' },
        { min: 6, max: 18, message: 'Length should be 6 to 18', trigger: 'blur' },
    ],
    confirmpassword: [
        { required: true, message: 'Please input confirmpassword', trigger: 'blur' },
        { min: 6, max: 18, message: 'Length should be 6 to 18', trigger: 'blur' },
        { validator: validateConfirmPassword, trigger: 'blur' }, // 添加自定义验证函数
    ],
})

const router = useRouter()
//登录函数
const login = () => {
    LoginFormRef.value.validate((valid) => {
        if (valid) {
            api.loginApi(LoginForm).then(res => {
                console.log('login', res)
                if (res.status === 200) {//登录成功
                    ElMessage.success(res.message)//显示信息
                    router.push({ name: 'home', query: { parms: LoginForm.username } })//跳转新页面
                }
                else {
                    console.log("fail");
                }
            }).catch((error) => {
                console.log(error);
            })
        }
        else {
            return
        }
    })

}
//注册函数
const register = () => {
    RegisterFormRef.value.validate((valid) => {
        if (valid) {
            api.registerApi(RegisterForm).then(res => {
                if (res.status === 200) {//注册成功
                    ElMessage.success(res.message)//显示信息
                }
            }).catch(error => {
                console.log(error);
            })
        }
        else {
            return
        }
    })
}
const loginwarning = () => {
    ElMessage.error("请先登录")//显示信息
}
</script>
<style >
@import url('https://fonts.googleapis.com/css?family=Poppins:400,400i,500,600,700|Ubuntu:400,500,700&display=swap');

/* 1.整体 */
* {
    padding: 0;
    margin: 0;
    box-sizing: border-box;
    font-size: 22px;
    font-family: 'Poppins', sans-serif;
}

:root {
    --linear-grad: linear-gradient(to right, #81aaf4, #0d737c);
    --grad-clr1: #81aaf4;
    --grad-clr2: #0d737c;
}

.bigBox {
    height: 100vh;
    background-color: #EDF0F2;
}

li {
    list-style: none;
}

/* 2.导航栏 */
.nav {
    position: sticky;
    top: 0;
    z-index: 2;
    height: 70px;
    border-bottom: 1px solid #777777;
    background-color: #FFFFFF;
    line-height: 70px;
    box-shadow: 0px 2px 2px 1px rgb(21, 4, 4, .5);
}

.nav .left-nav {
    float: left;
    display: flex;
    justify-content: flex-start;
    width: 200px;
}

.nav .left-nav .logo {
    width: 70px;
    border-radius: 35px;
    background-image: url(../assets/images/2.jpg);
    background-repeat: no-repeat;
}

/* 导航栏的选项 */
.nav .userchoices {
    float: left;
    padding-left: 100px;
}

.nav .userchoices a {

    /* a属于行内元素 此时必须要转换 行内块元素 */
    display: inline-block;
    height: 70px;
    padding: 0 20px;
    font-size: 20px;
    color: #4c4c4c;
    text-decoration: none;
}

.nav a:hover {
    background-color: #eee;
    color: #ff8500;
}

/* 下拉列表 */
.dropbtn {
    width: 150px;
    background-color: #b7d5ec;
    color: black;
    padding: 16px;
    font-size: 20px;
    border: none;
    cursor: pointer;
    border-radius: 8px;
}

.dropdown {
    float: right;
    position: relative;
    right: 10px;
}

.dropdown-content {
    display: none;
    position: absolute;
    right: 0px;
    text-align: center;
    background-color: #f9f9f9;
    min-width: 150px;
    box-shadow: 0px 8px 16px 0px rgba(0, 0, 0, 0.2);
    z-index: 1;
}

.dropdown-content a {
    color: black;
    /* padding: 12px 16px; */
    text-decoration: none;
    display: block;
}

.dropdown-content a:hover {
    background-color: #f1f1f1
}

.dropdown:hover .dropdown-content {
    display: block;
}

.dropdown:hover .dropbtn {
    background-color: #3e8e41;
}


/* 3.中间的图片 */
.middle-pic {
    /* background-image: ; */
    /* 还没找到图片不好意思 */
    background: linear-gradient(to right, #2085f2, rgb(217, 250, 225));
    height: 200px;
}

/* 4.登录部分 */


/* 4.2用户登录主体部分 */


/* 4.3登录注册按键 */
.loginfield {
    width: 100%;
    height: 90vh;
    display: grid;
    place-content: center;
    background-image: url(../assets/images/coding.gif);
    position: fixed;
    /* background-repeat: no-repeat;
    background-position: center; */
}

.container {
    position: relative;
    width: 850px;
    height: 500px;
    background-color: #FFF;
    box-shadow: 25px 30px 55px #5557;
    border-radius: 13px;
    overflow: hidden;
}

.form-container {
    position: absolute;
    width: 60%;
    height: 100%;
    padding: 0px 40px;
    transition: all 0.6s ease-in-out;
}

.sign-up-container {
    opacity: 0;
    z-index: 1;
}

.sign-in-container {
    z-index: 2;
}

form {
    height: 100%;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    padding: 0px 50px;
}

.container h1 {
    font-size: 35px;
    color: var(--grad-clr1);
}

.container span {
    font-size: 18px;
}

.el-form {
    width: 125%;
    height: 50%;
}

.el-form-item {
    width: 100%;
}

.el-input__inner {
    height: 40px;
    font-size: 17px;
}

.infield {
    position: relative;
    margin: 8px 0px;
    width: 100%;
}

.infield1 {
    margin-top: 50px;
}

.container el-input {
    width: 100%;
    padding: 12px 15px;
    background-color: #f3f3f3;
    border: none;
    outline: none;
    font-size: 14px;
}

.container label {
    position: absolute;
    left: 50%;
    top: 100%;
    transform: translateX(-50%);
    width: 0%;
    height: 2px;
    background: var(--linear-grad);
    transition: 0.3s;
}

input:focus~label {
    width: 100%;
}




.container a {
    color: #333;
    font-size: 17px;
    text-align: center;
    text-decoration: none;
    margin: 15px 0px;
}



.container button {
    border-radius: 20px;
    border: 1px solid var(--grad-clr1);
    background-color: var(--grad-clr2);
    color: #FFF;
    font-size: 14px;
    font-weight: bold;
    padding: 12px 45px;
    letter-spacing: 1px;
    text-transform: uppercase;
}

.form-container button {
    margin-top: 17px;
    transition: 80ms ease-in;
}

.form-container button:hover {
    background: #FFF;
    color: var(--grad-clr1);
}

.overlay-container {
    position: absolute;
    top: 0;
    left: 60%;
    width: 40%;
    height: 100%;
    overflow: hidden;
    transition: transform 0, 6s ease-in-out;
    z-index: 9;
}

#overlayBtn {
    cursor: pointer;
    position: absolute;
    left: 50%;
    top: 304px;
    transform: translateX(-50%);
    width: 143.67px;
    height: 40px;
    border: 1px solid #FFF;
    background: transparent;
    border-radius: 20px;
}

.overlay {
    position: relative;
    background: var(--linear-grad);
    color: #FFF;
    left: -150%;
    height: 100%;
    width: 250%;
    transition: transform 0.6s ease-in-out;

}

.overlay-panel {
    position: absolute;
    display: flex;
    align-items: center;
    justify-content: center;
    flex-direction: column;
    padding: 0px 40px;
    text-align: center;
    height: 100%;
    width: 340px;
    transition: 0.6s ease-in-out;
}

.overlay-left {
    right: 60%;
    transform: translateX(-12%);
}

.overlay-right {
    right: 0;
    transform: translateX(0%);
}

.overlay-panel h1 {
    color: #FFF;

}

.container p {
    font-size: 14px;
    font-weight: 300;
    line-height: 20px;
    letter-spacing: 0.5px;
    margin: 25px 0px 35px;
}

.overlay-panel button {
    border: none;
    background-color: transparent;
}

.right-panel-active .overlay-container {
    transform: translateX(-150%);
}

.right-panel-active .overlay {
    transform: translateX(50%);
}

.right-panel-active .overlay-left {
    transform: translateX(25%);
}

.right-panel-active .overlay-right {
    transform: translateX(35%);
}

.right-panel-active .sign-in-container {
    transform: translateX(20%);
    opacity: 0;
}

@keyframes show {

    0%,
    50% {
        opacity: 0;
        z-index: 1;
    }

    50.1%,
    100% {
        opacity: 1;
        z-index: 5;
    }
}

.right-panel-active .sign-up-container {
    transform: translateX(66.7%);
    opacity: 1;
    z-index: 5;
    animation: show 0.6s;
}

@keyframes scaleBtn {
    0% {
        width: 143.67px;
    }

    50% {
        width: 250px;
    }

    100% {
        width: 143.67px;
    }
}

.btnScaled {
    text-align: center;
    animation: scaleBtn 0.6s;
}
</style>