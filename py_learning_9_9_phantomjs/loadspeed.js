let page = require('webpage').create(),
    system = require('system'),
    t, address;

if (system.args.length === 1) {
    console.log('Usage: loadspeed.js <some URL>');
    phantom.exit();
}
t = Date.now();
address = system.args[1];
page.open(address, function (status) {
    if (status !== 'success') {
        console.log('PAIL to load the address');
    } else {
        t = Date.now() - t;
        console.log('Loading' + system.arg[1]);
        console.log('Loading time' + t + 'msec');   //加载时间
    }
    phantom.exit();
});