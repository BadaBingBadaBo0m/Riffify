import React from 'react'
import './sidebar.css'
import { useHistory } from 'react-router-dom'

const SideBar = () => {
  const history = useHistory()

  const testRedirect = () => {
    history.push('/test')
  }

  return (
    <div id='side-bar-container'>
      <ul id='home-button-container'>
        <li>
          <button onClick={testRedirect}>Home</button>
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

        <div id='owned-albums-container'>
          <h2 id='owned-albums-title'>Your Albums</h2>
          <div id='owned-albums-'>
            <span id='create-album'>Create new album</span>
          </div>
        </div>
      </div>

      <div id='album-container'>

      </div>
    </div>
  )
}

export default SideBar