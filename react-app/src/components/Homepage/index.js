import React, { useState, useContext } from 'react'
import SideBar from '../SideBar'
import MediaPlayer from '../MediaPlayer'
import Navbar from '../Navbar'

import './homepage.css'

const HomePage = ({ Content, type }) => {

  return (
    <div id='home-container'>
      <SideBar />

      <div id='main-content'>
        <div id='navbar-container'>
          <Navbar />
        </div>
        <div id='content-container'>
          <Content type={type ? type : ''} />
        </div>
      </div>

      <MediaPlayer />
    </div>
  )
}

export default HomePage