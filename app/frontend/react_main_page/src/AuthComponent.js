import React, { Component }  from "react";
class ContentComponent extends Component { 
    render() {
        return(
            <div className="authcomponent">
                <h2>Пройдите авторизацию</h2>
                <br/>
                <input
                className="authinput"
                placeholder="Номер телефона"
                />
            </div>
        )
    }
 }
export default ContentComponent