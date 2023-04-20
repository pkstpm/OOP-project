import React, { useState } from 'react';
import './login.css';

const LoginPage = () => {
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');
  const [alert, setAlert] = useState(null);

  const handleUsernameChange = (event) => {
    setUsername(event.target.value);
  };

  const handlePasswordChange = (event) => {
    setPassword(event.target.value);
  };

  const handleSubmit = (event) => {
    event.preventDefault();
    fetch(`http://127.0.0.1:8000/login?username=${username}&password=${password}`, {
      method: 'POST',
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
    <div className="login-page">
      <div className="form">
        <h1>Login</h1>
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

          <input className="btn btn-primary" type="submit" value="Login" />
        </form>
      </div>
    </div>
  );
};

export default LoginPage;
