import React, { useEffect, useContext } from 'react'
import { SongContext } from '../../context/Song';
import { useParams } from 'react-router-dom'
import { useSelector, useDispatch } from "react-redux";
import Loading from '../Loading';
import { getSingleAlbum, getSongsForAlbum } from '../../store/albums';
import AlbumDropdown from '../AlbumDropdown';
import SongDropdown from '../SongDropdown';
// import './albuminfo.css'

const PlaylistInfo = () => {
  const { playlistId } = useParams()
  const dispatch = useDispatch()
  const user = useSelector((state) => state.session.user)
  const { setCurrentSong, currentSong, setContextSongList, setContextAlbum, play, setPlay } = useContext(SongContext)
  let songCount = 0

  useEffect(() => {
    // dispatch(get)
    // dispatch(getSongsForAlbum(albumId))
  }, [playlistId])

  // const handleSongChange = (song) => {
  //   setCurrentSong(song)
  //   setContextSongList(songList)
  //   setContextAlbum(album)
  // }


  // console.log(user.id, album)
  return (
    <div>
      <h1>test</h1>
    </div>
  )
}

export default PlaylistInfo