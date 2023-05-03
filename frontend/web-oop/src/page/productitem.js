import "../styles/search.css"

function Productitem(props) {
    const {product, onProductClick} = props;
    return (<div className='grid-img'>
        <img src= {product.URL} onClick={() => {onProductClick(product)}}/>
        <h4>{product.title}</h4>
    </div>);
}

export default Productitem;