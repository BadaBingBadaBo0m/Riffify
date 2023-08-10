import React from 'react'
import { useSelector, useDispatch } from "react-redux";
import { logout } from '../../store/session';
import OpenModalButton from '../OpenModalButton'
import LoginFormModal from '../LoginFormModal'
import SignupFormModal from '../SignupFormModal';
import './navbar.css'

const Navbar = () => {
  const dispatch = useDispatch()
  const user = useSelector((state) => state.session.user)


  return (
    <div id='navBar-container'>
      <div id='back-forward-button-container'>
        <button> <i class="fa-solid fa-arrow-left"></i> </button>
        <button> <i className="fa-solid fa-arrow-right"></i> </button>
      </div>

      {user === null &&
        <div id='signup-login-button-container'>
          <div id='signUp-button'>
            <OpenModalButton buttonText={'Sign up'} modalComponent={<SignupFormModal />} />
          </div>
          <div className='login-button'>
            <OpenModalButton buttonText={'Login'} modalComponent={<LoginFormModal />} />
          </div>
        </div>}

      {user &&
        <div>
          <button className='logout-button' onClick={() => dispatch(logout())}>Logout</button>
        </div>}

    </div>
  )
}

export default Navbar