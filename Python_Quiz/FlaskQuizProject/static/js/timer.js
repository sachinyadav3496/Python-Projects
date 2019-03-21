var hour = 0;
var minutes = 0;
var seconds = 0;

function count(){
    if ( seconds >= 60 ){
        seconds = 0;
        minutes += 1; 
        if (minutes >= 60 ){
            minutes = 0;
            hour += 1;
        }
    } else {  seconds += 1; }  
}

setInterval(function(){
var t_s = ''
var t_m  = ''
var t_h = ''
    count();
    if ( seconds <= 9 )  { t_s += '0'+seconds; } else { t_s = seconds; }
    if ( minutes <= 9 )  { t_m += '0'+minutes; } else { t_m = minutes; }
    if ( hour <= 9 ) { t_h += '0' + hour; } else { t_h = hour; }
    document.querySelector("#timer").innerHTML = "<h1>"+t_h+":"+t_m+":"+t_s+"</h1>"
},1000)
