import React, { useState } from 'react'
import SideBar from '../SideBar'
import MediaPlayer from '../MediaPlayer'
import Navbar from '../Navbar'

import './homepage.css'

const HomePage = ({ Content }) => {

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