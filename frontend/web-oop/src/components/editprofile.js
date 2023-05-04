import React, { useState } from 'react'
import '../styles/editprofile.css'

function Update_info  (props) {
    const [user_name, setdefaultname] = useState("");
    const [user_password, setdefaultpassword] = useState("");
    const [user_email, setdefaultemail] = useState("");
    const [user_address, setdefaultaddress] = useState("");
    

    
  function saveinfo(){
    //save value and send api
  }


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
                        <input type="password" value={user_password} onChange={(event) => { setdefaultpassword(event.target.value) }}/>
                        <label>Password</label>
                    </div>
                    <div className="info-box">
                        <input type="email" value={user_email} onChange={(event) => { setdefaultemail(event.target.value) }}/>
                        <label>Email</label>
                    </div>
                    <div className="info-box">
                        <input type="text" value={user_address} onChange={(event) => { setdefaultaddress(event.target.value) }}/>
                        <label>Address</label>
                    </div>
                    <button type="submit" className="btn-save" onClick={props.onClose}>Save</button>
                </form>
                </div>
                </div>
            </div>
        </div>
  )
}

export default Update_info;