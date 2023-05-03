import "../styles/header.css"
import React from 'react';
import { Link } from 'react-router-dom';

function Header(props) {
    return (
        <header className=" border-b-2 border-black">
            <nav className="flex justify-between items-center px-[15%]">
            <link 
                rel="stylesheet" 
                href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css" />
            <div className="flex">
                <img
                    href="https://drop.com/home"
                className="logo"
                src="https://mma.prnewswire.com/media/878362/Drop_Logo.jpg?p=twitter"
                />
                <from className="navbar-left flex items-center">
                    <div className="nav-item"><Link to="/products/all" className="changepart">SHOP</Link></div>
                    <div className="nav-item"><Link to="/products/keyboard" className="changepart">KEY BOARD</Link></div>
                    <div className="nav-item"><Link to="/products/keycap" className="changepart">KEY CAP</Link></div>
                    <div className="nav-item"><Link to="/products/switch" className="changepart">SWITCH</Link></div>
                </from>
                
            </div>
                <from className="navbar-right">
                    {/* <bunton onClick={props.searchclick} class="fa fa-magnifying-glass"/> */}
                    <a href="#login" onClick={props.loginclick} className="btn-login">LOG IN</a>
                    <a href="#signup" onClick={props.signupclick} className="btn-login">SIGN UP</a>
                </from>


            </nav>
        </header>);
}

export default Header;