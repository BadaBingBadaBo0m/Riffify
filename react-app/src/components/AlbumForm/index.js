import React, { useState } from 'react'
import './albumform.css'

const AlbumForm = () => {
  const [name, setName] = useState(null);
  const [description, setDescription] = useState(null);
  const [image, setImage] = useState(null);
  const [artists, setArtists] = useState(null);

  const handleSubmit = (e) => {
    e.preventdefault()
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
          />
        </div>

        <div className='album-form-input-container'>
          <label htmlFor='name'>Description</label>
          <textarea
            className='album-form-textarea'
            type='text'
            required
            value={description}
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

        <button id='album-form-submit' onSubmit={handleSubmit}>Submit</button>

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