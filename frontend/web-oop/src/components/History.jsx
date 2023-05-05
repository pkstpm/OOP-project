import React, { useEffect, useState } from "react";

const PurchaseHistory = () => {
  const [transactions, setTransactions] = useState([]);
  const [userId, setUserId] = useState(null)
  const [rating, setRating] = useState("")
  useEffect(() => {
    const storedUserId = localStorage.getItem('userId');
    if(storedUserId){
      setUserId(+storedUserId)   
    }
    if(userId!=null){
      fetch(`http://127.0.0.1:8000/view_history_purchase/${userId}`).then((response) => response.json()
      )
      .then((data) => {
          console.log(data)
          setTransactions(data)
      })
      .catch((error) => {
        console.error("Error:", error);
      });
    }
   
}, [userId]);

const handleRatingChange = (event) => {
  const rating = event.target.value;
  setSearch(rating);
};

function handleRatingChange(){
  const playlode = JSON.stringify({account_id :userId, product_id : +id , rating:rating });
     console.log(playlode)
      fetch("http://127.0.0.1:8000/product/review/add_review", {
                method: "POST",
                body: playlode,
                headers: { 'Content-Type': 'application/json' },
              })
                .then((response) => response.json()
                )
                .then((data) => {
                  navigate(`/history`);
                })
                .catch((error) => {
                  console.error("Error:", error);
                });
    }
};


  return (
    <div className="flex justify-center">
      <div className="grid grid-cols-1 gap-4 md:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4">
        {transactions && transactions.map((transaction, index) => (
          <div
            key={index}
            className="bg-white shadow rounded-lg p-4 hover:shadow-xl transition-shadow"
          >
            <h3 className="font-semibold">{transaction.payment}</h3>
            <p className="text-gray-600">{transaction.pay_date}</p>
            <hr className="my-2" />
            <div className="flex justify-between mb-2">
              <p className="font-medium">Item</p>
              <p className="font-medium">Price</p>
            </div>
            {transaction.item.map((item, index) => (
              <div key={index} className="flex justify-between mb-1">
                <p>{item.name} x{item.quantity}</p>
                <p>${item.price.toFixed(2)}</p>
                <input
        type="number"
        name="rating"
        min="0"
        max="5"
        value={rating}
        onChange={handleRatingChange}
        placeholder="0"
        className="ml-4 px-2 py-1 border border-gray-400 rounded-md focus:outline-none focus:border-blue-500 w-16"
      />

              </div>
            ))}
            <hr className="my-2" />
            <div className="flex justify-between">
              <p className="font-medium">Total</p>
              <p className="font-medium">${transaction.total_price.toFixed(2)}</p>
            </div>
          </div>
        ))}
      </div>
    </div>
  );


// export default ShoppingHistory;

export default PurchaseHistory;

