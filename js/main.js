// loader at the opening of website
setTimeout(function(){
    document.getElementById("loader").style.display = "none";
    document.getElementById("main-content").style.display = "block";
}, 1000);
// open side bar logic
const revealSideBar = document.querySelector('.side-bar');
const menuIcon = document.querySelector('.icon');
menuIcon.addEventListener('click', function (){
    revealSideBar.style.display = 'block'
});
// close sidebar logic
const close = document.querySelector('.side-bar');
const closeIcon = document.querySelector('#close-window');
closeIcon.addEventListener('click', function (){
    close.style.display = 'none'
});
// sign in password tester
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

// toggle between register and sign in
const signInForm = document.querySelector('#sign-in');
const registerForm  = document.querySelector('#register')
const createAccountBtn = document.querySelector('#account');
const SignBtn = document.querySelector('.sign-in-btn');
createAccountBtn.addEventListener('click', function (){
    signInForm.style.display = 'none'
    registerForm.style.display = 'block'
    // window.location.href = "https://testflaskapp.vercel.app/";
});

//  password validation tester
// var password = document.getElementById('passWord');
// var border = document.getElementsByTagName('input');
// var msg = document.getElementById('message');
// var str = document.getElementById('strength');
// var confirmPassword = document.getElementById('confirm-passWord');

// password.addEventListener('input',()=>{
// if (password.value.length > 0){
//     msg.style.display = "block";
// }
// else{
//     msg.style.display = "none";
// }
// if(password.value.length < 5){
//     str.innerHTML = "weak";
//     password.style.borderColor = 'red';
//     msg.style.color = 'red';
// }
// else if(password.value.length >=6 && password.value.length< 10){
//     str.innerHTML = "medium";
//     password.style.borderColor = 'green';
//     msg.style.color = 'green';
// }
// else if(password.value.length >= 12){
//     str.innerHTML = 'strong';
//     password.style.borderColor = 'blue';
//     msg.style.color = 'blue'
// }
// });
// confirmPassword.addEventListener('click', function(){
//     msg.style.display = 'none'
// });
// password tester when registering
// const RegisterButton = document.querySelector('.register-btn');
// const RegisterBTN = document.querySelector('#register-btn');
// const confirmError = document.querySelector('.confirmation-error');
// const firstName = document.querySelector('#firstName');
// const secondName = document.querySelector('#secondName');
// const phonenumber = document.querySelector('#phoneNumber');

// RegisterButton.addEventListener('click',function(){
  
//     if(firstName.value == 0){
//         document.querySelector('.first-name-error').innerHTML = 'First Name Is Required';
//         firstName.style.borderColor = 'red';
//     }
//     else if (secondName.value == 0){
//         document.querySelector('.second-name-error').innerHTML = 'Second Name Is Required';
//         secondName.style.borderColor = 'red';
//     }
//     else if(isNaN(phonenumber.value)){
//         phonenumber.style.borderColor = 'red';
//         document.querySelector('.Phone-number-error').innerHTML = 'Enter Numeric Value Only';
//     }
//     else if(phonenumber.value.length = 0){
//         phonenumber.style.borderColor = 'red';
//         document.querySelector('.Phone-number-error').innerHTML = 'Phone Number Required';
//     }
//     else if(phonenumber.value.length < 9){
//         phonenumber.style.borderColor = 'red';
//         document.querySelector('.Phone-number-error').innerHTML = 'Number Must Be Ten Characters Long';
//     }
//     else if (password.value == 0){
//         phonenumber.style.borderColor = 'red';
//         document.querySelector('.password-error').innerHTML = 'Password Required';
//     }
//     else{RegisterBTN.addEventListener('click',function(){
//         if(password.value == confirmPassword.value){
//            return true;
//         }
//         else{
//             confirmError.innerHTML = 'Password must be the same';
//             confirmPassword.style.borderColor = 'red'
//             return false;
//         }
//         });
//     }
// });
// a graph to show the recent data transmitted
$(document).ready(function() {
$.ajax({
    type: "GET",
    url: "network_data.csv",
    dataType: "text",
    success: function(data) {
    var allLines = data.split(/\r?\n|\r/);
    var headers = allLines[0].split(',');
    var rbData = [];
    var tbData = [];
    for (var i = 1; i < allLines.length; i++) {
        var data = allLines[i].split(',');
        rbData.push(data[1]);
        tbData.push(data[4]);
    }
    var ctx = document.getElementById('chart').getContext('2d');
    var chart = new Chart(ctx, {
        type: 'line',
        data: {
        labels: Array.from({length: rbData.length}, (_, i) => i + 1),
        datasets: [
            {
            label: 'received bytes',
            backgroundColor: 'rgba(255, 99, 132, 0.2)',
            borderColor: 'rgba(255, 99, 132, 1)',
            data: rbData
            },
            {
            label: 'transmitted bytes',
            backgroundColor: 'rgba(54, 162, 235, 0.2)',
            borderColor: 'rgba(54, 162, 235, 1)',
            data: tbData
            }
        ]
        },
        options: {
        scales: {
            yAxes: [
            {
                id: 'rb-axis',
                position: 'left',
                gridLines: {
                color: 'rgba(0, 0, 0, 0.1)'
                }
            },
            {
                id: 'tb-axis',
                position: 'right',
                gridLines: {
                color: 'rgba(0, 0, 0, 0.1)'
                }
            }
            ]
        }
        }
    });
    }
});
});
// toggle change graph logic
const changeGraph = document.querySelector('.change-graph');
const hideSideBarList = document.querySelector('#hide');
const revealGraphTypes = document.querySelector('.graph-types');
const backNavigationArrow = document.querySelector('.back-navigation-arrow');

