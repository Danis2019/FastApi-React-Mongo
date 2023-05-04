import React from "react";

function HeadComponent(){
    return (
    <div>
        <h1 className="head">FastApiMongoReact</h1>
        <img className="headimage" src={require("./Danis.png")} alt="Author"/>
    </div>
    )
}
export default HeadComponent
