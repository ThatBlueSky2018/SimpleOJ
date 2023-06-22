//封装axios
import axios from 'axios'
import { ElMessage } from 'element-plus'

//创建axios实例
const Service = axios.create({
    //配置baseURL地址
    baseURL: 'http://127.0.0.1:8000',
    //定义统一的请求头
    header: {
        'Content-Type': "application/json;charset=UTF-8"
    },
    //配置请求超时时间
    timeout: 5000
})
//请求拦截器
Service.interceptors.request.use((config) => {
    //配置请求头，token需要加上Bearer，否则要拼接
    // config.headers['Authorization'] = 'Bearer ' + getToken();
    // config.headers.comon['Authorzation'] = window.sessionStorage.getItem('token') === null ? null : window.sessionStorage.getItem('token')
    return config
})
//响应拦截器
Service.interceptors.response.use((response) => {
    //获取接口返回结果
    const res = response.data
    if (res.status === 0) {//0代表成功
        return res;
    }
    else {
        //ElMessage.error(res.message || "网络异常")//写出返回信息，不会返回时写网络异常
        return res
    }
})
//暴露示例
export default Service