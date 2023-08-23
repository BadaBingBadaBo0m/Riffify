import React, { useEffect, useContext } from 'react'
import { SongContext } from '../../context/Song';
import { useParams } from 'react-router-dom'
import { useSelector, useDispatch } from "react-redux";
import Loading from '../Loading';
import { getSingleAlbum, getSongsForAlbum } from '../../store/albums';
import { addSongToLikedSongs, removeSongFromLikedSongs } from '../../store/playlists'
import AlbumDropdown from '../AlbumDropdown';
import SongDropdown from '../SongDropdown';
import './albuminfo.css'

const AlbumInfo = () => {
  const { albumId } = useParams()
  const dispatch = useDispatch()
  const user = useSelector((state) => state.session.user)
  const album = useSelector((state) => state.albums.singleAlbum)
  const songList = useSelector((state) => state.albums.albumSongs)
  const { setCurrentSong, currentSong, setContextSongList, setContextAlbum, play, setPlay } = useContext(SongContext)
  let songCount = 0

  useEffect(() => {
    dispatch(getSingleAlbum(albumId))
    dispatch(getSongsForAlbum(albumId, user?.id))
  }, [albumId, user])

  const handleSongChange = (song) => {
    setCurrentSong(song)
    setPlay(true)
    setContextSongList(songList)
    setContextAlbum(album)
  }

  const handleLike = async (song) => {
    await dispatch(addSongToLikedSongs(song.id))
    await dispatch(getSongsForAlbum(albumId, user?.id))
  }

  const handleUnLike = async (song) => {
    await dispatch(removeSongFromLikedSongs(song.id))
    await dispatch(getSongsForAlbum(albumId, user?.id))
  }

  if (!album || !songList || album.id != albumId) return <Loading />
  const albumDate = new Date(album.created_at)
  // console.log(user.id, album)
  return (
    <div id='album-details-container'>
      <div
        // Remnants from an attempt to make the background the same color as album cover
        // style={{ backgroundImage: `url(${album.art})` }}
        className='blurred-background'>

        <div
          id='album-banner-container'

        >
          <img src={album.art} id='album-details-cover'></img>
          <div id='album-info-container'>
            <p>Album</p>
            <h1>{album.name}</h1>
            <div id='album-creator-info-container'>
              {/* <img src={album.created_by?.profile_pic} id='artistPfp'></img> */}
              <p>{album.created_by?.username} &#x2022; {albumDate.getFullYear()} &#x2022; {songList.length} songs</p>
            </div>
          </div>
        </div>
      </div>

      <div id='album-dropdown-play-button'>
        <div id='play-button-like-container'>
          <button id='album-play-button' onClick={() => handleSongChange(songList[0])}> {<i className="fa-solid fa-play"></i>} </button>
          <AlbumDropdown album={album} />
        </div>
      </div>

      <ul id='song-list'>
        {songList.map(song => {
          songCount++
          return (
            <li className='song-container' data-tooltip-id={`playlist-dropdown-message-${song.id}`}>
              <div className='song-count-and-controls-container'>
                <p className='song-count'>{songCount}</p>
                {user && (!currentSong || currentSong.id !== song.id || play === false) &&
                  <button
                    className='song-list-play-button'
                    onClick={() => handleSongChange(song)}>
                    {<i className="fa-solid fa-play"></i>}
                  </button>}
                {user && currentSong && currentSong.id === song.id && play === true &&
                  <button className='song-list-play-button' onClick={() => setPlay(false)}>
                    {<i className="fa-solid fa-pause"></i>}
                  </button>}
                <div className='song-info'>
                  <p className='song-name'>{song.name}</p>
                  <p className='artist-name'>{album.created_by?.username}</p>
                </div>
              </div>
              <div className='like-song-button-n-dropdown-container'>
                {user && !song.liked && <button className={`${song.id} like-button`} onClick={() => handleLike(song)}> <i className="fa-regular fa-heart"></i> </button>}
                {user && song.liked && <button className={`${song.id} liked-button`} onClick={() => handleUnLike(song)}> <i className="fa-solid fa-heart"></i> </button>}
                <SongDropdown song={song} album={album} />
              </div>
            </li>
          )
        })}
      </ul>
    </div >
  )
}

export default AlbumInfo