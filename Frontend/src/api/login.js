import login from './request'
const loginApi = (data) => {

    return login.post({
        url: '/user/login/',
        data
    })
}
const registerApi = data => {
    return login.post({
        url: '/user/register/',
        data
    })
}

export default {
    loginApi,
    registerApi
}