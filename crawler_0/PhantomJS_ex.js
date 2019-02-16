// console.log('Hello, world!');

// 网页截图
var page = require('webpage').create();
page.open('https://music.163.com/', function(status) {
  console.log("Status: " + status);
  if(status === "success") {
    window.setTimeout(function(){
      page.render('163music.jpeg',{format: 'jpeg', quality: '100'});
      phantom.exit();
    },10000);
  }
});


// displays the system’s environment variables
var system = require('system'),
    env = system.env,
    key;

for (key in env) {
    if (env.hasOwnProperty(key)) {
        console.log(key + '=' + env[key]);
    }
}
phantom.exit();

