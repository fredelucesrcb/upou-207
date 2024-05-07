// import "./Discount.css";
import { useState } from "react";

const Discount = () => {

const [code, setCode] = useState("");
const [message, setMessage] = useState("");


const handleSubmit = async (e) => {
  e.preventDefault();
  try {
    let res = await fetch("http://localhost:8000/apis/discount/", {
      method: "POST",
      headers: {
        'Accept': 'application/json',
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({
        code: code,
      }),
    });
    let resJson = await res.json();
    console.log(resJson);
    if (res.status === 200) {
      setCode("");
      setMessage("Discount code valid! redirecting back to checkout page");
    } else {
      setMessage("Discount code invalid");
    }
  } catch (err) {
    setMessage("Discount code invalid");
  }
};

return (
  <div className="App">
    <div id="subscribe-form-wrap">
      <h1>
        Enter Discount Code
      </h1>
        <form onSubmit={handleSubmit} id="subscribe-form">
          <p>
            <input
              type="text"
              value={code}
              placeholder="Discount Code"
              onChange={(e) => setCode(e.target.value)}
            />
          </p>
          <p>
            <input type="submit" id="submit" value="Enter Discount Code"/>
          </p>
          <div className="message">{message ? <p>{message}</p> : null}</div>
        </form>
    </div>
  </div>
);
};

export default Discount;