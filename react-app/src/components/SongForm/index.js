import React, { useState, useContext } from 'react'
import './songform.css'
import { useDispatch } from 'react-redux';
import { createSongForAlbum, getSongsForAlbum, updateSong } from '../../store/albums';
import { useModal } from '../../context/Modal';
import { SongContext } from '../../context/Song';

const SongForm = ({ type, albumId, song }) => {
  const [errors, setErrors] = useState({});
  const [song_body, setSong_body] = useState(null);
  const [title, setTitle] = useState('')
  const [name, setName] = useState(song?.name || null);
  const [imageLoading, setImageLoading] = useState(false);
  const dispatch = useDispatch()
  const { closeModal } = useModal()
  const { setContextSongList } = useContext(SongContext)

  const validateData = () => {
    const errorObj = {};

    if (!name) errorObj.name = 'is required.'
    if (name && name.length > 50) errorObj.name = 'length cannot be greater than 50.'

    if (type == 'create') {
      if (!song_body) errorObj.song_body = 'is required.'
    }

    setErrors(errorObj)
    if (Object.keys(errorObj).length) return false
    else return true
  }

  const handleSubmit = async (e) => {
    e.preventDefault()

    const isValid = validateData()

    if (isValid && type == 'create') {
      const formData = new FormData();
      formData.append('name', name)
      formData.append('song_body', song_body)
      setImageLoading(true)
      const new_song = await dispatch(createSongForAlbum(albumId, formData))

      if (new_song.errors) {
        setErrors(new_song.errors)
        setImageLoading(false)
      } else {
        const songs = await dispatch(getSongsForAlbum(albumId))
        setContextSongList(songs)
        closeModal()
      }
    }

    if (isValid && type === 'edit') {
      const formData = new FormData();
      formData.append('name', name)

      if (song_body) {
        formData.append('song_body', song_body)
      }
      console.log(song.id)
      setImageLoading(true)
      const updated_song = await dispatch(updateSong(formData, song.id))
      if (updated_song.errors) {
        setErrors(updated_song.errors)
        setImageLoading(false)
      } else {
        const songs = await dispatch(getSongsForAlbum(albumId))
        setContextSongList(songs)
        closeModal()
      }
      // if (updated_song.ok) {
      //   await dispatch(getSongsForAlbum(albumId))
      //   closeModal()
      // }
    }
  }

  return (
    <div id='create-song-container'>
      <form id='create-song-from' encType='multipart/form-data'>
        <h1 id='Song-form-title'>
          {type === 'create' ? 'Create a new Song' : `Edit ${song?.name}`}
        </h1>

        <div className='album-form-input-container'>
          <label htmlFor='name'>Name {errors.name && <span className='errors'>{errors.name}</span>}</label>
          <input
            className='album-form-input'
            type='text'
            value={name}
            onChange={(e) => setName(e.target.value)}
          />
        </div>

        <div className='album-form-input-container'>
          <label htmlFor='name'>Song mp3 {errors.song_body && <span className='errors'>{errors.song_body}</span>}</label>
          <input
            className='album-form-file'
            type='file'
            accept="audio/mp3"
            required={type === 'create'}
            onChange={(e) => setSong_body(e.target.files[0])}
          />
        </div>

        <button id='album-form-submit' type='submit' onClick={handleSubmit}>Submit</button>
        {(imageLoading) && <p>Loading...</p>}
      </form>
    </div>
  )
}

export default SongForm