import { Outlet, Link } from "react-router-dom";
import "./App.css";
import { useState } from "react";

const Layout = () => {

const [email, setEmail] = useState("");
const [message, setMessage] = useState("");


const handleSubmit = async (e) => {
  e.preventDefault();
  try {
    let res = await fetch("http://localhost:8000/apis/basic/", {
      method: "POST",
      headers: {
        'Accept': 'application/json',
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({
        email: email,
      }),
    });
    let resJson = await res.json();
    if (res.status === 200) {
      setEmail("");
      setMessage("Subscribed to Newsletter! Please check your email for a surprise");
    } else {
      setMessage("Some error occured");
    }
  } catch (err) {
    console.log(err);
  }
};

return (
  <div className="App">
    <div id="subscribe-form-wrap">
      <h1>
        Subscribe to Our Newsletter!
      </h1>
        <form onSubmit={handleSubmit} id="subscribe-form">
          <p>
            <input
              type="text"
              value={email}
              placeholder="Email"
              onChange={(e) => setEmail(e.target.value)}
            />
          </p>
          <p>
            <input type="submit" id="submit" value="Subscribe"/>
          </p>
          <div className="message">{message ? <p>{message}</p> : null}</div>
        </form>
    </div>
  </div>
);
};

export default Layout;