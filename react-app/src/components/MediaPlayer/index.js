import React, { useState, useRef, useContext, useEffect } from 'react'
import { SongContext } from '../../context/Song';
import './mediaplayer.css'

const MediaPlayer = () => {
  const [play, setPlay] = useState(false);
  const [currentTime, setCurrentTime] = useState(0)
  const [duration, setDuration] = useState(0)
  const [volume, setVolume] = useState(1)
  const { currentSong, setCurrentSong, contextAlbum } = useContext(SongContext)
  const audioRef = useRef()

  // useEffect(() => {
  //   audioRef.current.play()
  //   setPlay(true)
  // }, [currentSong])

  const handlePlay = () => {
    audioRef.current.play()
    setPlay(true)
  }

  const handlePause = () => {
    audioRef.current.pause()
    setPlay(false)
  }

  const handleVolume = (e) => {
    setVolume(e.target.value)
    audioRef.current.volume = e.target.value
  }

  const handleTimeUpdate = () => {
    setCurrentTime(audioRef.current.currentTime)
    setDuration(audioRef.current.duration)
  }

  const handleCurrentTime = (e) => {
    setCurrentTime(e.target.value)
    audioRef.current.currentTime = e.target.value
  }
  console.log(contextAlbum)
  return (
    <div id={currentSong ? 'media-player-container' : 'hidden'}>
      <audio
        ref={audioRef}
        src={currentSong?.song_body}
        onTimeUpdate={handleTimeUpdate}
      />

      <div id='media-player-song-info-container'>
        <img id='media-player-album-art' src={contextAlbum?.art}></img>
        <div id='media-player-song-info'>
          <h2 id='media-player-song-name'>{currentSong?.name}</h2>
          <p id='media-player-artist-name'>{contextAlbum?.created_by.username}</p>
        </div>
      </div>

      <div id='media-player-controls-container'>
        <div id='media-player-controls'>
          <button id='step-back-button'> <i class="fa-solid fa-backward-step"></i> </button>
          {!audioRef.current?.paused && <button className='media-player-play-button' onClick={handlePause}> <i class="fa-solid fa-circle-pause"></i> </button>}
          {audioRef.current?.paused && <button className='media-player-play-button' onClick={handlePlay}> <i class="fa-solid fa-circle-play"></i> </button>}
          <button id='step-forward-button'> <i class="fa-solid fa-forward-step"></i> </button>
        </div>

        <input
          type='range'
          id='song-play-bar'
          min={0}
          max={duration}
          step={1}
          value={currentTime}
          onChange={handleCurrentTime}
        />
      </div>

      <input
        type='range'
        id='song-volume-bar'
        min={0}
        max={1}
        step={0.01}
        value={volume}
        onChange={handleVolume}
      />
    </div >
  )
}

export default MediaPlayer