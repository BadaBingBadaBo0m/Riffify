import React, { useEffect, useContext, useState } from 'react'
import { SongContext } from '../../context/Song';
import { useParams } from 'react-router-dom'
import { useSelector, useDispatch } from "react-redux";
import Loading from '../Loading';
import { getLikedSongs, getPlaylist, getPlaylistSongs, addSongToLikedSongs, removeSongFromLikedSongs } from '../../store/playlists';
import PlaylistDropdown from '../PlaylistDropdown';
import SongDropdown from '../SongDropdown';
import './playlist.css'
import PlaylistSongDropdown from '../PlaylistSongDropdown';

const PlaylistInfo = () => {
  const { playlistId } = useParams()
  const dispatch = useDispatch()
  const user = useSelector((state) => state.session.user)
  const playlist = useSelector((state) => state.playlists.singlePlaylist)
  const songList = useSelector((state) => state.playlists.playlistSongs)
  const { setCurrentSong, currentSong, setContextSongList, contextAlbum, setContextAlbum, play, setPlay, contextPlaylist, setContextPlaylist } = useContext(SongContext)
  const [playButton, setPlayButton] = useState(false)
  let songCount = 0

  useEffect(() => {
    dispatch(getPlaylist(playlistId))
    dispatch(getPlaylistSongs(playlistId))
  }, [playlistId])

  if (!playlist || !songList || playlist.id != playlistId) return <Loading />

  const handleSongChange = (song) => {
    setCurrentSong(song)
    setContextSongList(songList)
    setContextAlbum(song.album)
    setContextPlaylist(playlist)
    setPlay(true)
  }

  const handlePlaylistPlayButton = () => {
    if (!currentSong) {
      setCurrentSong(songList[0])
      setPlay(true)
      setContextSongList(songList)
      setContextAlbum(songList[0].album)
      setContextPlaylist(playlist)
    }
    if (currentSong && contextPlaylist.id === playlist.id) {
      setPlay(true)
    }
    if (currentSong && contextPlaylist.id !== playlist.id) {
      setCurrentSong(songList[0])
      setPlay(true)
      setContextSongList(songList)
      setContextAlbum(songList[0].album)
      setContextPlaylist(playlist)
    }
  }

  const handleLike = async (song) => {
    await dispatch(addSongToLikedSongs(song.id))
    dispatch(getPlaylistSongs(playlistId))
  }

  const handleUnLike = async (song) => {
    await dispatch(removeSongFromLikedSongs(song.id))
    dispatch(getPlaylistSongs(playlistId))
  }

  return (
    <div id='playlist-details-container'>
      <div id='playlist-banner-container'>
        <img src={playlist.picture} id='album-details-cover'></img>
        <div id='album-info-container'>
          <p>Playlist</p>
          <h1>{playlist.name}</h1>
          <div id='album-creator-info-container'>
          </div>
        </div>
      </div>

      <div id='album-dropdown-play-button'>
        <div id='play-button-like-container'>

          {user &&
            contextPlaylist && contextPlaylist !== 'likedSongs' && contextPlaylist.id === playlist.id && play === true
            ?
            <button
              id='album-play-button'
              onClick={() => setPlay(false)}
            >
              {<i className="fa-solid fa-pause"></i>}
            </button>
            :
            <button
              id='album-play-button'
              onClick={handlePlaylistPlayButton}
            >
              {<i className="fa-solid fa-play"></i>}
            </button>}

          <PlaylistDropdown playlist={playlist} />
        </div>
      </div>

      <ul id='song-list'>
        {songList.map(song => {
          songCount++
          return (
            <li className='song-container' onMouseEnter={() => setPlayButton(true)} onMouseLeave={() => setPlayButton(false)}>
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
                {/* {user && <button
                  className='song-list-play-button'
                  onClick={() => handleSongChange(song)}
                > {<i className="fa-solid fa-play"></i>}
                </button>} */}
                <img src={song.album.art} id='playlist-song-album-art'></img>
                <div className='song-info'>
                  <p className='song-name'>{song.name}</p>
                  <p className='artist-name'>{song.album.created_by.username}</p>
                </div>
              </div>
              <div className='like-song-button-n-dropdown-container'>
                {!song.liked && <button className={`${song.id} like-button`} onClick={() => handleLike(song)}> <i className="fa-regular fa-heart"></i> </button>}
                {song.liked && <button className={`${song.id} liked-button`} onClick={() => handleUnLike(song)}> <i className="fa-solid fa-heart"></i> </button>}
                <PlaylistSongDropdown playlist={playlist} song={song} />
              </div>
              {/* <SongDropdown song={song} album={album} /> */}
            </li>
          )
        })}
      </ul>

    </div >

  )
}

export default PlaylistInfo