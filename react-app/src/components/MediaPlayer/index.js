import React, { useState, useRef } from 'react'

const MediaPlayer = () => {
  const [play, setPlay] = useState(false);
  const [currentTime, setCurrentTime] = useState(0)
  const [duration, setDuration] = useState(0)
  const [volume, setVolume] = useState(1)
  const audioRef = useRef()

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
    <div>
      <h1 id='media-test'>MediaPlayer</h1>
      <audio
        ref={audioRef}
        src='https://tritone-spotify-clone.s3.amazonaws.com/Currents+Better+days.mp3'
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
    </div>
  )
}

export default MediaPlayer