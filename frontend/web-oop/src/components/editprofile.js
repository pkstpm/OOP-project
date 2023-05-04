import React, { useState } from 'react'
import '../styles/update_info.css'

function Update_info  (props) {
    const [user_name, setdefaultname] = useState("");
    const [user_password, setdefaultpassword] = useState("");
    const [user_email, setdefaultemail] = useState("");
    
  function saveinfo(){
    //save value and send api
  }


  return (
    <div className='info-page' onClick={props.onClose}>
        <div className='info-bg' onClick={e => e.stopPropagation()}>
            <div className='info-container'>
                <div className='box'>
                <h2>Update Your Information</h2>
                <form onSubmit={saveinfo}>
                    <div className="info-box">
                    <span className="icon">
                                            <i class="fa-solid fa-user-secret" />
                                        </span>
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
                    <button type="submit" className="btn-save" onClick={props.onClose}>Save</button>
                </form>
                </div>
                </div>
            </div>
        </div>
  )
}

export default Update_info;