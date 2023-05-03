import "../styles/checkout.css";

import React, { useEffect, useState } from 'react';
import Status from "./staytus_pay";
import { useParams } from "react-router-dom";

function Checkout (props){
    const { id } = useParams();
    const [showstatusPage, setShowstatusPage] = useState(false);
    const [userId, setUserId] = useState(null);
    
    const [totalPrice, setTotalPrice] = useState(0)
    const [orderItem, setOrderItem] = useState([])

    function handlepayClick(){
        setShowstatusPage(true)
    }
    function handlepaybgClick(){
        setShowstatusPage(false)
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
        if(storedUserId){
          setUserId(+storedUserId)   
        }

        lodeData()
    }, [userId]);
    
    

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

            <div className="container mx-auto my-4">
      <h2 className="text-xl font-bold mb-4">Product Bill</h2>
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
          {/* <tr>
            <td className="border px-4 py-2" colSpan="2">Subtotal</td>
            <td className="border px-4 py-2">{subtotal}</td>
          </tr> */}
          {/* <tr>
            <td className="border px-4 py-2" colSpan="2">Tax</td>
            <td className="border px-4 py-2">{tax}</td>
          </tr> */}
          <tr>
            <td className="border px-4 py-2" colSpan="2">Total</td>
            <td className="border px-4 py-2">{totalPrice}</td>
          </tr>
        </tfoot>
      </table>
    </div>
            {/* <div className="order">
                <div className="checkout-items">
                    <ul className="item">
                        <li>test</li>
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
            </div> */}
        </div>
        {showstatusPage &&<Status onClose={handlepaybgClick}/>}
        </div>
    )
}

export default Checkout;