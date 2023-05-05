import "../styles/checkout.css";

import React, { useEffect, useState } from 'react';
import Status from "./staytus_pay";
import { useParams } from "react-router-dom";
import { useNavigate } from 'react-router-dom';

function Checkout (props){
    const { id } = useParams();
    const [showstatusPage, setShowstatusPage] = useState(false);
    const [userId, setUserId] = useState(null);
    
    const [totalPrice, setTotalPrice] = useState(0)
    const [orderItem, setOrderItem] = useState([])
    const [address, setAddress] = useState("")

    const [activeButton, setActiveButton] = useState('');

    const navigate = useNavigate();

    const handleButtonClick = (buttonName) => {
      setActiveButton(buttonName);
    };


    function handleCancel(){
      const playlode = JSON.stringify({account_id :userId, order_id : +id });
     console.log(playlode)
      fetch("http://127.0.0.1:8000/cancel_order", {
                method: "POST",
                body: playlode,
                headers: { 'Content-Type': 'application/json' },
              })
                .then((response) => response.json()
                )
                .then((data) => {
                  navigate(`/history`);
                })
                .catch((error) => {
                  console.error("Error:", error);
                });
    }
    

    function handlePay(){
      const playlode = JSON.stringify({account_id :userId, order_id : +id , payment : activeButton});
     console.log(playlode)
      fetch("http://127.0.0.1:8000/payment", {
                method: "PUT",
                body: playlode,
                headers: { 'Content-Type': 'application/json' },
              })
                .then((response) => response.json()
                )
                .then((data) => {
                  navigate(`/history`);
                })
                .catch((error) => {
                  console.error("Error:", error);
                });
    }
    function handlepaybgClick(){
        setShowstatusPage(false)
    }


    function handlepayClick(){
      setShowstatusPage(true)
  }


    const lodeData = () => {
        const storedUserId = localStorage.getItem('userId');
        if(storedUserId){
          setUserId(+storedUserId)   
        }

        console.log(`http://127.0.0.1:8000/view_order/${userId}/${id}`)
       if(  userId !== null) {
       fetch(`http://127.0.0.1:8000/view_order/${userId}/${id}`, {
                method: "GET",
              })
                .then((response) => response.json()
                )
                .then((data) => {
                    console.log(data)
                    setOrderItem(data.item)
                    setTotalPrice(data.total_price)

                })
                .catch((error) => {
                  console.error("Error:", error);
                });
              }
      };

      useEffect(() => {
        const storedUserId = localStorage.getItem('userId');
        const storedAccount = localStorage.getItem('account');
        if(storedUserId){
          setUserId(+storedUserId)   
        }
        if(storedAccount){
          const account = JSON.parse(storedAccount)
          setAddress(account._Customer__address)
        }
        lodeData()
    }, [userId,id]);
    
    

    return (
        <div>
        <div className="checkout-page">
            <div className="payment">
            <img  href="https://drop.com/home" className='logo' src='https://mma.prnewswire.com/media/878362/Drop_Logo.jpg?p=twitter' />
                <h6>Payment</h6>
                <div className="flex justify-center space-x-4">
                  <button
                    className={`px-3 py-2 rounded-lg text-sm ${
                      activeButton === 'Shoppay' ? 'bg-black text-white' : 'bg-white'
                    }`}
                    onClick={() => handleButtonClick('Shoppay')}
                  >
                    Shoppay
                  </button>
                  <button
                    className={`px-3 py-2 rounded-lg text-sm ${
                      activeButton === 'Paypal' ? 'bg-black text-white' : 'bg-white'
                    }`}
                    onClick={() => handleButtonClick('Paypal')}
                  >
                    Paypal
                  </button>
                  <button
                    className={`px-3 py-2 rounded-lg text-sm ${
                      activeButton === 'Googlepay' ? 'bg-black text-white' : 'bg-white'
                    }`}
                    onClick={() => handleButtonClick('Googlepay')}
                  >
                    Google Pay
                  </button>
                </div>
                
            
                <div>
                    <h6>Address</h6>
                    <div>{userId && userId.address}</div>
                    <textarea name="address" id="" cols="40" rows="5" value={address} onChange={(event) => { setAddress(event.target.value) }}> </textarea>
                    <button class = "btn" onClick={handlePay}> Pay Now</button>
                    <button class = "btn-cancel mt-1"  onClick={handleCancel}> Cancel</button>
                </div>

            </div>

            <div className="container mx-auto my-4">
      <h2 className="text-xl font-bold mb-4">Product Bill {id}</h2>
      <h3></h3>
      <table className="table-auto w-full border-collapse">
        <thead>
          <tr>
            <th className="border px-4 py-2">Product Name</th>
            <th className="border px-4 py-2">Quantity</th>
            <th className="border px-4 py-2">Price</th>
          </tr>
        </thead>
        <tbody>
          {orderItem && orderItem.map((item, index) => (
            <tr key={index}>
              <td className="border px-4 py-2">{item.name}</td>
              <td className="border px-4 py-2">{item.quantity}</td>
              <td className="border px-4 py-2">{item.price}</td>
            </tr>
          ))}
        </tbody>
        <tfoot>
          <tr>
            <td className="border px-4 py-2" colSpan="2">Total</td>
            <td className="border px-4 py-2">{totalPrice}</td>
          </tr>
        </tfoot>
      </table>
    </div>
        </div>
        {showstatusPage &&<Status onClose={handlepaybgClick}/>}
        </div>
    )
}

export default Checkout;