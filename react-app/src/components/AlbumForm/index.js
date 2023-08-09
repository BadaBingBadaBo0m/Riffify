import React, { useState } from 'react'
import './albumform.css'

const AlbumForm = () => {
  const [name, setName] = useState(null)

  return (
    <div id='album-form-container'>
      <form id='album-form'>
        <h1>Create a new album</h1>

        <div id='album-form-input-container'>
          <label htmlFor='name'>Name</label>
          <input
            id='album-form-input'
            type='text'
            required
            value={name}
          />

        </div>

      </form>
    </div >
  )
}

export default AlbumForm