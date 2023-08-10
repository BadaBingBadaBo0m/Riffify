import React, { useState } from 'react'

export const SongContext = React.createContext();

const SongProvider = props => {
  const [currentSong, setCurrentSong] = useState(null);
  const [contextSongList, setContextSongList] = useState(null);

  const contextValue = {
    currentSong,
    setCurrentSong,
    contextSongList,
    setContextSongList
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