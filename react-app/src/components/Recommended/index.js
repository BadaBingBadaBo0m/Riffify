import React, { useState, useEffect } from 'react'
import { useSelector, useDispatch } from "react-redux";
import Loading from '../Loading';
import { getAllAlbums } from "../../store/albums";
import './recommended.css'

const Recommended = () => {
  const dispatch = useDispatch();
  const albums = useSelector((state) => state.albums.albumList)

  useEffect(() => {
    dispatch(getAllAlbums())
  }, [])

  if (!albums) return <Loading />

  return (
    <>
      <div id='recommended-container'>
        <h1 id='recommended'>Recommended</h1>
      </div>
    </>
  )
}

export default Recommended