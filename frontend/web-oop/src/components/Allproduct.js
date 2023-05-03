import React, { useState, useEffect } from "react";
import { Link ,useParams,useNavigate} from "react-router-dom";
import "../styles/product.css"

const Products = () => {
  const [search, setSearch] = useState('');
  const [products, setProducts] = useState([]);
  const {name} = useParams();

   const handleChange = (event) => {
    const newValue = event.target.value;
    setSearch(newValue);
  };
  
  useEffect(() => {
    let path = "http://127.0.0.1:8000"
    if(!search){
      if (name==="all") path += "/product";
      else path += `/${name}`
    }
    else{
      if (name==="all") path +=  `/product/search_product/${search}`;
      else path +=  `/product/${name}/search_product/${search}`;
    }
    const fetchProducts = async () => {
      // if(!search){
      //   if (name==="all") path += "/product";
      //   else path += `/${name}`
      // }
      // else{
      //   if (name==="all") path +=  `/product/search_product/${search}`;
      //   else path +=  `/product/${name}/search_product/${search}`;
      // }
      const response = await fetch(path);
      const data = await response.json();
      setProducts(data);
    };
    fetchProducts();
  }, [name,search]);

  

  

  return (
    <div className="container my-5">
     
      <input name="search" class="form-control mr-sm-2" type="search" placeholder="Search" aria-label="Search" value={search} onChange={handleChange}/>
      
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
                { product._promotion_price ? (<h4 className="mt-3">{product._promotion_price}$ <del>{product._price}$</del></h4>): (<h4 className="mt-3">{product._price}</h4>)}
                <Link to={`/product/${product._product_id}`} >Read more</Link>
              </div>

              
            </div>
          </div>
          
        ))}
      </div>
    </div>
  );
};

export default Products;
