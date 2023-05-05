import "../styles/checkout.css";
import React, { useEffect, useState } from 'react';

function Status(props){
    const [userId, setUserId] = useState(null);
    const [ID, setId] = useState(null);
    const [payment , setpayment] = useState("")

    
            const lodeData = () => {
                const storedUserId = localStorage.getItem('userId');
                if(storedUserId){
                  setUserId(+storedUserId)
                  
                  
                }
                const playlode = JSON.stringify({account_id :userId , order_id: ID , payment: payment});
               if(  userId !== null) {
                fetch("http://127.0.0.1:8000/payment", {
                    method: "PUT",
                    body: playlode,
                    headers: { 'Content-Type': 'application/json' },
                })
                .then((response) => response.json()
                )
                .then((data) => {
                
                    setId(data._Order__order_id)
                    setpayment(data._Order__payment)
                    lodeData()
                  
                })
                .catch((error) => {
                  console.error("Error:", error);
                });
                      }
              };
    return (
        <div className="status-page" onClick={props.onClose}>
            <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css" />
            <div className="status-bg"onClick={e => e.stopPropagation()}>
                <div className="status-container">
                    <div className="status-icon"><i class="fa-regular fa-circle-check"/></div>
                    <div className="status-text"><h1>PAID BY {payment} </h1></div>
                    <button onClick={props.onClose}>OKAY</button>
                </div>
            </div>
        </div>
    )
    }

export default Status;