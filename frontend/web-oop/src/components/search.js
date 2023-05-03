import "../styles/search.css"
import SearchProducts from "./searchproduct";
import React, { useState } from "react";

function Search() {
    const [ inputValue, setInputValue ] = useState('');



    const handdlevaluechange = (event) =>{
        setInputValue(event.target.value);
        
    }



    return (
        <div className="search">
            <input
                className="search-input"
                type="text"
                placeholder="search product"
                value={inputValue}
                onChange={handdlevaluechange} />
                <SearchProducts inputValue={inputValue} />
        </div>
                
    );
    
}

export default Search;