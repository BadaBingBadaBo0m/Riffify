import React, { useState } from 'react'
import { useDispatch, useSelector } from "react-redux";
import { useHistory } from 'react-router-dom'
import { createAlbum } from "../../store/albums";
import './albumform.css'

const AlbumForm = () => {
  const user = useSelector((state) => state.session.user)
  const history = useHistory()
  const dispatch = useDispatch()
  const [name, setName] = useState(null);
  const [description, setDescription] = useState(null);
  const [image, setImage] = useState(null);
  // const [artists, setArtists] = useState(null);
  const [imageLoading, setImageLoading] = useState(false);

  if (!user) history.push('/')

  const handleSubmit = async (e) => {
    e.preventDefault();
    const formData = new FormData();
    formData.append('art', image);
    formData.append('name', name);
    formData.append('description', description);

    setImageLoading(true)
    console.log(formData)
    const album = await dispatch(createAlbum(formData))
    history.push('/')
  }

  return (
    <div id='album-form-container'>
      <form id='album-form'>
        <h1 id='album-form-header'>Create a new album</h1>

        <div className='album-form-input-container'>
          <label htmlFor='name'>Name</label>
          <input
            className='album-form-input'
            type='text'
            required
            value={name}
            onChange={(e) => setName(e.target.value)}
          />
        </div>

        <div className='album-form-input-container'>
          <label htmlFor='name'>Description</label>
          <textarea
            className='album-form-textarea'
            type='text'
            required
            value={description}
            onChange={(e) => setDescription(e.target.value)}
          />
        </div>

        <div className='album-form-input-container'>
          <label htmlFor='name'>Album art</label>
          <input
            className='album-form-file'
            type='file'
            accept="image/*"
            onChange={(e) => setImage(e.target.files[0])}
          />
        </div>

        <button id='album-form-submit' type='submit' onClick={handleSubmit}>Submit</button>
        {(imageLoading) && <p>Loading...</p>}

        {/* <div className='album-form-input-container'>
          <label htmlFor='name'>Featured artists</label>
          <input
            className='album-form-input'
            type='text'
            value={artists}
          />
        </div> */}

      </form>
    </div >
  )
}

export default AlbumForm