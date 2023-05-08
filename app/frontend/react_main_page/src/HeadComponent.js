import React from "react";

function HeadComponent(){
    return (
    <div className="head">
        <h1 className="headname">FastApiMongoReact</h1>
        <img className="headimage" src={require("./Danis.png")} alt="Author"/>
        <div className="headdescription"> 
            By Danis <br/>
            Python/JS developer
        </div>
    </div>
    )
}
export default HeadComponent
