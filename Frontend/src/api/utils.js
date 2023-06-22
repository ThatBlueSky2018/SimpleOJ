
import axios from 'axios';
import jsonExplainer from "../api/DataProcess/jsonExplainer.js";
//向服务器端发送请求，并渲染到题目列表上：
function loadQuestion(id) {
    axios.get(" http://127.0.0.1:8000/problem/problemDetail/" + id+"/").then(function (response) {
        //var arr=jsonExplainer.jsonExplainer(JSON.stringify(response.data));
        //加载ID和标题：
        var arr = response.data;
        console.log(arr);
        var id=0;
        for(var i=0;i<arr['id'].length;i++){id=id+arr['id'].charCodeAt(i);}
        var value =  arr['title'];
        var ele = document.getElementById("idandtitle");
        ele.innerHTML = value;

        //加载其他内容：
        var keys = ["timeLimit", "memoryLimit",
            "description", "input", "output", "inputExample", "outputExample"];
        for (var i = 0; i < keys.length; i++) {
            // var value=jsonExplainer.getFromKey(arr,keys[i]);
            var value = arr[keys[i]];
            if (keys[i] === "timeLimit") { value = "时间限制：" + value +"ms" }
            if (keys[i] === "memoryLimit") { value = "内存限制：" + value +"MB"}
            var ele = document.getElementById(keys[i]);
            ele.innerHTML = value;
        }
    }).catch(function (error) {
        console.log("错误发生了");
        console.log(error);
    })
}
//提交代码
function submitCode(name,id) {
    var ele = document.getElementById("saver");
    var _username = name;
    var _problemID = id;
    var _code = ele.value;
    console.log("code is:")
    console.log(_code)
    axios.post("http://127.0.0.1:8000/judgeStatus/judgeStatusPut/", {
        "username": _username,
        "problemID": _problemID,
        "language": "C++",
        "code": _code
    }).then(function (response) {
        // var data=eval(response.data);
        var data = response.data;
        alert(data["message"]);//显示警示框
    }).catch(function (error) {
        console.log("错误发生了");
        console.log(error);
    })
}
//加载判题信息
function loadJudgeInfromation(id,name) {
    console.log("loadJudgeInfromation调试，"+" "+name);
    axios.get(" http://127.0.0.1:8000/judgeStatus/judgeStatus/?search="+name+"+"+id).then(function (response) {
        //信息显示
        console.log("URL是："+"http://127.0.0.1:8000/judgeStatus/judgeStatus/?search="+name+"+"+id);
        var arr = response.data;
        console.log(arr);
        var value = "";

        for (var i = 0; i < arr.length; i++) {
            var color="red";var result="NO RESULT";
            if(arr[i]["result"]==-1){color="rgb(5,34,66)";}
            if(arr[i]["result"]==-2){color="blue";}
            if(arr[i]["result"]==-3){color="rgb(232,76,61)";}
            if(arr[i]["result"]==-4){color="rgb(251,219,20)";}
            if(arr[i]["result"]==-5){color="red";}
            if(arr[i]["result"]==-6){color="red";}
            if(arr[i]["result"]==1){color="rgb(5,34,66)";}
            if(arr[i]["result"]==2){color="rgb(5,34,66)";}
            if(arr[i]["result"]==3){color="rgb(255,115,2)";}
            if(arr[i]["result"]==4){color="rgb(156,61,207)";}
            if(arr[i]["result"]==5){color="red";}
            if(arr[i]["result"]==-5){color="rgb(83,196,26)";}

            value = value+"<li style="+"\"border-left: 4px solid "+color+";"+"top:"+(i*50+50)+"px;"+"\">";

            if(arr[i]["result"]==-1){color="rgb(5,34,66)";result="PENDING";}
            if(arr[i]["result"]==-2){color="blue";result="JUDGINNG";}
            if(arr[i]["result"]==-3){color="rgb(232,76,61)";result="WRONG_ANSWER";}
            if(arr[i]["result"]==-4){color="rgb(251,219,20)";result="COMPILE_ERROR";}
            if(arr[i]["result"]==-5){color="red";result="PRESENTATION_ERROR";}
            if(arr[i]["result"]==-6){color="red";result="WAITING";}
            if(arr[i]["result"]==1){color="rgb(5,34,66)";result="TLE";}
            if(arr[i]["result"]==2){color="rgb(5,34,66)";result="TLE";}
            if(arr[i]["result"]==3){color="rgb(255,115,2)";result="MLE";}
            if(arr[i]["result"]==4){color="rgb(156,61,207)";result="RUNTIME_ERROR";}
            if(arr[i]["result"]==5){color="red";result="SYSTEM_ERROR";}
            if(arr[i]["result"]==-5){color="rgb(83,196,26)";result="ACCEPT";}

            value = value + "<span id=\"id1\" style=\"color:"+color+";\">" + result + "</span>"
            value = value + "<span id=\"id2\" style=\"color:"+"black"+";\">" + arr[i]["username"] + "</span>"
            value = value + "<span id=\"id3\" style=\"color:black;\">" + arr[i]["language"] + "</span>"
            value = value + "<span id=\"id4\" style=\"color:black;\">" + arr[i]["memory"] + "KB</span>"
            value = value + "<span id=\"id5\" style=\"color:black;\">" + arr[i]["time"] + "ms</span>"
            value = value + "<span id=\"id6\" style=\"color:black;\">" + arr[i]["submitTime"].substr(0, 10)+" "+arr[i]["submitTime"].substr(11, 8)+ "</span>"
            value += "</li>";
        }
        var ele = document.getElementById("Judgelist");
        ele.innerHTML = value;
    }).catch(function (error) {
        console.log("错误发生了");
        console.log(error);
    })
}
//彩色渲染代码：
function renderCode(){
    
}
export default {
    loadQuestion,
    submitCode,
    loadJudgeInfromation,
    renderCode
}
