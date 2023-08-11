import React, { useState } from 'react'
import './songform.css'
import { useDispatch } from 'react-redux';
import { createSongForAlbum } from '../../store/albums';
import { useModal } from '../../context/Modal';

const SongForm = ({ type, albumId }) => {
  const [errors, setErrors] = useState({});
  const [song_body, setSong_body] = useState(null);
  const [name, setName] = useState(null);
  const [imageLoading, setImageLoading] = useState(false);
  const dispatch = useDispatch()
  const { closeModal } = useModal()

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

  const handleSubmit = (e) => {
    e.preventDefault()

    const isValid = validateData()

    if (isValid && type == 'create') {
      const formData = new FormData();
      formData.append('name', name)
      formData.append('song_body', song_body)
      setImageLoading(true)
      const new_song = dispatch(createSongForAlbum(albumId, formData))
      console.log('newsong', new_song)
      if (new_song.ok) {
        closeModal()
      }
    }
  }

  return (
    <div id='create-song-container'>
      <form id='create-song-from'>
        <h1 id='Song-form-title'>Create a new song</h1>

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