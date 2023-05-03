import { useState } from 'react';
import Navbar from "../components/navbar";
import "../styles/history.css";


const purchases = [
  { id: 1, date: 'May 1, 2023', description: 'Item 1', amount: 10.99 },
  { id: 2, date: 'April 28, 2023', description: 'Item 2', amount: 19.99 },
  { id: 3, date: 'April 20, 2023', description: 'Item 3', amount: 5.99 },
];

function PurchaseHistory() {
  const [showDetails, setShowDetails] = useState(null);
  const [infoVisible, setInfoVisible] = useState(false);
  function searchclick() {
    setInfoVisible(!infoVisible);
}

    
  return (
    
    <div>
        <Navbar/>
    <div className="py-[40px] max-w-md mx-auto">
    <h2 className="text-xl font-bold mb-4 mx-auto">Purchase History</h2>
        
      
      <ul className="divide-y divide-gray-200 border black">
        {purchases.map(purchase => (
          <li key={purchase.id} className="py-4">
            <div className="flex justify-between items-center">
              <div>
                <p className="text-gray-600">{purchase.date}</p>
                <p className="font-bold">{purchase.description}</p>
              </div>
              <div>
                <p className="font-bold">${purchase.amount.toFixed(2)}</p>
                <button
                  className="black"
                  onClick={() => setShowDetails(purchase.id)}
                >
                    
                    <i  class="fa-solid fa-caret-down fa-2xl mr-0"></i>
                
                </button>
              </div>
            </div>
            {showDetails === purchase.id && (
              <div className="mt-2 border-t border-gray-200 pt-4">
                <p>Details for {purchase.description}:</p>
                <p>Amount: ${purchase.amount.toFixed(2)}</p>
              </div>
            )}
          </li>
        ))}
      </ul>
    </div>
    </div>
 
  );
}

export default PurchaseHistory;