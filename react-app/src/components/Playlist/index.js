import React, { useEffect, useContext, useState } from 'react'
import { SongContext } from '../../context/Song';
import { useParams } from 'react-router-dom'
import { useSelector, useDispatch } from "react-redux";
import Loading from '../Loading';
import { getPlaylist, getPlaylistSongs } from '../../store/playlists';
import AlbumDropdown from '../AlbumDropdown';
import SongDropdown from '../SongDropdown';
import './playlist.css'

const PlaylistInfo = () => {
  const { playlistId } = useParams()
  const dispatch = useDispatch()
  const user = useSelector((state) => state.session.user)
  const playlist = useSelector((state) => state.playlists.singlePlaylist)
  const songList = useSelector((state) => state.playlists.playlistSongs)
  const { setCurrentSong, currentSong, setContextSongList, setContextAlbum, play, setPlay } = useContext(SongContext)
  const [playButton, setPlayButton] = useState(false)
  let songCount = 0

  useEffect(() => {
    dispatch(getPlaylist(playlistId))
    dispatch(getPlaylistSongs(playlistId))
  }, [playlistId])

  if (!playlist || !songList) return <Loading />

  const handleSongChange = (song) => {
    setCurrentSong(song)
    setContextSongList(songList)
    setContextAlbum(song.album)
  }

  // console.log(user.id, album)
  return (
    <div id='playlist-details-container'>
      <div id='playlist-banner-container'>
        <img src={playlist.picture} id='album-details-cover'></img>
        <div id='album-info-container'>
          <p>Playlist</p>
          <h1>{playlist.name}</h1>
          <div id='album-creator-info-container'>
            {/* <img src={user.profile_pic} id='artistPfp'></img> */}
            {/* <p>{playlist.created_by?.username} &#x2022; {albumDate.getFullYear()} &#x2022; {songList.length} songs</p> */}
          </div>
        </div>
      </div>

      <div id='album-dropdown-play-button'>
        <div id='play-button-like-container'>
          <button id='album-play-button'> {<i className="fa-solid fa-play"></i>} </button>
          {/* <AlbumDropdown album={album} /> */}
        </div>
      </div>

      <ul id='song-list'>
        {songList.map(song => {
          songCount++
          return (
            <li className='song-container' onMouseEnter={() => setPlayButton(true)} onMouseLeave={() => setPlayButton(false)}>
              <div className='song-count-and-controls-container'>
                <p className='song-count'>{songCount}</p>
                <img src={song.album.art} id='playlist-song-album-art'></img>
                {user && <button
                  className='song-list-play-button'
                  onClick={() => handleSongChange(song)}
                > {<i className="fa-solid fa-play"></i>}
                </button>}
                <div className='song-info'>
                  <p className='song-name'>{song.name}</p>
                  <p className='artist-name'>{song.album.created_by.username}</p>
                </div>
              </div>
              {/* <SongDropdown song={song} album={album} /> */}
            </li>
          )
        })}
      </ul>

    </div>

  )
}

export default PlaylistInfo