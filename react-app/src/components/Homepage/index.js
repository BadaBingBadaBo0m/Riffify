import React, { useState, useContext } from 'react'
import SideBar from '../SideBar'
import MediaPlayer from '../MediaPlayer'
import Navbar from '../Navbar'
import { SongContext } from '../../context/Song';

import './homepage.css'

const HomePage = ({ Content }) => {
  const { currentSong, setCurrentSong, contextAlbum } = useContext(SongContext)

  return (
    <div id='home-container'>
      <SideBar />

      <div id='main-content'>
        <div id='navbar-container'>
          <Navbar />
        </div>
        <div id='content-container'>
          <Content />
        </div>
      </div>

      <MediaPlayer />
    </div>
  )
}

export default HomePage