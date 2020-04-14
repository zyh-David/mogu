var rpc = function(url,method,params,callback){
    axios.post(url,{
        "jsonrpc": "2.0",
        "method" : method,
        "params" : params,
        "id"     : 1
    }).then(response=>{
        callback(response.data.result);
    }).catch(error=>{
        console.log(error.response);
    });
}
