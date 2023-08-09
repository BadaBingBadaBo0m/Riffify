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
        <Navbar />
        <Content />
      </div>

      <MediaPlayer />
    </div>
  )
}

export default HomePage