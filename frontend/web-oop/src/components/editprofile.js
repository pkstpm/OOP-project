import React, { useEffect, useState } from 'react'
import '../styles/editprofile.css'

function Update_info  (props) {
    const [user_name, setdefaultname] = useState("");
    const [user_email, setdefaultemail] = useState("");
    const [user_address, setdefaultaddress] = useState("");
    const [userId, setUserId] = useState(null);
   
    
    const lodeData = () => {
        const storedUserId = localStorage.getItem('userId');
        if(storedUserId){
          setUserId(+storedUserId)   
        }
    }
    
  function saveinfo(){
    const playlode = JSON.stringify({account_id :userId, name : user_name , email : user_email, address : user_address});
       
        fetch("http://127.0.0.1:8000/edit_profile", {
                  method: "PUT",
                  body: playlode,
                  headers: { 'Content-Type': 'application/json' },
                })
                  .then((response) => response.json()
                  )
                  .then((data) => {
                    if(data.message === 'edit profile success'){
                        localStorage.setItem('account', JSON.stringify(data.account));
                        props.onClose()
                        window.location.reload();
                    }
                  })
                  .catch((error) => {
                    console.error("Error:", error);
                  });
       
  }

  useEffect(() => {
    const storedUserId = localStorage.getItem('userId');
    const storedAccount = localStorage.getItem('account');
    if(storedUserId){
      setUserId(+storedUserId)   
    }
    if(storedAccount){
        const account = JSON.parse(storedAccount);
        setdefaultname(account._Customer__name);
        setdefaultemail(account._Customer__email);
        setdefaultaddress(account._Customer__address);

        console.log(user_name)
    }
    
    
}, [userId]);

  return (
    <div className='info-page' onClick={props.onClose}>
        <div className='info-bg' onClick={e => e.stopPropagation()}>
            <div className='info-container'>
                <div className='box'>
                <h2>Edit Your Information</h2>
                <form onSubmit={saveinfo}>
                    <div className="info-box">
                        <input type="text" value={user_name} onChange={(event) => { setdefaultname(event.target.value) }}/>
                        <label>Name</label>
                    </div>
                    <div className="info-box">
                        <input type="email" value={user_email} onChange={(event) => { setdefaultemail(event.target.value) }}/>
                        <label>Email</label>
                    </div>
                    <div className="info-box">
                        <input type="text" value={user_address} onChange={(event) => { setdefaultaddress(event.target.value) }}/>
                        
                        <label>Address</label>
                    </div>
                    
                    <button type="submit" className="btn-save" onClick={saveinfo}>Save</button>
                </form>
                </div>
                </div>
            </div>
        </div>
  )
}

export default Update_info;