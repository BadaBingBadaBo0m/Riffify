import React, { useState, useRef, useContext, useEffect } from 'react'
import { SongContext } from '../../context/Song';
import './mediaplayer.css'

const MediaPlayer = () => {
  const [play, setPlay] = useState(false);
  const [currentTime, setCurrentTime] = useState(0)
  const [duration, setDuration] = useState(0)
  const [volume, setVolume] = useState(1)
  const { currentSong, setCurrentSong } = useContext(SongContext)
  const audioRef = useRef()

  useEffect(() => {
    audioRef.current.play()
    setPlay(true)
  }, [currentSong])

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

  return (
    <div id='media-player-container'>
      <div className='errors'>{currentSong?.name}</div>
      <audio
        ref={audioRef}
        src={currentSong?.song_body}
        onTimeUpdate={handleTimeUpdate}
      />
      <button onClick={play ? handlePause : handlePlay}>{play ? 'Pause' : "Play"}</button>
      <input
        type='range'
        min={0}
        max={1}
        step={0.01}
        value={volume}
        onChange={handleVolume}
      />
      <input
        type='range'
        min={0}
        max={duration}
        step={1}
        value={currentTime}
        onChange={handleCurrentTime}
      />
    </div >
  )
}

export default MediaPlayer