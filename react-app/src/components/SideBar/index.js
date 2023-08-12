import React, { useEffect, useRef, useState } from 'react';
import { useSelector } from 'react-redux';
import './sidebar.css';
import { useHistory } from 'react-router-dom';
import OpenModalButton from '../OpenModalButton';
import LoginFormModal from '../LoginFormModal'
import SignupFormModal from '../SignupFormModal';
import AlbumForm from '../AlbumForm';
import { Tooltip } from 'react-tooltip';

const SideBar = () => {
  const [albumTooltip, setAlbumTooltip] = useState(false)
  const history = useHistory();
  const user = useSelector((state) => state.session.user)

  useEffect(() => {
    if (albumTooltip === true) {
      const tooltipTimeout = setTimeout(() => {
        setAlbumTooltip(false)
      }, 5000);

      return () => {
        clearTimeout(tooltipTimeout)
      }
    }
  })

  return (
    <>
      <div id='side-bar-container'>
        <ul id='home-button-container'>
          <li>
            <button onClick={() => history.push('/')}>Home</button>
          </li>
          <li>
            <button>Search</button>
          </li>
        </ul>

        <div id='playlist-container'>
          <div id='library-container'>
            <h2 id='library-heading'>Your Library</h2>
            <div id='create-first-playlist'>
              <h2 id='first-playlist-heading'>Create your first playlist</h2>
              <p id='first-playlist-desc'>It's easy, we'll help you</p>
              <span id='create-playlist-button'>Create playlist</span>
            </div>
          </div>

          <div id='owned-albums-container' data-tooltip-id='create-album-tooltip'>
            <h2 id='owned-albums-title'>Your Albums</h2>

            <div id='create-album-button-container'>
              {!user && <button id='dead-create-album' onClick={() => setAlbumTooltip(true)}>Create a album</button>}
              {user && <OpenModalButton buttonText={'Create new album'} modalComponent={<AlbumForm type={'create'} />} />}
            </div>
          </div>
        </div>
      </div>
      <Tooltip
        id='create-album-tooltip'
        variant='info'
        openOnClick
        clickable
        place='right'
        className='create-album-tooltip'
        opacity={1}
        isOpen={albumTooltip}
      >
        <div id='album-tooltip-header-container'>
          <h2 id='album-tooltip-header'>Create a Album</h2>
          <p id='album-tooltip-sub-header'>Login to create a album</p>
        </div>

        <div id='album-tooltip-button-container'>
          <div className='login-button' onClick={() => setAlbumTooltip(false)}>
            <OpenModalButton buttonText={'Login'} modalComponent={<LoginFormModal />} />
          </div>
          <div id='album-tooltip-signUp-button' onClick={() => setAlbumTooltip(false)}>
            <OpenModalButton buttonText={'Sign up'} modalComponent={<SignupFormModal />} />
          </div>
        </div>
      </Tooltip>
    </>
  )
}

export default SideBar