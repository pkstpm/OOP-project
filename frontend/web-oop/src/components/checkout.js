import "../styles/checkout.css";
import Status from "./status_pay";
import React, { useState } from 'react';

function Checkout (props){
    const [showstatusPage, setShowstatusPage] = useState(false);

    function handlepayClick(){
        setShowstatusPage(true)
    }
    function handlepaybgClick(){
        setShowstatusPage(false)
    }

    return (
        <div>
        <div className="checkout-page">
            <div className="payment">
            <img  href="https://drop.com/home" className='logo' src='https://mma.prnewswire.com/media/878362/Drop_Logo.jpg?p=twitter' />
                <h6>Payment</h6>
                <div className="pay">
                    <button onClick={handlepayClick}>Pay1</button>
                    <button onClick={handlepayClick}>Pay2</button>
                    <button onClick={handlepayClick}>Pay3
                    </button>
                </div>

            </div>
            <div className="order">
                <div className="checkout-items">
                    <ul className="item">
                        <li>test1</li>
                        <li>test2</li>
                        <li>test3</li>
                        <li>test4</li>
                        <li>test5</li>
                    </ul>
                </div>
            
                <div className="checkout-footer">
                        <div className="text-footer"><h6>Subtotal</h6><h6>$100</h6></div>
                        
                        <div className="text-footer"><h6>Total</h6><h6>$120</h6></div>
                        
                </div>
            </div>
        </div>
        {showstatusPage &&<Status onClose={handlepaybgClick}/>}
        </div>
    )
}

export default Checkout;