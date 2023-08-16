import React, { useContext } from 'react'
import { useSelector, useDispatch } from "react-redux";
import { useHistory } from 'react-router-dom'
import { logout } from '../../store/session';
import { SongContext } from '../../context/Song';
import OpenModalButton from '../OpenModalButton'
import LoginFormModal from '../LoginFormModal'
import SignupFormModal from '../SignupFormModal';
import './navbar.css'

const Navbar = () => {
  const dispatch = useDispatch()
  const history = useHistory()
  const user = useSelector((state) => state.session.user)
  const { setCurrentSong } = useContext(SongContext)

  const handleLogout = async () => {
    await dispatch(logout())
    history.push('/')
    setCurrentSong(null)
  }

  return (
    <div id='navBar-container'>
      <div id='back-forward-button-container'>
        {/* <button> <i class="fa-solid fa-arrow-left"></i> </button>
        <button> <i className="fa-solid fa-arrow-right"></i> </button> */}
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
          <button className='logout-button' onClick={handleLogout}>Logout</button>
        </div>}

    </div>
  )
}

export default Navbar