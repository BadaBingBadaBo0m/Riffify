import React, { useState } from 'react'

export const SongContext = React.createContext();

const SongProvider = props => {
  const [currentSong, setCurrentSong] = useState(null);
  const [contextSongList, setContextSongList] = useState(null);
  const [contextAlbum, setContextAlbum] = useState(null);

  const contextValue = {
    currentSong,
    setCurrentSong,
    contextSongList,
    setContextSongList,
    contextAlbum,
    setContextAlbum
  }

  return (
    <>
      <SongContext.Provider value={contextValue}>
        {props.children}
      </SongContext.Provider>
    </>
  )
}

export default SongProvider