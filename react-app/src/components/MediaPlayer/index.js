import React, { useState, useRef, useContext, useEffect } from 'react'
import { SongContext } from '../../context/Song';
import './mediaplayer.css'

const MediaPlayer = () => {
  const [play, setPlay] = useState(false);
  const [currentTime, setCurrentTime] = useState(0)
  const [duration, setDuration] = useState(0)
  const [volume, setVolume] = useState(1)
  const [repeat, setRepeat] = useState(false)
  const [shuffle, setShuffle] = useState(false)
  const [currentSongIndex, setCurrentSongIndex] = useState(null)
  const { currentSong, setCurrentSong, contextAlbum, contextSongList } = useContext(SongContext)
  const audioRef = useRef()

  useEffect(() => {
    setTimeout(() => {
      audioRef.current.play()
      setPlay(true)
    }, 1000);
    setCurrentSongIndex(contextSongList.map((songMap) => songMap.id).indexOf(currentSong?.id))
    // console.log(contextSongList)
    // console.log(currentSongIndex)

    const localAudio = localStorage.getItem('tritone-volume')
    if (localAudio) {
      audioRef.current.volume = localAudio
      setVolume(localAudio)
    }
  }, [currentSong])

  useEffect(() => {
    if (repeat) {
      audioRef.current.loop = true
    } else {
      audioRef.current.loop = false
    }

    if (currentTime === duration && !repeat) {

    }
  }, [repeat, duration])

  const handlePlay = () => {
    audioRef.current.play()
    setPlay(true)
    // console.log(contextSongList.map((songMap) => songMap.id).indexOf(currentSong.id))
    console.log(currentSongIndex)
  }

  const handleBack = () => {
    setCurrentSong(contextSongList[currentSongIndex - 1] || contextSongList[contextSongList.length - 1])
  }

  const handleSkip = () => {
    setCurrentSong(contextSongList[currentSongIndex + 1] || contextSongList[0])
  }

  const handlePause = () => {
    audioRef.current.pause()
    setPlay(false)
  }

  const handleVolume = (e) => {
    setVolume(e.target.value)
    localStorage.setItem('tritone-volume', e.target.value)
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

  const handleRepeat = () => {
    if (!repeat) setRepeat(true)
    else setRepeat(false)
  }

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
          <button className={shuffle ? 'shuffle-button active' : 'shuffle-button'}> <i class="fa-solid fa-shuffle"></i> </button>

          <button id='step-back-button' onClick={handleBack}> <i class="fa-solid fa-backward-step"></i> </button>

          {!audioRef.current?.paused && <button className='media-player-play-button' onClick={handlePause}> <i class="fa-solid fa-circle-pause"></i> </button>}

          {audioRef.current?.paused && <button className='media-player-play-button' onClick={handlePlay}> <i class="fa-solid fa-circle-play"></i> </button>}

          <button id='step-forward-button' onClick={handleSkip}> <i class="fa-solid fa-forward-step"></i> </button>

          <button className={repeat ? 'repeat-button active' : 'repeat-button'} onClick={handleRepeat}> <i class="fa-solid fa-repeat"></i> </button>
        </div>

        <div id='volume-controls-container'>
          <input
            type='range'
            id='song-play-bar'
            min={0}
            max={duration || ''}
            step={1}
            value={currentTime}
            onChange={handleCurrentTime}
          />
        </div>
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