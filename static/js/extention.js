/*

 author: Zehua Yu

 function : picture animation

 */

window.onload = function () {

    var images = document.getElementsByTagName('img');
    var pos = 3;
    var len = images.length;


    setInterval(function () {

        images[pos].style.display = 'none';
        pos = ++pos == len ? 3 : pos;
        images[pos].style.display = 'inline';

    }, 5000);

};