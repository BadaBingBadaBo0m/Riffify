import React from 'react';
import { useSelector } from 'react-redux';
import './sidebar.css';
import { useHistory } from 'react-router-dom';
import OpenModalButton from '../OpenModalButton';
import AlbumForm from '../AlbumForm';
import { Tooltip } from 'react-tooltip';

const SideBar = () => {
  const history = useHistory();
  const user = useSelector((state) => state.session.user)

  return (
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

        <div
          id='owned-albums-container'
        >
          <h2 id='owned-albums-title'>Your Albums</h2>
          <div id='create-album-button-container' data-tooltip-id='create-album-tooltip'>
            {!user && <button id='dead-create-album'>Create a album</button>}
            {user && <OpenModalButton buttonText={'Create new album'} modalComponent={<AlbumForm type={'create'} />} />}
          </div>

          <div id='owned-albums-'>
          </div>
        </div>
      </div>
      <Tooltip id='create-album-tooltip' variant='info' openOnClick clickable place='right'>
        <span>Test</span>
      </Tooltip>
    </div>
  )
}

export default SideBar