let user = document.querySelector("#name")
user.oninput = function(){
    window.localStorage.setItem("username", user.value)
}
if(window.localStorage.length == 0){
    window.localStorage.setItem("opened", true)
    alert("Welcome!!!")
} else {
    user.value = window.localStorage.getItem("username")
}