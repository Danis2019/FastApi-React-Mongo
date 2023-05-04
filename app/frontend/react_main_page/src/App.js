import './App.css';
import React from "react";
import HeadComponent from './HeadComponent';
import AuthComponent from './AuthComponent';

export default class App extends React.Component {
  render() {
    return (
      <div>
        <table>
        <tr>
            <td><AuthComponent /></td>
            <td><HeadComponent /></td>
        </tr>
        </table>
      </div>
    )
  }
}
