import React, { useState, useEffect } from "react";
import { Link } from "react-router-dom";
import "../styles/product.css"

const SearchKeyboards = () => {
  const [products, setProducts] = useState([]);

  useEffect(() => {
    const fetchProducts = async () => {
      const response = await fetch("/product/keyboard/search_product/{name}");
      const data = await response.json();
      setProducts(data);
    };

    fetchProducts();
  }, []);

  return (
    <div className="container my-5">
      <div className="row">
        {  products && products.map((product) => (
          <div className="col-sm-12 col-md-6 col-lg-4" key={product._product_id}>
            <div className="card my-3">
              <img className="card-img-top" src={`https://via.placeholder.com/350x250?text=${product._name}`} alt={product._name} />
              <div className="card-body">
                <h5 className="card-title">{product._name}</h5>
                <p className="card-text">{product._quantity}</p>
                <span className="badge badge-primary">{product._category}</span>{' '}
                <span className="badge badge-secondary">{product._status}</span>{' '}
                <h4 className="mt-3">{product._promotion_price}$ <del>{product._price}$</del></h4>
                <Link to={`/products/${product._name}`} >Read more</Link>
              </div>

              
            </div>
          </div>
          
        ))}
      </div>
    </div>
  );
};

export default SearchKeyboards;
