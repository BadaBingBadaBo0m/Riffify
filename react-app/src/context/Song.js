import React, { useState } from 'react'

export const SongContext = React.createContext();

const SongProvider = props => {
  const [currentSong, setCurrentSong] = useState(null);
  const [contextSongList, setContextSongList] = useState([]);
  const [contextAlbum, setContextAlbum] = useState(null);
  const [contextPlaylist, setContextPlaylist] = useState(null);
  const [play, setPlay] = useState(false);

  const contextValue = {
    currentSong,
    setCurrentSong,
    contextSongList,
    setContextSongList,
    contextAlbum,
    setContextAlbum,
    contextPlaylist,
    setContextPlaylist,
    play,
    setPlay
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