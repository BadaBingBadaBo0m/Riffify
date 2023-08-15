import React, { useEffect, useContext, useState } from 'react'
import { SongContext } from '../../context/Song';
import { useParams } from 'react-router-dom'
import { useSelector, useDispatch } from "react-redux";
import Loading from '../Loading';
import { getLikedSongs, getPlaylist, getPlaylistSongs, addSongToLikedSongs, removeSongFromLikedSongs } from '../../store/playlists';
import PlaylistDropdown from '../PlaylistDropdown';
import SongDropdown from '../SongDropdown';
import PlaylistSongDropdown from '../PlaylistSongDropdown';
// import './playlist.css'

const LikedSongs = () => {
  const dispatch = useDispatch()
  const user = useSelector((state) => state.session.user)
  // const playlist = useSelector((state) => state.playlists.singlePlaylist)
  const songList = useSelector((state) => state.playlists.playlistSongs)
  const { setCurrentSong, currentSong, setContextSongList, setContextAlbum, play, setPlay } = useContext(SongContext)
  const [playButton, setPlayButton] = useState(false)
  let songCount = 0

  useEffect(() => {
    dispatch(getLikedSongs())
  }, [])

  if (!songList) return <Loading />

  const handleSongChange = (song) => {
    setCurrentSong(song)
    setContextSongList(songList)
    setContextAlbum(song.album)
  }

  const handleLike = async (song) => {
    await dispatch(addSongToLikedSongs(song.id))
    await dispatch(getLikedSongs())
  }

  const handleUnLike = async (song) => {
    await dispatch(removeSongFromLikedSongs(song.id))
    await dispatch(getLikedSongs())
  }

  return (
    <div id='playlist-details-container'>
      <div id='playlist-banner-container'>
        <img src='/likedSongs.png' id='album-details-cover'></img>
        <div id='album-info-container'>
          <p>Playlist</p>
          <h1>Liked Songs</h1>
          <div id='album-creator-info-container'>
          </div>
        </div>
      </div>

      <div id='album-dropdown-play-button'>
        <div id='play-button-like-container'>
          <button id='album-play-button' onClick={() => handleSongChange(songList[0])}> {<i className="fa-solid fa-play"></i>} </button>
        </div>
      </div>

      <ul id='song-list'>
        {songList.map(song => {
          songCount++
          return (
            <li className='song-container' onMouseEnter={() => setPlayButton(true)} onMouseLeave={() => setPlayButton(false)}>
              <div className='song-count-and-controls-container'>
                <p className='song-count'>{songCount}</p>
                {user && <button
                  className='song-list-play-button'
                  onClick={() => handleSongChange(song)}
                > {<i className="fa-solid fa-play"></i>}
                </button>}
                <img src={song.album.art} id='playlist-song-album-art'></img>
                <div className='song-info'>
                  <p className='song-name'>{song.name}</p>
                  <p className='artist-name'>{song.album.created_by.username}</p>
                </div>
              </div>
              <div className='like-song-button-n-dropdown-container'>
                {!song.liked && <button className={`${song.id} like-button`} onClick={() => handleLike(song)}> <i className="fa-regular fa-heart"></i> </button>}
                {song.liked && <button className={`${song.id} liked-button`} onClick={() => handleUnLike(song)}> <i className="fa-solid fa-heart"></i> </button>}
              </div>
            </li>
          )
        })}
      </ul>

    </div>

  )
}

export default LikedSongs