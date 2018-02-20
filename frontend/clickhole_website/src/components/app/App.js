// Third-Party Libraries
import React, { Component } from "react";
import { BrowserRouter, Route, Switch } from "react-router-dom";
// Custom Components
import HomePage from "../../pages/home_page/home_page.js";
import LogInPage from "../../pages/log_in_page/log_in_page.js";
import SignUpPage from "../../pages/sign_up_page/sign_up_page.js";
// Styling
import "./App.css";

class App extends Component {
    render() {
        return (
            <BrowserRouter>
                <Switch>
                    <Route exact path="/" component={HomePage} />
                    <Route path="/login" component={LogInPage} />
                    <Route path="/signup" component={SignUpPage} />
                </Switch>
            </BrowserRouter>
        );
    }
}

export default App;
