import { Link, useParams } from 'react-router-dom';
import { useState,useEffect} from 'react';
function ProductByName() {
    const { name } = useParams();
    const [data, setData] = useState(null);
    
  useEffect(() => {
    
    const path = `http://localhost:8000/search_name/${name}`;
    
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
  }, [name]);


  return (
    
    <div>
    <section class="py-5">
        <div class="container px-4 px-lg-5 my-5">
            <div class="row gx-4 gx-lg-5 align-items-center">
                <div class="col-md-6"><img class="card-img-top mb-5 mb-md-0" src="https://dummyimage.com/600x700/dee2e6/6c757d.jpg" alt="..." /></div>
                <div class="col-md-6">
                    <div class="small mb-1">SKU: BST-498</div>
                    <h1 class="display-5 fw-bolder">{data && data._name}</h1>
                    <div class="fs-5 mb-5">
                        <span class="text-decoration-line-through">{data && data._price}</span>
                        <span>{data && data._promotion_price}</span>
                    </div>
                    <p class="lead">{data &&data._quantity}</p>
                    <div class="d-flex">
                        <input class="form-control text-center me-3" id="inputQuantity" type="num" value="1" style={{maxWidth: "3rem"}} />
                        <button class="btn btn-outline-dark flex-shrink-0" type="button">
                            <i class="bi-cart-fill me-1"></i>
                            Add to cart
                        </button>
                    </div>
                </div>
            </div>
        </div>
    </section>
    </div>
  );
}

export default ProductByName;