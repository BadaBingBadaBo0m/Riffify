import React, { useState, useEffect } from 'react'
import { useHistory } from 'react-router-dom'
import { useSelector, useDispatch } from "react-redux";
import Loading from '../Loading';
import { getAllAlbums } from "../../store/albums";
import './recommended.css'

const Recommended = () => {
  const dispatch = useDispatch();
  const history = useHistory()
  const albums = useSelector((state) => state.albums.albumList?.albums)

  useEffect(() => {
    dispatch(getAllAlbums())
  }, [])

  if (!albums) return <Loading />

  return (
    <>
      <div id='recommended-container'>
        {/* <div id='recommended-playlists-container'>
          <h1 id='recommended-playlists-title'>Tritone Playlists</h1>
        </div> */}
        <div id='recommended-albums'>
          <h1 id='recommended-albums-title'>Albums</h1>
          <ul id='album-list-container'>
            {albums.map((album) => (
              <li key={album.id} id='single-album' onClick={() => history.push(`/albums/${album.id}`)}>
                <img id='album-art-list' src={album.art}></img>
                <p id='album-name'>{album.name}</p>
              </li>
            ))}
          </ul>
        </div>
      </div>
    </>
  )
}

export default Recommended