import "../styles/header.css"
import React from 'react';
import { Link } from 'react-router-dom';




function Headerlogin(props) {
    return (
        <header className="border-b-2 border-black">
        <nav className="flex justify-between items-center px-[15%]">
          <link
            rel="stylesheet"
            href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css"
          />
          <div className="flex items-center">
            <img
              href="https://drop.com/home"
              className="logo"
              src="https://mma.prnewswire.com/media/878362/Drop_Logo.jpg?p=twitter"
            />
  
            <from className="navbar-left">
              <div>
                <Link to="/products/all" className="changepart">
                  SHOP
                </Link>
              </div>
              <div className="navbar-left">
                <Link to="/products/keyboard" className="changepart">
                  KEY BOARD
                </Link>
              </div>
              <div className="navbar-left">
                <Link to="/products/keycap" className="changepart">
                  KEY CAP
                </Link>
              </div>
              <div className="navbar-left">
                <Link to="/products/switch" className="changepart">
                  SWITCH
                </Link>
              </div>
            </from>
          </div>
  
          <from className="flex">
            {/* <bunton onClick={props.searchclick} class="fa fa-magnifying-glass" /> */}
            <a href="#cart" onClick={props.cartclick}>
              <i class="fa fa-cart-shopping" />
            </a>
            <i onClick={props.op_userclick} class="fa fa-user"></i>
          </from>
        </nav>
      </header>);
}

export default Headerlogin;