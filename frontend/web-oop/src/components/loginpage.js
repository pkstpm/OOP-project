import Header from "./header";
import "../styles/loginpage.css";
import React, { useState } from 'react';

function Loginpage(props) {
    const [isWrapperActive, setIsWrapperActive] = useState(false);
    const [isWrapper, setIsWrapper] = useState(false);

    const [username, setUsername] = useState('');
    const [password, setPassword] = useState('');
    const [confirmPassword, setConfirmPassword] = useState('');
    const [email, setEmail] = useState('');
    const [name,setName] = useState('');
    const [loginStatus, setLoginStatus] = useState('');
    const [registerStatus, setRegisterStatus] = useState('');

    function SignUpClick() {
        setIsWrapper(false);
    }
    function LoginClick() {
        setIsWrapper(true);
    }
    function handleSignUpClick() {
        setIsWrapperActive(true);
    }
    function handleLoginClick() {
        setIsWrapperActive(false);
    }

 const handleUsernameChange = (event) => {
    setUsername(event.target.value);
  };

  const handlePasswordChange = (event) => {
    setPassword(event.target.value);
  };

  const handleConfirmPasswordhange = (event) => {
    setConfirmPassword(event.target.value);
  };

  const handleEmailChange = (event) => {
    setEmail(event.target.value);
  };

  
  const handleNameChange = (event) => {
    setName(event.target.value);
  };


  const handleSubmitRegister = (event) => {
    event.preventDefault();
    const paylode = {
        "username":username,
        "password" : password,
        "check_password" : confirmPassword,
        "email": email, 
        "name" : name
     }
     console.log(paylode)
    fetch(`http://127.0.0.1:8000/register`, {
      method: 'POST',
      body:  JSON.stringify(paylode),
      headers: { 'Content-Type': 'application/json' },
    })
    .then(response => response.json())
    .then(data => {
        console.log(data)
        if(data && data.message === 'Success'){
            localStorage.setItem('isLoggedIn', true); 
            localStorage.setItem('role', 'Custommer');
            console.log('login',data.account)
            localStorage.setItem('user',data.account);
            props.onClose();
            window.location.reload()
        }
        else{
            setRegisterStatus('Register Failed');
        }
    //   setAlert({ type: 'success', message: data });
    })
    .catch(error => {
        
        console.log(error)
    //   setAlert({ type: 'danger', message: error.message });
    });
  };


  const handleSubmitLogin = (event) => {
    event.preventDefault();
    fetch(`http://127.0.0.1:8000/login`, {
      method: 'POST',
      body: JSON.stringify({ username, password }),
      headers: { 'Content-Type': 'application/json' },
    })
    .then(response => response.json())
    .then(data => {
        console.log(data)
        if(data && data.message === 'Login success'){
            localStorage.setItem('isLoggedIn', true); 
            localStorage.setItem('role', data.role);
            localStorage.setItem('userId',data.account._Customer__account_id);
            props.onClose();
            window.location.reload()
        }
        else{
            setLoginStatus('Login Failed');
        }
    //   setAlert({ type: 'success', message: data });
    })
    .catch(error => {
        
        console.log(error)
    //   setAlert({ type: 'danger', message: error.message });
    });
  };



    return (
        <div>
            <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css" />
            {props.clicksignup ? (
                <div className="login-page" onClick={props.onClose}>
                    <div className="login-bg" onClick={e => e.stopPropagation()}>
                        <div className={isWrapper ? ('wrapper'):'wrapper active'}>
                            <span className="icon-close" onClick={props.onClose}>
                                <i class="fa-solid fa-xmark"></i>
                            </span>
                            <div className="form-box login">
                                <h2>Log In To Drop</h2>
                                <form >
                                    <div className="input-box">
                                        <span className="icon">
                                            <i class="fa-solid fa-user-secret" />
                                        </span>
                                        <input type="text" required value={username}  onChange={handleUsernameChange}/>
                                        <label>Username</label>
                                    </div>
                                    <div className="input-box">
                                        <span className="icon">
                                            <i className="fa-solid fa-lock" />
                                        </span>
                                        <input type="password" required value={password} onChange={handlePasswordChange}/>
                                        <label>Password</label>
                                    </div>
                                    <div className="remember-forgot">
                                        <label><input type="checkbox" />Remember me</label>
                                        <a href="#">Forgot Password?</a>
                                    </div>
                                    <button type="submit" className="btn" onClick={handleSubmitLogin}>Login</button>
                                    <div className="login-register">
                                        <p>Not a member yet?  <a href="#signup" className="register-link" onClick={SignUpClick}>Sign up</a></p>
                                    </div>
                                </form>
                            </div>
                            <div className="form-box register">
                                <h2>Sign Up</h2>
                                <form action="#">
                                    {registerStatus ? (
                                    <p style={{ width: '100%', textAlign: 'center', color: 'red' }}>{registerStatus}</p>) : null}
                                    <div className="input-box">
                                        <span className="icon">
                                            <i class="fa-solid fa-user-secret" />
                                        </span>
                                        <input type="text" required value={username} onChange={handleUsernameChange}/>
                                        <label>Username</label>
                                    </div>
                                    <div className="input-box">
                                        <span className="icon">
                                            <i className="fa-solid fa-lock" />
                                        </span>
                                        <input type="password" required  value={password} onChange={handlePasswordChange}/>
                                        <label>Password</label>
                                    </div>
                                    <div className="input-box">
                                        <span className="icon">
                                            <i class="fa-solid fa-square-check" />
                                        </span>
                                        <input type="password" required value={confirmPassword} onChange={handleConfirmPasswordhange} />
                                        <label>Password Again</label>
                                    </div>
                                    <div className="input-box">
                                        <span className="icon">
                                            <i class="fa-solid fa-envelope" />
                                        </span>
                                        <input type="email" required value={email} onChange={handleEmailChange} />
                                        <label>Email</label>
                                    </div>
                                    <div className="input-box">
                                        <span className="icon">
                                            <i class="fa-solid fa-circle-user" />
                                        </span>
                                        <input type="text" required value={name} onChange={handleNameChange} />
                                        <label>Name</label>
                                    </div>
                                    <button type="submit" className="btn" onClick={handleSubmitRegister}>Register</button>
                                    <div className="login-register">
                                        <p>Already have an account? <a href="#login" className="login-link" onClick={LoginClick}>Login</a></p>
                                    </div>
                                </form>
                            </div>
                        </div>
                    </div>
                </div>
            ) : (
                <div className="login-page" onClick={props.onClose}>
                    <div className="login-bg" onClick={e => e.stopPropagation()}>
                        <div className={isWrapperActive?'wrapper active':'wrapper'}>
                            <span className="icon-close" onClick={props.onClose}>
                                <i class="fa-solid fa-xmark"></i>
                            </span>
                            <div className="form-box login">
                                <h2>Log In To Drop</h2>
                               
                                <form >
                                {loginStatus ? (
                                <p style={{ width: '100%', textAlign: 'center', color: 'red' }}>{loginStatus}</p>) : null}
                                    <div className="input-box">
                                        <span className="icon">
                                            <i class="fa-solid fa-user-secret" />
                                        </span>
                                        <input type="text" required value={username}  onChange={handleUsernameChange}/>
                                        <label>Username</label>
                                    </div>
                                    <div className="input-box">
                                        <span className="icon">
                                            <i className="fa-solid fa-lock" />
                                        </span>
                                        <input type="password" required value={password} onChange={handlePasswordChange}/>
                                        <label>Password</label>
                                    </div>
                                    <div className="remember-forgot">
                                        <label><input type="checkbox" />Remember me</label>
                                        <a href="#">Forgot Password?</a>
                                    </div>
                                    <button type="submit" className="btn" onClick={handleSubmitLogin}>Login</button>
                                    <div className="login-register">
                                        <p>Not a member yet?  <a href="#signup" className="register-link" onClick={SignUpClick}>Sign up</a></p>
                                    </div>
                                </form>
                            </div>
                            <div className="form-box register">
                                <h2>Sign Up</h2>
                                <form action="#">
                                    <div className="input-box">
                                        <span className="icon">
                                            <i class="fa-solid fa-user-secret" />
                                        </span>
                                        <input type="text" required />
                                        <label>Username</label>
                                    </div>
                                    <div className="input-box">
                                        <span className="icon">
                                            <i className="fa-solid fa-lock" />
                                        </span>
                                        <input type="password" required />
                                        <label>Password</label>
                                    </div>
                                    <div className="input-box">
                                        <span className="icon">
                                            <i class="fa-solid fa-square-check" />
                                        </span>
                                        <input type="password" required />
                                        <label>Password Again</label>
                                    </div>
                                    <div className="input-box">
                                        <span className="icon">
                                            <i class="fa-solid fa-envelope" />
                                        </span>
                                        <input type="email" required />
                                        <label>Email</label>
                                    </div>
                                    <div className="input-box">
                                        <span className="icon">
                                            <i class="fa-solid fa-circle-user" />
                                        </span>
                                        <input type="text" required />
                                        <label>Name</label>
                                    </div>
                                    <button type="submit" className="btn">Register</button>
                                    <div className="login-register">
                                        <p>Already have an account? <a href="#login" className="login-link" onClick={handleLoginClick}>Login</a></p>
                                    </div>
                                </form>
                            </div>
                        </div>
                    </div>
                </div>)}

        </div>
    );
}



export default Loginpage;