import { Link, useParams } from 'react-router-dom';
import { useState,useEffect} from 'react';
import "../styles/product.css"
import Cartpage from './cart';

function Product() {
    const { _product_id } = useParams();
    const [data, setData] = useState(null);
    const [amount,setAmount] = useState(0)
    const handleAmountChange = (event) => {
      setAmount(event.target.value); // เมื่อผู้ใช้กรอกข้อมูล input ให้เปลี่ยนค่า State ของ inputValue
    };
    
    const [isLoggedIn, setIsLoggedIn] = useState(false);
    const [userId, setUserId] = useState(null);

    const handleSubmit = (event) => {
      console.log("Hi")
      event.preventDefault();
      const playlode = JSON.stringify({
        "account_id" : userId ,
        "product_id": +_product_id,
        "quantity":  +amount
        })
      event.preventDefault(); // ยกเลิกการส่งฟอร์มเพื่อให้เราสามารถจัดการข้อมูล input ได้
      console.log(playlode)
      // ส่งค่า input ไปยังเซิร์ฟเวอร์เพื่อประมวลผล
      fetch("http://127.0.0.1:8000/cart/add_item", {
        method: "POST",
        body: playlode,
        headers: { 'Content-Type': 'application/json' },
      })
        .then((response) => response.json()
        )
        .then((data) => {
          if(data){
            window.location.reload()
          }
          console.log(data); // ประมวลผลข้อมูลที่ส่งกลับมาจากเซิร์ฟเวอร์
        })
        .catch((error) => {
          console.error("Error:", error);
        });
  

        
     
    };
    
  useEffect(() => {
    
    const storedIsLoggedIn = localStorage.getItem('isLoggedIn');
    const storedUserId = localStorage.getItem('userId');
    if (storedIsLoggedIn) {
       setIsLoggedIn(JSON.parse(storedIsLoggedIn));
    }
    if(storedUserId){
      setUserId(JSON.parse(storedUserId))
    }

    

    const path = `http://127.0.0.1:8000/product/${_product_id}`;
    
    fetch(path ,{
      })
      .then(response => response.json())
      .then(data => {
        setData(data);
        console.log(data); // Log the data to the console
      })
      .catch(error => {

        console.error('Error:', error);
      });
  }, [_product_id]);


  return (
    
    <div>
    <section class="py-5">
        <div class="container px-4 px-lg-5 my-5">
            <div class="row gx-4 gx-lg-5 align-items-center">
                <div class="col-md-6"><img class="card-img-top mb-5 mb-md-0" src="https://dummyimage.com/600x700/dee2e6/6c757d.jpg" alt="..." /></div>
                <div class="col-md-6">
                    {/* <div class="small mb-1">{data && data._product_id}</div> */}
                    <h1 class="display-5 fw-bolder">{data && data._name}</h1>
                    
                    { data && data._promotion_price ? (<div class="fs-5 mb-5">
                        <span class="text-decoration-line-through">{data && data._price}</span>
                        <span>{data && data._promotion_price}</span>
                    </div>): (<div class="fs-5 mb-5">
                        <span>{data && data._price}</span>
                    </div>)}
                   
                    
                    <p class="lead">{data &&data._quantity}</p>
                    <div class="d-flex">
                    <form onSubmit={handleSubmit}>
                        <input class="form-control text-center me-3" id="inputQuantity" type="num" value={amount} onChange={handleAmountChange} style={{maxWidth: "3rem"}} disabled={!isLoggedIn} />
                        <button  class="btn btn-outline-dark flex-shrink-0" type="submit" disabled={!isLoggedIn} >
                            <i class="bi-cart-fill me-1"> Add to Cart</i>
                        </button>
                      </form>
                    </div>
                </div>
            </div>
        </div>
    </section>
    </div>
  );
}

export default Product;