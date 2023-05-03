// import './App.css';
// import Header from './component/header';
// import { BrowserRouter as Router, Routes, Route } from 'react-router-dom'
// import ProductByName from './page/productbyname';
// import Category from './page/category';
// import LoginPage from './page/login';
// import SignupPage from './page/signup';
// import Home from './page/home';
// import Products from './page/product';

// function App() {
//   return (
//     <Router>
//       <div>
//       <Header/>
       
//         <Routes>
          
//           <Route path="/" element={<Home />} />
//           <Route path="/login" element={<LoginPage />} />
//           <Route path="/signup" element={<SignupPage/>} />
//           <Route path="/product/:name" element={<ProductByName />} />
//           <Route path="/product" element={<Products />} />
//           <Route path="/category/:category_name" element={<Category />} />
//         </Routes>
//       </div>
//     </Router>
//   );
// }

// export default App;

// import './App.css';
import Header from './components/header';
import Simple from './components/simple';
import "./styles/search.css"
import "./styles/header.css"
import { BrowserRouter as Router, Switch, Route, RouterProvider, Routes } from 'react-router-dom';
import React from 'react';
import Products from './components/Allproduct';
import Navbar from './components/navbar';
import Product from './components/productpage';
import Home from './components/navbar';
import Cartpage from './components/cart';

// import Loginpage from './page/loginpage';


function App() {
    return (
        <Router>
          <Navbar/>
            <Routes>
                <Route path='/' element={<Simple/>}/>
                {/* <Route path="/product" element={<Products />} /> */}
                <Route path="/products/:name" element={<Products />} />
                <Route path="/product/:_product_id" element={<Product />} />
                <Route path="/cart" element={<Cartpage />} />


                

                

                {/* <Route path='/login' element={<Loginpage/>}/> */}
            </Routes>
        </Router>
    );
}

export default App;
