import React, { useState } from 'react'
import { useDispatch, useSelector } from "react-redux";
import { useHistory } from 'react-router-dom'
import { createAlbum, getUsersAlbums, updateAlbum } from "../../store/albums";
import { useModal } from '../../context/Modal';
import './albumform.css'

const AlbumForm = ({ type, album }) => {
  const user = useSelector((state) => state.session.user);
  const history = useHistory();
  const dispatch = useDispatch();
  const { closeModal } = useModal()
  const [name, setName] = useState(album ? album.name : null);
  const [description, setDescription] = useState(album ? album.description : null);
  const [image, setImage] = useState(null);
  const [errors, setErrors] = useState({});
  // const [artists, setArtists] = useState(null);
  const [imageLoading, setImageLoading] = useState(false);

  const validateData = () => {
    const errorObj = {};

    if (!name) errorObj.name = 'is required.'
    if (name && name.length > 50) errorObj.name = 'Cannot be greater than 50 characters.'

    // if (!description) errorObj.description = 'is required.'
    // if (description && description.length > 1000) errorObj.description = 'length cannot be greater than 1000'

    if (type == 'create') {
      if (!image) errorObj.art = 'is required.'
    }

    setErrors(errorObj)
    if (Object.keys(errorObj).length) return false
    else return true
  }

  const handleSubmit = async (e) => {
    e.preventDefault();

    const isValid = validateData()

    if (isValid && type == 'create') {
      const formData = new FormData();
      formData.append('art', image);
      formData.append('name', name);
      formData.append('description', description);
      setImageLoading(true)
      const new_album = await dispatch(createAlbum(formData))
      if (new_album.errors) {
        setErrors(new_album.errors)
        setImageLoading(false)
      } else {
        closeModal()
        history.push(`/albums/${new_album.id}`)
      }
    }

    if (isValid && type == 'update') {
      const formData = new FormData();
      formData.append('name', name);
      formData.append('description', description);
      if (image) formData.append('art', image)
      setImageLoading(true)
      const updated_album = await dispatch(updateAlbum(album.id, formData))
      if (updated_album.errors) {
        setErrors(updated_album.errors)
        setImageLoading(false)
      } else {
        await dispatch(getUsersAlbums())
        closeModal()
      }
    }
  }

  return (
    <div id='album-form-container'>
      <form id='album-form' encType='multipart/form-data'>
        <h1 id='album-form-header'>{type === 'create' ? 'Create a new album' : `Update ${album.name}`}</h1>

        <div className='album-form-input-container'>
          <label className='album-form-label' htmlFor='name'>Name {errors.name && <span className='errors'>{errors.name}</span>}</label>
          <input
            className='album-form-input'
            type='text'
            required
            value={name}
            onChange={(e) => setName(e.target.value)}
          />
        </div>

        <div className='album-form-input-container'>
          <label htmlFor='name'>Album art {errors.art && <span className='errors'>{errors.art}</span>}</label>
          <input
            className='album-form-file'
            type='file'
            accept="image/*"
            onChange={(e) => setImage(e.target.files[0])}
            required={type === 'create'}
          />
        </div>

        <button id='album-form-submit' type='submit' onClick={handleSubmit}>Submit</button>
        {(imageLoading) && <p>Loading...</p>}

      </form>
    </div >
  )
}

export default AlbumForm
