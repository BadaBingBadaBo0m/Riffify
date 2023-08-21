import React, { useState } from "react";
import { useDispatch } from "react-redux";
import { useModal } from "../../context/Modal";
import { signUp } from "../../store/session";
import "./SignupForm.css";

function SignupFormModal() {
  const dispatch = useDispatch();
  const [email, setEmail] = useState("");
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const [firstName, setFirstName] = useState("");
  const [lastName, setLastName] = useState("");
  const [confirmPassword, setConfirmPassword] = useState("");
  const [errors, setErrors] = useState({});
  const { closeModal } = useModal();

  const validateEmail = (email) => {
    return email.match(
      // eslint-disable-next-line
      /^(([^<>()[\]\\.,;:\s@\"]+(\.[^<>()[\]\\.,;:\s@\"]+)*)|(\".+\"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/
    );
  };

  const handleFlaskErrors = (errorsList) => {
    let errorObj = {}
    for (let i = 0; i < errorsList.length; i++) {
      const splitError = errorsList[i].split(':')
      errorObj[splitError[0].trim()] = splitError[1]
    }
    // console.log('obj', errorObj)
    setErrors(errorObj)
    console.log(errorsList)
  }

  const validateData = () => {
    const errorObj = {}

    if (!validateEmail(email)) errorObj.email = ' Must be valid'
    // if (validateEmail(email)) delete errorObj.email
    // if (!username) errorObj.username = ' Field is required'
    if (username.length < 5) errorObj.username = ' Must be at least 5 characters'
    if (username.length > 10) errorObj.username = ' Must be shorter than 10 characters'

    // if (!firstName) errorObj.firstName = ' Field is required'
    if (firstName.length < 2) errorObj.firstName = ' Must be at least 2 characters'
    if (firstName.length > 10) errorObj.firstName = ' Must be shorter than 10 characters'

    // if (!lastName) errorObj.lastName = ' Field is required'
    if (lastName.length < 2) errorObj.lastName = ' Must be at least 2 characters'
    if (lastName.length > 10) errorObj.lastName = ' Must be shorter than 10 characters'

    if (password.length < 6) errorObj.password = ' Must be at least 6 characters'
    if (password.length > 15) errorObj.password = ' Must be shorter than 15 characters'

    if (password !== confirmPassword) errorObj.password = ' Passwords must match'

    setErrors(errorObj)
    console.log(errorObj)
    if (!Object.keys(errorObj).length) return true
    else return false

  }

  const handleSubmit = async (e) => {
    e.preventDefault();
    if (validateData()) {
      const data = await dispatch(signUp(username, firstName, lastName, email, password));
      if (data) {
        handleFlaskErrors(data)
      } else {
        closeModal()
      }
    }
  };

  return (
    <div id="signUp-form-container">
      <h1>Sign Up</h1>
      <form onSubmit={handleSubmit} id="signUp-form">

        <div className="signUp-inputs-labels">
          <label className="signUp-labels">Email{errors.email && <span>:</span>}{errors.email && <span className="errors">{errors.email}</span>}</label>
          <input
            type="text"
            value={email}
            onChange={(e) => setEmail(e.target.value)}
            required
            className="signUp-inputs"
          />
        </div>

        <div className="signUp-inputs-labels">
          <label className="signUp-labels">Username{errors.username && <span>:</span>}{errors.username && <span className="errors">{errors.username}</span>}</label>
          <input
            type="text"
            value={username}
            onChange={(e) => setUsername(e.target.value)}
            required
            className="signUp-inputs"
          />
        </div>

        <div id="first-last-name-errors-container">
          {errors.firstName && <span className="errors">First name:{errors.firstName}</span>}
          {errors.lastName && <span className="errors">Last name:{errors.lastName}</span>}
        </div>

        <div id="first-last-name">
          <div>
            <label className="first-name-label">First name</label>
            <input
              type="text"
              value={firstName}
              onChange={(e) => setFirstName(e.target.value)}
              required
              className="first-name-inputs"
            />
          </div>

          <div>
            <label className="last-name-label">Last name</label>
            <input
              type="text"
              value={lastName}
              onChange={(e) => setLastName(e.target.value)}
              required
              className="last-name-inputs"
            />
          </div>
        </div>

        <div className="signUp-inputs-labels">
          <label className="signUp-labels">Password{errors.password && <span className="errors">{errors.password}</span>}</label>
          <input
            type="password"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
            required
            className="signUp-inputs"
          />
        </div>

        <div className="signUp-inputs-labels">
          <label className="signUp-labels">Confirm Password</label>
          <input
            type="password"
            value={confirmPassword}
            onChange={(e) => setConfirmPassword(e.target.value)}
            required
            className="signUp-inputs"
          />
        </div>

        <button type="submit" id="signUp-form-button">Sign Up</button>

      </form>
    </div>
  );
}

export default SignupFormModal;