import React, { useState } from 'react'
import './playlistForm.css'
import { useDispatch, useSelector } from 'react-redux'
import { getUsersPlaylists, updatePlaylist } from '../../store/playlists'
import { useModal } from '../../context/Modal'

const PlaylistForm = ({ playlist }) => {
  const [imageLoading, setImageLoading] = useState(false)
  const [name, setName] = useState(null || playlist.name)
  const [image, setImage] = useState(null)
  const [errors, setErrors] = useState({})
  const { closeModal } = useModal()
  const dispatch = useDispatch()
  const user = useSelector((state) => state.session.user)

  const validateData = () => {
    const errorObj = {};

    if (!name) errorObj.name = 'is required.'
    if (name && name.length > 50) errorObj.name = 'length cannot be greater than 50.'

    setErrors(errorObj)
    if (Object.keys(errorObj).length) return false
    else return true
  }

  const handleSubmit = async (e) => {
    e.preventDefault()

    const isValid = validateData()

    if (isValid) {
      const formData = new FormData()
      formData.append('name', name)
      if (image) {
        formData.append('picture', image)
      }
      setImageLoading(true)
      const updated_playlist = await dispatch(updatePlaylist(playlist.id, formData))
      if (updated_playlist.errors) {
        setErrors(updated_playlist.errors)
        setImageLoading(false)
      } else {
        await dispatch(getUsersPlaylists())
        closeModal()
      }
    }
  }

  return (
    <div id='playlist-form-container'>
      <form id='playlist-form'>
        <h1 id='playlist-form-header'>{`Edit ${playlist.name}`}</h1>

        <div className='album-form-input-container'>
          <label>Name {errors.name && <span className='errors'>{errors.name}</span>}</label>
          <input
            className='album-form-input'
            type='text'
            required
            value={name}
            onChange={(e) => setName(e.target.value)}
          />
        </div>

        <div className='album-form-input-container'>
          <label htmlFor='name'>Playlist Picture {errors.picture && <span className='errors'>{errors.picture}</span>}</label>
          <input
            className='album-form-file'
            type='file'
            accept="image/*"
            onChange={(e) => setImage(e.target.files[0])}
          />
        </div>

        <button id='album-form-submit' type='submit' onClick={handleSubmit}>Submit</button>
        {(imageLoading) && <p>Loading...</p>}

      </form>
    </div>
  )
}

export default PlaylistForm