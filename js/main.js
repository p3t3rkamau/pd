setTimeout(function(){
    document.getElementById("loader").style.display = "none";
    document.getElementById("main-content").style.display = "block";
}, 1000);

const revealSideBar = document.querySelector('.side-bar');
const menuIcon = document.querySelector('.icon');
menuIcon.addEventListener('click', function (){
    revealSideBar.style.display = 'block'
});

const close = document.querySelector('.side-bar');
const closeIcon = document.querySelector('#close-window');
closeIcon.addEventListener('click', function (){
    close.style.display = 'none'
});

const loginFirstName = document.querySelector('.first-login-page');
const Page2  = document.querySelector('.second-page')
const signBtn = document.querySelector('.sign-up-btn');
const UserName = document.querySelector('.userName');
const profileName = document.querySelector('#profile');
const phoneNumber = document.querySelector('.phone-no');




signBtn.addEventListener('click', function (){
    if (UserName.value == 0){
        UserName.style.borderColor = 'red';
        document.querySelector('.username-error').innerHTML = 'Username Required'
    }
    else if(phoneNumber.value == 0){
        document.querySelector('.phone-no-error').innerHTML = 'Phone Number Required'
        phoneNumber.style.borderColor = 'red';

    }
    else if (isNaN(phoneNumber.value)){
        
        document.querySelector('.phone-no-error').innerHTML = 'Enter Numeric Value Only'
        phoneNumber.style.borderColor = 'red';
         
    }
    else if (phoneNumber.value.length < 9){
        phoneNumber.style.borderColor = 'red';
        document.querySelector('.phone-no-error').innerHTML = 'Number Must Be Ten Characters Long'
    }
    else{
        loginFirstName.style.display = 'none'
        Page2.style.display = 'block'
        profileName.innerHTML = UserName.value;
    } 
});


const signInForm = document.querySelector('#sign-in');
const registerForm  = document.querySelector('#register')
const createAccountBtn = document.querySelector('#account');
const SignBtn = document.querySelector('.sign-in-btn');
createAccountBtn.addEventListener('click', function (){
    signInForm.style.display = 'none'
    registerForm.style.display = 'block'
});
// signBtn.addEventListener('click', function (){
//     signInForm.style.display = 'block'
//     registerForm.style.display = 'none'
// });


//  password validation tester
var password = document.getElementById('passWord');
var border = document.getElementsByTagName('input');
var msg = document.getElementById('message');
var str = document.getElementById('strength');
var confirmPassword = document.getElementById('confirm-passWord');


password.addEventListener('input',()=>{
if (password.value.length > 0){
    msg.style.display = "block";
}
else{
    msg.style.display = "none";
}
if(password.value.length < 5){
    str.innerHTML = "weak";
    password.style.borderColor = 'red';
    msg.style.color = 'red';
}
else if(password.value.length >=6 && password.value.length< 10){
    str.innerHTML = "medium";
    password.style.borderColor = 'green';
    msg.style.color = 'green';
}
else if(password.value.length >= 12){
    str.innerHTML = 'strong';
    password.style.borderColor = 'blue';
    msg.style.color = 'blue'
}
});
confirmPassword.addEventListener('click', function(){
    msg.style.display = 'none'
})

const RegisterButton = document.querySelector('.register-btn');
const RegisterBTN = document.querySelector('#register-btn');
const confirmError = document.querySelector('.confirmation-error');
const firstName = document.querySelector('#firstName');
const secondName = document.querySelector('#secondName');
const phonenumber = document.querySelector('#phoneNumber');


RegisterButton.addEventListener('click',function(){
    // if(password.value == confirmPassword.value){
    //     return true;
    // }
    if(firstName.value == 0){
        document.querySelector('.first-name-error').innerHTML = 'First Name Is Required';
        firstName.style.borderColor = 'red';
    }
    else if (secondName.value == 0){
        document.querySelector('.second-name-error').innerHTML = 'Second Name Is Required';
        secondName.style.borderColor = 'red';
    }
    else if(isNaN(phonenumber.value)){
        phonenumber.style.borderColor = 'red';
        document.querySelector('.Phone-number-error').innerHTML = 'Enter Numeric Value Only';
    }
    else if(phonenumber.value.length = 0){
        phonenumber.style.borderColor = 'red';
        document.querySelector('.Phone-number-error').innerHTML = 'Phone Number Required';
    }
    else if(phonenumber.value.length < 9){
        phonenumber.style.borderColor = 'red';
        document.querySelector('.Phone-number-error').innerHTML = 'Number Must Be Ten Characters Long';
    }
    else if (password.value == 0){
        phonenumber.style.borderColor = 'red';
        document.querySelector('.password-error').innerHTML = 'Password Required';
    }
    else{RegisterBTN.addEventListener('click',function(){
        if(password.value == confirmPassword.value){
           return true;
        }
        else{
            confirmError.innerHTML = 'Password must be the same';
            confirmPassword.style.borderColor = 'red'
            return false;
        }
        });
    }
});







