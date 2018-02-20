// Third-Party Libraries
import React from "react";
import ReactDOM from "react-dom";
// Custom Code
import App from "./components/app/App.js";
// Resources
import "./index.css";
import registerServiceWorker from "./registerServiceWorker";

ReactDOM.render(<App />, document.getElementById("root"));
registerServiceWorker();
