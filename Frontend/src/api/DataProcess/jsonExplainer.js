function jsonExplainer(data){
    //1.使用换行符，冒号和逗号进行划分
    var words=data.split(/[:\n{}]/);
    //2.删除所有的空格和空字符
    var ans=[];
    for(var i=0;i<words.length;i++){
        if(words[i]!=""){
            // ans.push(words[i].split(/["]/)[1]);
            if(words[i][0]=="\""){
            words[i]=words[i].split("\",")[0];
            words[i]=words[i].split("\"")[1];
            }else{
            words[i]=words[i].split(",")[0];
            }
            ans.push(words[i]);
        }
    }
    return ans; 
}
function getFromKey(jsonArr,key){
    for(var i=0;i<jsonArr.length;i+=2){
        if(jsonArr[i]==key){
            return jsonArr[i+1];
        }
    }
    return "NOT FOUND";
}
export default{
    jsonExplainer,
    getFromKey
}