


console.log("ss")
function login(){
    var username = document.getElementById('loginUsername').value
    var password = document.getElementById('loginPassword').value
    var csrf = document.getElementById('csrf').value

    if(username == '' && password == ''){
        alert('You must enter both')
        e.preventDefault();
    }

    var data = {
        'username' : username,
        'password' : password
    }

    fetch('/api/login/' , {
        method : 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken' : csrf,
        },
       
        body : JSON.stringify(data)
    }).then(result => result.json())
    .then(response => {
        
        if(response.status == 200){
            window.location.href = '/'
        }
        else{
            alert(response.message)
        }

    })

}


function register(){
    var username = document.getElementById('signupUsername').value
    var password = document.getElementById('signupPassword').value
    var confirmpassword = document.getElementById('confirmPassword').value
    var csrf = document.getElementById('csrf').value

    if(username == '' && password == ''){
        alert('You must enter both')
        e.preventDefault();
    }
    if(password != confirmpassword){
        alert('password and confirm password doesnt match')
        e.preventDefault();
    }

    var data = {
        'username' : username,
        'password' : password
    }

    fetch('/api/register/' , {
        method : 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken' : csrf,
        },
       
        body : JSON.stringify(data)
    }).then(result => result.json())
    .then(response => {
        console.log(response)
        if(response.status == 200){
            window.location.href = '/login'
            alert("account created, now login")
        }
        else{
            alert(response.message)
        }

    })

}