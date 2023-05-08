import React, { Component }  from "react";

class ContentComponent extends Component {
    constructor() {
        super();
        this.state = {
          phone: ''
        };
        this.handleChange = this.handleChange.bind(this);
    }

    handleChange = (event) => {
    var { name, value } = event.target;
    this.setState({[name]: value});
    console.log(this.state)
    }

    render() {
        return(
            <div className="authcomponent">
                <div className="authname">Пройдите авторизацию</div>
                <br/>
                <input
                name="phone"
                className="authinput"
                placeholder="Номер телефона"
                onChange={this.handleChange}
                />
                <br/>
                <button className="authbutton">Далее</button>
            </div>
        )
    }
 }
export default ContentComponent