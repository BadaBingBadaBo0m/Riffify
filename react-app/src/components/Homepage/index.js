import React from 'react'
import SideBar from '../SideBar'
import Recommended from '../Recommended'
import './homepage.css'

const HomePage = () => {


  return (
    <div id='home-container'>
      <SideBar />

      <div id='main-content'>
        <Recommended />
      </div>
    </div>
  )
}

export default HomePage