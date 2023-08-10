import React, { useEffect, useState } from 'react'
import { useParams } from 'react-router-dom'
import { useSelector, useDispatch } from "react-redux";
import Loading from '../Loading';
import { getSingleAlbum, getSongsForAlbum } from '../../store/albums';
import AlbumDropdown from '../AlbumDropdown';
import './albuminfo.css'

const AlbumInfo = () => {
  const { albumId } = useParams()
  const dispatch = useDispatch()
  const user = useSelector((state) => state.session.user)
  const album = useSelector((state) => state.albums.singleAlbum)
  const songList = useSelector((state) => state.albums.albumSongs)
  let songCount = 0

  useEffect(() => {
    dispatch(getSingleAlbum(albumId))
    dispatch(getSongsForAlbum(albumId))
  }, [])

  if (!album || !songList) return <Loading />
  const albumDate = new Date(album.created_at)
  // console.log(user.id, album)
  return (
    <div id='album-details-container'>
      {/* <div
        style={{ backgroundImage: `url(${album.art})`, filter: 'blur(50px)', transform: 'scale(3)' }}
      >
      </div> */}
      <div
        id='album-banner-container'
      // style={{ backgroundImage: `url(${album.art})`, filter: 'blur(50px)', transform: 'scale(3)' }}
      >
        <img src={album.art} id='album-details-cover'></img>
        <div id='album-info-container'>
          <p>Album</p>
          <h1>{album.name}</h1>
          <div id='album-creator-info-container'>
            <img src={album.profile_pic} id='artistPfp'></img>
            <p>{album.username} &#x2022; {albumDate.getFullYear()} &#x2022; {songList.length} songs</p>
          </div>
        </div>
      </div>

      <div id='song-list-container'>
        <div id='play-button-like-container'>
          <button id='album-play-button'> {<i className="fa-solid fa-play"></i>} </button>
          <AlbumDropdown album={album} />
        </div>
      </div>

      <ul id='song-list'>
        {songList.map(song => {
          songCount++
          return (
            <li className='song-container'>
              <p className='song-count'>{songCount}</p>
              <div className='song-info'>
                <p className='song-name'>{song.name}</p>
                <p className='artist-name'>{album.username}</p>
              </div>
            </li>
          )
        })}
      </ul>
    </div >
  )
}

export default AlbumInfo