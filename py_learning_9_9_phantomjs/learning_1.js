var page = require('webpage').create();
page.open('http://cnblogs.com/qiyeboy/', function (status){
    console.log("Status: " + status);
    if (status === "success"){
        page.render('qiye.png');        //截图
    }
    phantom.exit();
});

