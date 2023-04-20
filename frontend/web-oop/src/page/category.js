import React, { useState, useEffect } from 'react';
import { useParams } from 'react-router-dom';

const Product = ({ product }) => {
  return (
    <div className="card mb-3">
      <div className="card-body">
        <h5 className="card-title">{product._name}</h5>
        <h6 className="card-subtitle mb-2 text-muted">{product._price}</h6>
        <p className="card-text mb-3">{product._quantity}</p>
        <p className="card-text font-weight-bold">
          Category: <span className="text-capitalize">{product._category}</span>
        </p>
        <p className="card-text font-weight-bold">
          Status: <span>{product._status}</span>
        </p>
      </div>
    </div>
  );
};

const Category = () => {
  const { category_name } = useParams();

  const [products, setProducts] = useState([]);

  useEffect(() => {
    fetch(`http://127.0.0.1:8000/search_category/${category_name}`)
      .then((response) => response.json())
      .then((data) =>  setProducts(data))
     
      .catch((error) => console.log(error));
  }, [category_name]);

  return (
    <div className="container">
        <div style={{marginTop:100}}></div>
      <div className="row">
        {
          products && products.map((product) => (
            <div className="col-md-4" key={product._product_id}>
              <Product product={product} />
            </div>
          ))}
      </div>
    </div>
  );
};

export default Category;
