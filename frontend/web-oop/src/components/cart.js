import React, { useState, useEffect } from "react";
import "../styles/cart.css"
import { Link } from 'react-router-dom';
import { useNavigate } from 'react-router-dom';



function Cartpage(props) {
    const [userId, setUserId] = useState(null);
    const [showCart, setShowCart] = useState(false);
    const [totalPrice, setTotalPrice] = useState(0)
    const [cartItem, setCartItem] = useState([])
    const navigate = useNavigate();

    // const handleChange = (event) => {
    //   const newValue = event.target.value;
    //   setSearch(newValue);
    // };
  
    function handleCheckOut ()  {
      const playlode = JSON.stringify({account_id :userId});
    
      fetch("http://127.0.0.1:8000/make_order", {
                method: "POST",
                body: playlode,
                headers: { 'Content-Type': 'application/json' },
              })
                .then((response) => response.json()
                )
                .then((data) => {
                
                  navigate(`/checkout/${data.order_id}`);
                  props.onClose();
                })
                .catch((error) => {
                  console.error("Error:", error);
                });
     };

    const lodeData = () => {
      const storedUserId = localStorage.getItem('userId');
      if(storedUserId){
        setUserId(+storedUserId)   
      }
      const playlode = JSON.stringify({account_id :userId});
     if(  userId !== null) {
     fetch("http://127.0.0.1:8000/cart", {
              method: "POST",
              body: playlode,
              headers: { 'Content-Type': 'application/json' },
            })
              .then((response) => response.json()
              )
              .then((data) => {
                if(data.item.message != 'Your cart is empty'){
                  setCartItem(data.item)
                  setTotalPrice(data.total_price)
                 }
                 else {
                  setCartItem([])
                  setTotalPrice(0)
                 }
              })
              .catch((error) => {
                console.error("Error:", error);
              });
            }
    };

    function handleDeletItem (event)  {
      const playlode = JSON.stringify({account_id :userId, product_id:+event.target.value});
      fetch("http://127.0.0.1:8000/cart/remove_item/", {
                method: "PUT",
                body: playlode,
                headers: { 'Content-Type': 'application/json' },
              })
                .then((response) => response.json()
                )
                .then((data) => {
                
                  lodeData();
                })
                .catch((error) => {
                  console.error("Error:", error);
                });
     };

    useEffect(() => {
        setShowCart(props.isShow)
        if(props.isShow == true) lodeData();
    }, [showCart,]);

    return (
      <div class="relative">
        <div className={`fixed right-0 h-full w-1/4 bg-gray-800 ${showCart ? 'translate-x-0' : 'translate-x-full'} transition-transform duration-500 ease-in-out z-50`}>
        <div className="flex justify-between items-center px-4 py-2 border-b border-gray-700">
          <h2 className="text-lg font-semibold text-white">Shopping Cart</h2>
          <button className="bg-indigo-950 text-white" onClick={() =>{setShowCart(false); props.onClose() }  }>Close</button>
        </div>
        <div className="p-4">
          { cartItem ? (cartItem.map(product => (
            <div key={product.name} className="flex justify-between items-center mb-4">
              <div className="inline"><button className="inline-block bg-transparent border-transparent text-red-500 me-3"  value={product.product_id} onClick={handleDeletItem}> X </button>
              <p className="text-white inline-block">{product.name} ({product.quantity})</p></div>
              <p className="text-white">{product.price}</p>
            </div>
          ))) : null
        }
          <div className="flex justify-between items-center border-t border-gray-700 mt-4 pt-2">
            <p className="text-white">Total:</p>
            <p className="text-white">{totalPrice}</p>
          </div>
        </div>
        <div className="flex justify-between items-center px-4 py-2 border-t border-gray-700">
          <p className="text-white">Continue Shopping</p>
          <Link onClick={handleCheckOut} className="text-white">Checkout</Link>
        </div>
      </div>
      </div>
    )
    // return (
    //     <div className="cart-page" onClick={props.onClose}>
    //         <div className="cart-bg" onClick={e => e.stopPropagation()}>
    //             <div className="cart-container">
    //                 <div className="cart-header">
    //                     <h2>Shopping Cart</h2>
    //                 </div>
    //                 <div className="cart-items">
    //                     <ul className="items">
    //                         <li>Item 1</li>
    //                         <li>Item 2</li>
    //                         <li>Item 3</li>
    //                         <li>Item 4</li>
    //                         <li>Item 5</li>
    //                         <li>Item 6</li>
    //                         <li>Item 7</li>
    //                         <li>Item 8</li>
    //                         <li>Item 9</li>
    //                     </ul>
    //                 </div>
    //                 <div className="cart-footer">
    //                     <div><Link to="/checkout" className="btn-checkout">Checkout</Link></div>
    //                 </div>
    //             </div>
    //         </div>
    //     </div>
    // )
}

export default Cartpage;