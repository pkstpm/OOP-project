import "../styles/search.css"
function Productpost(props){
    const { product, onBgClick} = props;
    return(
        <div className="product-post">
            <div className="product-post-bg" onClick={onBgClick}/>
            <div className="product-post-content">
                <img src={product.URL} />
                <h4>{product.title}</h4>
            </div>
        </div>
    );
}

export default Productpost ;