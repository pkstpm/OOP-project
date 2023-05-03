import React from "react";
import "../styles/op_user.css";
import { Link } from "react-router-dom";
import { useNavigate } from 'react-router-dom';




function Op_userpage(props) {
    const navigate = useNavigate();
    const logout = () => {
        localStorage.removeItem('isLoggedIn'); 
        localStorage.removeItem('role');
        localStorage.removeItem('account');
        localStorage.removeItem('userId');
        navigate('/products/all');
        window.location.reload()
      };

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