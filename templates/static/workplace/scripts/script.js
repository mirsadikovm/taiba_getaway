document.querySelector(".nav_reg-item").addEventListener("click", function (e) {
  var sign = document.querySelector("#btn");
  sign.style.display = "none";
});
let btn = document.querySelector(".modal__back");
btn.onclick = function () {
  document.querySelector(".modal").style.display = "none";
};
let burger = document.querySelector(".burger");
burger.onclick = function () {
  document.querySelector(".nav_content").style.transform = "translateX(0)";
};
let close = document.querySelector(".close_mod");
close.onclick = function () {
  document.querySelector(".nav_content").style.transform = "translateX(-100%)";
};

function updateServerTime() {
  $.getJSON('/server-time/', function(data) {
    $('#server-time').text(data.server_time);
  });
}

$(document).ready(function() {
  updateServerTime();
  setInterval(updateServerTime, 1000);
});