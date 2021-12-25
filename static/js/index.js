//for getting a no data alert random msg, when there are no records
window.onload = function alert(){
//get random sentence from array and send it to html
let sentence = ["You got no case.","There are no records in your possession.","No todos for now.","Yey! You all got it covered.", "You got no history."];
let randSentence = sentence[Math.floor(Math.random() * sentence.length)];

/*console.log(randSentence)*/
const $ = id=> document.getElementById(id);
let alert_box = $("no_data_alert")

if (!alert_box){return;}
else{
    alert_box.innerText = randSentence
}

}

// hide menu on scroll

var prevScrollpos = window.pageYOffset;
window.onscroll = function() {
var currentScrollPos = window.pageYOffset;
  if (prevScrollpos > currentScrollPos) {
    document.getElementById("navbar").style.top = "0";
  } else {
    document.getElementById("navbar").style.top = "-80px";
  }
  prevScrollpos = currentScrollPos;
}

//Smooth Scrolling

window.scroll({
    top: 0, 
    left: 0, 
    behavior: 'smooth'
  });