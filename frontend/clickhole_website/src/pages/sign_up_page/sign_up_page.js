// Third-Party Libraries
import React from "react";
import { Link } from "react-router-dom";
// Resources
import "./sign_up_page.css";
import falling_image from "../../images/falling.png";

class SignUpPage extends React.Component {
    perform_signup_request() {
        //
    }
    render() {
        return (
            <div className="signup body">
                <div className="signup container">
                    <div className="header">Create a username and password!</div>
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

export default SignUpPage;
