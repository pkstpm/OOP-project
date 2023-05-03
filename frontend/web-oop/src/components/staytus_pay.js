import "../styles/checkout.css";

function Status(props){
    return (
        <div className="status-page" onClick={props.onClose}>
            <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css" />
            <div className="status-bg"onClick={e => e.stopPropagation()}>
                <div className="status-container">
                    <div className="status-icon"><i class="fa-regular fa-circle-check"/></div>
                    <div className="status-text"><h1>PAID</h1></div>
                    <button onClick={props.onClose}>OKAY</button>
                </div>
            </div>
        </div>
    )
}

export default Status;