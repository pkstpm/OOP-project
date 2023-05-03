import React from "react";
import "../styles/op_user.css";
import { Link } from "react-router-dom";

const logout = () => {
    localStorage.removeItem('isLoggedIn'); 
    localStorage.removeItem('role');
    localStorage.removeItem('user');
    window.location.reload()
  };


function Op_userpage(props) {
    return (
        <div className="op_user-page z-50" onClick={props.onClose}>
            <div className="op_user-bg" onClick={e => e.stopPropagation()}>
                <div className="op_user-container">
                    <div className="profile">
                        <Link to="/profile" className="changepart">Profile</Link>
                    </div>
                    <div className="history">
                        <Link to="/history" className="changepart">History</Link>
                        </div>
                    <div className="logout">
                        <Link onClick={logout} className="changepart">Log Out</Link>
                        </div>
                </div>
            </div>
        </div>
    )
}

export default Op_userpage;