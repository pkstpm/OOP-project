import React, { useState, useEffect, useRef } from 'react';
import Search from "./search";
import "../styles/search.css"
import "../styles/header.css";
import Header from "./header";
import Loginpage from './loginpage';
import Headerlogin from './headerlogin';
import Cartpage from './cart';
import Op_userpage from './op_user';



function Navbar() {
    const [searchText, setsearchText] = useState('');
    const [infoVisible, setInfoVisible] = useState(false);
    const infoRef = useRef(null);
    const [showLoginPage, setShowLoginPage] = useState(false);
    const [showSignupPage, setShowSignupPage] = useState(false);

    const [isLoggedIn, setIsLoggedIn] = useState(false);

    const [showCartPage, setShowCartPage] = useState(false);
    const [showOp_userPage, setShowOp_userPage] = useState(false);

    const ff = false;
    const tt = true;


    function handleLoginClick() {
        setShowLoginPage(true);
    }
    function handleLoginPageClick() {
        setShowLoginPage(false);
    }
    function handleSignupClick() {
        setShowSignupPage(true);
    }
    function handleSignupPageClick() {
        setShowSignupPage(false);
    }

    function handleOp_userClick() {
        setShowOp_userPage(true);
    }
    function handleOp_userbgClick() {
        setShowOp_userPage(false);
    }
    function handleCartClick() {
        setShowCartPage(true);
    }
    function handleCartbgClick() {
        setShowCartPage(false);
    }



    function searchclick() {
        setInfoVisible(!infoVisible);
    }
    function handleClickOutside(event) {
        if (infoRef.current && !infoRef.current.contains(event.target)) {
            setInfoVisible(false);
        }
    }
    useEffect(() => {
        document.addEventListener("mousedown", handleClickOutside);
        return () => {
            document.removeEventListener("mousedown", handleClickOutside);
            const storedIsLoggedIn = localStorage.getItem('isLoggedIn');
             if (storedIsLoggedIn) {
                setIsLoggedIn(JSON.parse(storedIsLoggedIn));
            }
        };
    }, []);

    return (
        <div>
            {isLoggedIn ?  <Headerlogin searchclick={searchclick} loginclick={handleLoginClick} signupclick={handleSignupClick} cartclick={handleCartClick} op_userclick={handleOp_userClick}/>:<Header searchclick={searchclick} loginclick={handleLoginClick}  signupclick={handleSignupClick}/> }
            
            {infoVisible && <Search  ref={infoRef} value={searchText} onValueChange={setsearchText} />}
            {showLoginPage && <Loginpage onClose={handleLoginPageClick} clicksignup={ff}/>}
            {showSignupPage && <Loginpage  onClose={handleSignupPageClick}  clicksignup={tt}/>}
            {showCartPage && <Cartpage onClose={handleCartbgClick} />}
            {showOp_userPage && <Op_userpage onClose={handleOp_userbgClick} />}
            {/* <Headerlogin/> */}
           
        </div>
       
        

    );
}

export default Navbar;