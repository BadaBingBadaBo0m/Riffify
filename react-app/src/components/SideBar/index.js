import React from 'react';
import { useSelector } from 'react-redux';
import './sidebar.css';
import { useHistory } from 'react-router-dom';
import OpenModalButton from '../OpenModalButton';
import AlbumForm from '../AlbumForm';

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
          <div id='owned-albums-'>
            {/* <span id='create-album' onClick={() => history.push('/new-album')}>Create new album</span> */}
            <div id='create-album'>
              {!user && <button onClick={() => alert('Must be logged in')}>Create a album</button>}
              {user && <OpenModalButton buttonText={'Create new album'} modalComponent={<AlbumForm type={'create'} />} />}
            </div>
          </div>
        </div>
      </div>
    </div>
  )
}

export default SideBar