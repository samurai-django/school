//
// function sayHello(){
//     alert("Hello!");
// }
// function sayGoodbye(){
//     alert("Bye!");
// }
// const p = document.getElementById('update_cart');
// p.addEventListener('click', sayHello, false);
// p.addEventListener('click', sayGoodbye, false);




// function myFunction() {
//     // alert('Button was clicked!');
//     console.log('button was clicked')
// }




const updateBtns = document.getElementsByClassName("update_cart");
for(var i = 0; i < updateBtns.length; i++){
    updateBtns[i].addEventListener('click', function(){
        var courseId = this.dataset.courses
        var action = this.dataset.action
        console.log('courseId:', courseId, 'Action:', action)
        console.log('USER:', user)
    })
}

