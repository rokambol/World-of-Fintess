         ___        ______     ____ _                 _  ___  
        / \ \      / / ___|   / ___| | ___  _   _  __| |/ _ \ 
       / _ \ \ /\ / /\___ \  | |   | |/ _ \| | | |/ _` | (_) |
      / ___ \ V  V /  ___) | | |___| | (_) | |_| | (_| |\__, |
     /_/   \_\_/\_/  |____/   \____|_|\___/ \__,_|\__,_|  /_/ 
 ----------------------------------------------------------------- 


command use:
sudo pip3 install django==1.11
django-admin startproject world_of_fintess .
python3 manage.py makemigrations
python3 manage.py migrate

$(function() {
var body = $(‘body’);
var backgrounds = new Array(
‘url(image1.jpg)’,
‘url(image2.jpg)’
);
var current = 0;

function nextBackground() {
body.css(
‘background’,
backgrounds[current = ++current % backgrounds.length]
);

setTimeout(nextBackground, 10000);
}
setTimeout(nextBackground, 10000);
body.css(‘background’, backgrounds[0]);
});

https://media1.tenor.com/images/52ee24b6e1634cb072cc4dbdf51013ab/tenor.gif?itemid=4469244
https://media.tenor.com/images/3ba6571ba6610f4fa59b2cd68e8eb81c/tenor.gif