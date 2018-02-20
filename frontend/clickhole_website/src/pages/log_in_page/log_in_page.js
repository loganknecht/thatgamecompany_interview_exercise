// Third-Party Libraries
import React from "react";
import { Link } from "react-router-dom";
// Resources
import "./log_in_page.css";
import falling_image from "../../images/falling.png";

class LogInPage extends React.Component {
    render() {
        return (
            <div className="log-in body">
                <div className="log-in container">
                    <div className="header">Enter your username and password to log-in!</div>
                    <br />
                    <div className="header image">
                        <img src={falling_image} alt="Welcome to your doom!" />
                    </div>
                    <br />
                    <form>
                        <div className="username container">
                            <div className="header">Username:</div>
                            <div className="field">
                                <input type="text/input" name="username" />
                            </div>
                        </div>
                        <div className="password container">
                            <div className="header">Password:</div>
                            <div className="field">
                                <input type="password" name="password" />
                            </div>
                        </div>
                        <br />
                        {/* TODO: Buttonize */}
                        <div className="submit">
                            <input type="submit" />
                        </div>
                    </form>
                </div>
                <br />
                <div>
                    <Link to="/">Return Home?</Link>
                </div>
            </div>
        );
    }
}

export default LogInPage;
