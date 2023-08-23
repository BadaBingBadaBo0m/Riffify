import React from 'react'
import ScaleLoader from "react-spinners/ScaleLoader";
import './loading.css'

const Loading = () => {

  return (
    <div id='loading-container'>
      <ScaleLoader color='#1ed760' height={50} width={5} radius={50} />
    </div>
  )
}

export default Loading