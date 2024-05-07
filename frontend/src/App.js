// Filename - App.js

import React, { Component } from "react";
import {
    BrowserRouter as Router,
    Routes,
    Route,
    Link,
} from "react-router-dom";
import Home from "./pages/Home";
import Discount from "./pages/Discount";
import Contact from "./pages/Contact";
import NoPage from "./pages/NoPage";
// import "./App.css";

class App extends Component {
    render() {
        return (
            <Router>
                <div className="AppContainer">

                    <Routes>
                        <Route
                            path="/"
                            element={<Home />}
                        ></Route>
                        <Route
                            path="/discount"
                            element={<Discount />}
                        ></Route>
                    </Routes>
                </div>
            </Router>
        );
    }
}

export default App;
