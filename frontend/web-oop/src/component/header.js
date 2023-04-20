import "./sheader.css"
import { useNavigate } from 'react-router-dom';
import { Link } from "react-router-dom";

function Header(){
  const history = useNavigate();
  const handleSubmit = (event) => {
    
    event.preventDefault();
    const input = event.target.elements.search.value;
    const select = event.target.elements.searchBy.value;

    if (select === '1') {
      history(`/product/${input}`);
    } else if (select === '2') {
      history(`/category/${input}`);
    }
  };
    return(
      <nav class="navbar navbar-expand-lg navbar-dark fixed-top bg-dark">
      <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarTogglerDemo03" aria-controls="navbarTogglerDemo03" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
      </button>
      <a class="navbar-brand" href="#">OOP</a>
    
      <div class="collapse navbar-collapse" id="navbarTogglerDemo03">
        <ul class="navbar-nav mr-auto mt-2 mt-lg-0">
          <li class="nav-item active">
            <Link to={"/product/"} class="nav-link" href="#">SHOP </Link>
          </li>
          <li class="nav-item">
            <a class="nav-link" href="#">MECH KEYS</a>
          </li>
          <li class="nav-item">
            <a class="nav-link" href="#">AUDIOPHILE</a>
          </li>
        </ul>
      </div>
      <div>
          <div class="form-inline my-2 my-lg-0">
          <form onSubmit={handleSubmit}>
      <input name="search" class="form-control mr-sm-2" type="search" placeholder="Search" aria-label="Search"/>
      <select name="searchBy" class="form-select btn btn-outline-success my-2 my-sm-0 mr-sm-1" aria-label="Default select example">
        <option value="1">name</option>
        <option value="2">category</option>
      </select>
      <button class="btn btn-outline-success my-2 my-sm-0 mr-sm-1" type="submit">Search</button>
    </form>
            <Link to={""} class="btn btn-outline-success my-2 my-sm-0 mr-sm-1 text-success" type="submit">cart</Link>
            <Link to={"/login"} class="btn btn-outline-success my-2 my-sm-0 mr-sm-1 text-success" type="submit">log in</Link>
            <Link to={"/signup"} class="btn btn-outline-success my-2 my-sm-0 mr-sm-1 text-success" type="submit">sign up</Link>
            </div>
      </div>
      
  </nav>

          
    );

}

export default Header;