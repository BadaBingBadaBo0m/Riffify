import React, { useState } from "react";
import { login } from "../../store/session";
import { useDispatch } from "react-redux";
import { useModal } from "../../context/Modal";
import "./LoginForm.css";

function LoginFormModal() {
  const dispatch = useDispatch();
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [errors, setErrors] = useState([]);
  const { closeModal } = useModal();

  const handleDemoLogin = async (e) => {
    e.preventDefault();
    const data = await dispatch(login('currents@aa.io', 'password'));
    if (data) {
      setErrors(data);
    } else {
      closeModal()
    }
  }

  const handleFlaskErrors = (errorsList) => {
    let errorObj = {}
    for (let i = 0; i < errorsList.length; i++) {
      const splitError = errorsList[i].split(':')
      errorObj[splitError[0].trim()] = splitError[1]
    }
    // console.log('obj', errorObj)
    setErrors(errorObj)
    console.log(errorObj)
  }

  const handleSubmit = async (e) => {
    e.preventDefault();
    const data = await dispatch(login(email, password));
    if (data) {
      handleFlaskErrors(data)
    }
  };

  return (
    <div id="login-form-container">
      <h1>Log in to Tritone</h1>
      <form onSubmit={handleSubmit} id="login-form">
        {/* <ul id="login-form-errors">
          {errors.map((error, idx) => (
            <li key={idx}>{error}</li>
          ))}
        </ul> */}

        <div className="login-inputs-labels">
          <label className="login-labels">Email{errors.email && <span>:</span>}{errors.email && <span className="errors"> {errors.email}</span>}</label>
          <input
            type="text"
            value={email}
            onChange={(e) => setEmail(e.target.value)}
            className='login-inputs'
            required
          />
        </div>

        <div className="login-inputs-labels">
          <label className="login-labels">Password{errors.password && <span>:</span>}{errors.password && <span className="errors"> {errors.password}</span>}</label>
          <input
            type="password"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
            className='login-inputs'
            required
          />
        </div>

        <button id="login-form-button" type="submit">Log In</button>

        <button id="login-demo-button" type="submit" onClick={handleDemoLogin}>Demo user</button>
      </form>
    </div>
  );
}

export default LoginFormModal;
