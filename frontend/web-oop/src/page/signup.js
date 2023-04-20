import React, { useState } from 'react';
import './signup.css';

const SignupPage = () => {
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');
  const [confirmPassword, setConfirmPassword] = useState('');
  const [email, setEmail] = useState('');
  const [name, setName] = useState('');
  const [alert, setAlert] = useState(null);

  const handleUsernameChange = (event) => {
    setUsername(event.target.value);
  };

  const handlePasswordChange = (event) => {
    setPassword(event.target.value);
  };

  const handleConfirmPasswordChange = (event) => {
    setConfirmPassword(event.target.value);
  };

  const handleName = (event) => {
    setName(event.target.value);
  };

  const handleEmail = (event) => {
    setEmail(event.target.value);
  };

  const handleSubmit = (event) => {
    event.preventDefault();
    if (password !== confirmPassword) {
      setAlert({ type: 'danger', message: 'Passwords do not match' });
      return;
    }
    fetch(`http://127.0.0.1:8000/sign_up?username=${username}&password=${password}&check_password=${confirmPassword}&email=${{email}}&name=${name}`, {
      method: 'POST',
      body: JSON.stringify({ username, password }),
      headers: {
        'Content-Type': 'application/json'
      }
    })
    .then(response => response.json())
    .then(data => {
      setAlert({ type: 'success', message: data });
    })
    .catch(error => {
      setAlert({ type: 'danger', message: error.message });
    });
  };

  return (
    <div className="signup-page">
      <div className="form">
        <h1>Sign Up</h1>
        {alert &&
          <div className={`alert alert-${alert.type}`} role="alert">
            {alert.message}
          </div>
        }
        <form onSubmit={handleSubmit}>
          <div className="form-group">
            <label>Username</label>
            <input type="text" className="form-control" placeholder="Enter username" value={username} onChange={handleUsernameChange} />
          </div>

          <div className="form-group">
            <label>Password</label>
            <input type="password" className="form-control" placeholder="Password" value={password} onChange={handlePasswordChange} />
          </div>

          <div className="form-group">
            <label>Confirm Password</label>
            <input type="password" className="form-control" placeholder="Confirm password" value={confirmPassword} onChange={handleConfirmPasswordChange} />
          </div>

          <div className="form-group">
            <label>Email</label>
            <input type="text" className="form-control" placeholder="Email" value={email} onChange={handleEmail} />
          </div>

          <div className="form-group">
            <label>Name</label>
            <input type="text" className="form-control" placeholder="name" value={name} onChange={handleName} />
          </div>

          <input className="btn btn-primary" type="submit" value="Sign Up" />
        </form>
      </div>
    </div>
  );
};

export default SignupPage;