changeGraph.addEventListener('click', function(){
    hideSideBarList.style.display = 'none'
    revealGraphTypes.style.display = 'block'
    backNavigationArrow.style.display = 'block'
});
// toggle Back to sidebar list from graph list logic 
backNavigationArrow.addEventListener('click', function(){
    revealGraphTypes.style.display = 'none'
    hideSideBarList.style.display = 'block'
    backNavigationArrow.style.display = 'none'
});
// hide everything else and show wifi usage table
const allConnectedWifiData = document.querySelector('.all-connected-wifi-data');
const tableHeaderForAllWifiData = document.querySelector('.table-header');
const networkTable = document.querySelector('#network-table');
const latestWifiUsage = document.querySelector('#chart');
const Table = document.querySelector('.table');
const AvailableBalanceBlock = document.querySelector('.available-bal');
const analysisHeader = document.querySelector('.analysis');

allConnectedWifiData.addEventListener('click', function(){
    tableHeaderForAllWifiData.style.display = 'block'
    networkTable.style.display = 'none'
    latestWifiUsage.style.display = 'none'
    Table.style.display = 'none'
    analysisHeader.style.display = 'none'
    AvailableBalanceBlock.style.display = 'none'
});
// fetch all the data from csv and display it in html table
const table = document.getElementById("network-table");

fetch("network_data.csv")
.then(response => response.text())
.then(data => {
    const rows = data.split("\n");
    const headers = rows[0].split(",");

    let tableHTML = "";
    tableHTML += "<tr>";
    headers.forEach(header => {
    tableHTML += `<th>${header}</th>`;
    });
    tableHTML += "</tr>";

    for (let i = 1; i < rows.length; i++) {
    const cells = rows[i].split(",");
    tableHTML += "<tr>";
    cells.forEach(cell => {
        tableHTML += `<td>${cell}</td>`;
    });
    tableHTML += "</tr>";
    }
    table.innerHTML = tableHTML;
});
// uncheck one option if one is checked

const radiobutton1 = document.querySelector("#radiobtn1");
const radiobutton2 = document.querySelector("#radiobtn2");


radiobutton1.addEventListener("click", function() {
if (this.checked) {
    radiobutton2.checked = false;
    
}
});

radiobutton2.addEventListener("click", function() {
if (this.checked) {
    radiobutton1.checked = false;
  
}
});

// display send money and hide
const revealSendMoney = document.querySelector('.send-money-btn');
const sendMoneyBox = document.querySelector('.send-money');

revealSendMoney.addEventListener('click', function(){
    sendMoneyBox.style.display = 'block';
    revealSideBar.style.display = 'none'
    hideSendMoneyIcon.style.display = 'block'
});
// hide side money box
const hideSendMoneyIcon = document.querySelector('#close-sendmoney');

hideSendMoneyIcon.addEventListener('click', function(){
    function showNextDiv() {
        sendMoneyBox.style.display = 'none';
        hideSendMoneyIcon.style.display = 'none'
      }
    showNextDiv();
});



// counter balance 


const balanceCounter = document.querySelector("#available-bal-counter");
const countbalvalue = parseInt(balanceCounter.getAttribute("bal-count"), 10);
const duration = 2000; // in milliseconds
const step1 = Math.ceil(countbalvalue / (duration / 10)); 

let currentnumber = 0;

function balCounter() {
    intervalId = setInterval(() => {
        currentnumber  += step1;
      if (currentnumber  >= countbalvalue) {
        currentnumber  = countbalvalue;
        clearInterval(intervalId);
      }
      balanceCounter.textContent = currentnumber + '.00';
    }, 10);
}

const virtualCounter = document.querySelector("#virtual-bal-counter");
const virtualbalvalue = parseInt(virtualCounter.getAttribute("virtual-count"), 10);
const step2 = Math.ceil(virtualbalvalue / (duration / 10)); 

let Value = 0;

function virtualCounterFunction() {
    intervalId = setInterval(() => {
      Value += step2;
      if (Value >= virtualbalvalue) {
        Value = virtualbalvalue;
        clearInterval(intervalId);
      }
      virtualCounter.textContent = Value + '.00';
    }, 5);
}

const numberCounter = document.querySelector("#number-counter");
const countValue = parseInt(numberCounter.getAttribute("data-count"), 10);
const step = Math.ceil(countValue / (duration / 10)); // increase value by this amount every 10ms

let currentValue = 0;

function startCounting() {
  intervalId = setInterval(() => {
    currentValue += step;
    if (currentValue >= countValue) {
      currentValue = countValue;
      clearInterval(intervalId);
      startBtn.style.display = "block";
      loadingCircle.style.display = "none";
    }
    numberCounter.textContent = currentValue + 'USD';
  }, 10);
}

// refresh animation

const startBtn = document.getElementById("start-refresh-btn");
const loadingCircle = document.querySelector(".loading-circle");

startBtn.addEventListener("click", () => {
  startBtn.style.display = "none";
  loadingCircle.style.display = "block";
  loadingCircle.classList.add("rotate");
  setTimeout(() => {
    loadingCircle.classList.remove("rotate");
    startCounting();
    balCounter() 
    virtualCounterFunction()
  }, 5000);
});
