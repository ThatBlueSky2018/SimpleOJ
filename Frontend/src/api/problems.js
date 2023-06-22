import axios from "axios"

function loadProblems() {

    var res = null
    axios.get("http://127.0.0.1:8000/problem/problems/").then(function (response) {
        res = response;
        console.log(res)
    }).catch(error => {
        console.log("Error happened")
        console.log(error);
    })
    return res
}
export default {
    loadProblems,
}