if (/Android (\d+\.\d+)/.test(navigator.userAgent)) {
    var version = parseFloat(RegExp.$1);
    if (version > 2.3) {
        var phoneScale = parseInt(window.screen.width) / 750;
        document.write('<meta name="viewport" content="width=750, minimum-scale = ' + phoneScale + ', maximum-scale = ' + phoneScale + ', user-scalable=no, target-densitydpi=device-dpi">');
    } else {
        document.write('<meta name="viewport" content="width=750, user-scalable=no, target-densitydpi=device-dpi">');
    }
} else {
    document.write('<meta name="viewport" content="width=750, user-scalable=no, target-densitydpi=device-dpi">');
}