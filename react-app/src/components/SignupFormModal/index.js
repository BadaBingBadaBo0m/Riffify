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
  const [errors, setErrors] = useState([]);
  const { closeModal } = useModal();

  const handleSubmit = async (e) => {
    e.preventDefault();
    if (password === confirmPassword) {
      const data = await dispatch(signUp(username, firstName, lastName, email, password));
      if (data) {
        setErrors(data);
      } else {
        closeModal();
      }
    } else {
      setErrors([
        "Confirm Password field must be the same as the Password field",
      ]);
    }
  };

  return (
    <div id="signUp-form-container">
      <h1>Sign Up</h1>
      <form onSubmit={handleSubmit} id="signUp-form">
        <ul id="signUp-form-errors">
          {errors.map((error, idx) => (
            <li key={idx}>{error}</li>
          ))}
        </ul>

        <div className="signUp-inputs-labels">
          <label className="signUp-labels">Email</label>
          <input
            type="text"
            value={email}
            onChange={(e) => setEmail(e.target.value)}
            required
            className="signUp-inputs"
          />
        </div>

        <div className="signUp-inputs-labels">
          <label className="signUp-labels">Username</label>
          <input
            type="text"
            value={username}
            onChange={(e) => setUsername(e.target.value)}
            required
            className="signUp-inputs"
          />
        </div>

        <div id="first-last-name">
          <div>
            <label className="first-name-label">Fist name</label>
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
          <label className="signUp-labels">Password</label>
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