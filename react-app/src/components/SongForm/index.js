import React, { useState } from 'react'
import './songform.css'

const SongForm = () => {
  const [errors, setErrors] = useState({})

  return (
    <div id='create-song-container'>
      <form id='create-song-from'>
        <h1>Create a new song</h1>

        <div className='album-form-input-container'>
          <label htmlFor='name'>Name {errors.name && <span className='errors'>{errors.name}</span>}</label>
          <input
            className='album-form-input'
            type='text'
          />
        </div>

        <div className='album-form-input-container'>
          <label htmlFor='name'>Song mp3 {errors.art && <span className='errors'>{errors.art}</span>}</label>
          <input
            className='album-form-file'
            type='file'
            accept="audio/mp3"
          // required={type === 'create'}
          />
        </div>
      </form>
    </div>
  )
}

export default SongForm