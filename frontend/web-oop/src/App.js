import './App.css';
import Header from './component/header';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom'
import ProductByName from './page/productbyname';
import Category from './page/category';
import LoginPage from './page/login';
import SignupPage from './page/signup';
import Home from './page/home';
import Products from './page/product';

function App() {
  return (
    <Router>
      <div>
      <Header/>
       
        <Routes>
          
          <Route path="/" element={<Home />} />
          <Route path="/login" element={<LoginPage />} />
          <Route path="/signup" element={<SignupPage/>} />
          <Route path="/product/:name" element={<ProductByName />} />
          <Route path="/product" element={<Products />} />
          <Route path="/category/:category_name" element={<Category />} />
        </Routes>
      </div>
    </Router>
  );
}

export default App;
