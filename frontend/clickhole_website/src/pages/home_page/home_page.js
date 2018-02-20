// Third-Party Libraries
import React from "react";
import { Link } from "react-router-dom";
// Resources
import "./home_page.css";
import falling_image from "../../images/falling.png";

class HomePage extends React.Component {
    render() {
        return (
            <div className="homepage body">
                <div className="header container">
                    <div className="text">
                        〜〜Ｗｅｌｃｏｍｅ　ｔｏ　Ｃｌｉｃｋｈｏｌｅ!〜〜<br />
                        <center>気を付けてください！</center>
                    </div>
                    <br />
                    <br />
                    <div className="image">
                        <img src={falling_image} alt="Welcome to Your Doom!" />
                    </div>
                </div>
                <br />
                <br />
                <br />
                <br />
                <br />
                <div className="buttons container">
                    <Link to="/login">
                        <button name="login">Log In</button>
                    </Link>
                    <Link to="/signup">
                        <button name="signup">Sign Up</button>
                    </Link>
                </div>
            </div>
        );
    }
}

export default HomePage;
