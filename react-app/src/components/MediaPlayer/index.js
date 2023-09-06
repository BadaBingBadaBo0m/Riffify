import React, { useState, useRef, useContext, useEffect } from 'react'
import Slider from 'rc-slider'
import { SongContext } from '../../context/Song';
import './mediaplayer.css'
import SongPlayBar from './SongPlayBar';

const MediaPlayer = () => {
  // const [play, setPlay] = useState(false);
  const [currentTime, setCurrentTime] = useState(0)
  const [duration, setDuration] = useState(0)
  const [volume, setVolume] = useState(1)
  const [repeat, setRepeat] = useState(false)
  const [shuffle, setShuffle] = useState(false)
  const [currentSongIndex, setCurrentSongIndex] = useState(null)
  const { currentSong, setCurrentSong, contextAlbum, contextSongList, contextPlaylist, play, setPlay } = useContext(SongContext)
  const audioRef = useRef()
  const randomIndex = Math.floor(Math.random() * (contextSongList.length - 0) + 0)

  useEffect(() => {
    setTimeout(() => {
      if (currentSong) {
        audioRef.current.play()
        setPlay(true)
      }
    }, 1000);

    if (!currentSong) {
      audioRef.current.pause()
      setPlay(false)
    }

    setCurrentSongIndex(contextSongList.map((songMap) => songMap.id).indexOf(currentSong?.id))

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
      setCurrentSong(contextSongList[currentSongIndex + 1] || contextSongList[0])
    }

    if (currentTime === duration && shuffle) {
      setCurrentSong(contextSongList[randomIndex])
    }

    const handleExternalPlay = async () => {
      await audioRef.current.play()
    }

    if (play === false) {
      audioRef.current.pause()
    }

    if (play === true) {
      handleExternalPlay()
    }
  }, [repeat, currentTime, play, shuffle])

  const handlePlay = async () => {
    await audioRef.current.play()
    setPlay(true)
  }

  const handlePause = () => {
    audioRef.current.pause()
    setPlay(false)
  }

  const handleBack = () => {
    if (currentTime === duration && shuffle) {
      setCurrentSong(contextSongList[randomIndex])
    } else {
      setCurrentSong(contextSongList[currentSongIndex - 1] || contextSongList[contextSongList.length - 1])
    }
  }

  const handleSkip = () => {
    if (shuffle) {
      setCurrentSong(contextSongList[randomIndex])
    } else {
      setCurrentSong(contextSongList[currentSongIndex + 1] || contextSongList[0])
    }
  }

  const handleVolume = (e) => {
    setVolume(e)
    localStorage.setItem('tritone-volume', e)
    audioRef.current.volume = e
  }

  const handleTimeUpdate = () => {
    setCurrentTime(audioRef.current.currentTime)
    setDuration(audioRef.current.duration)
  }

  const handleCurrentTime = (e) => {
    setCurrentTime(e)
    audioRef.current.currentTime = e
  }

  const handleRepeat = () => {
    if (!repeat) setRepeat(true)
    else setRepeat(false)
  }

  const handleShuffle = () => {
    if (!shuffle) setShuffle(true)
    else setShuffle(false)
  }

  return (
    <div id={currentSong ? 'media-player-container' : 'hidden'}>
      <audio
        ref={audioRef}
        src={currentSong?.song_body}
        onTimeUpdate={handleTimeUpdate}
      />

      <div id='media-player-song-info-container'>
        <img id='media-player-album-art' src={currentSong?.album.art}></img>
        <div id='media-player-song-info'>
          <h2 id='media-player-song-name'>{currentSong?.name}</h2>
          <p id='media-player-artist-name'>{contextAlbum?.created_by.username}</p>
        </div>
      </div>

      <div id='media-player-controls-container'>
        <div id='media-player-controls'>
          <button className={shuffle ? 'shuffle-button active' : 'shuffle-button'} onClick={handleShuffle}> <i class="fa-solid fa-shuffle"></i> </button>

          <button id='step-back-button' onClick={handleBack}> <i class="fa-solid fa-backward-step"></i> </button>

          {!audioRef.current?.paused && <button className='media-player-play-button' onClick={handlePause}> <i class="fa-solid fa-circle-pause"></i> </button>}

          {audioRef.current?.paused && <button className='media-player-play-button' onClick={handlePlay}> <i class="fa-solid fa-circle-play"></i> </button>}

          <button id='step-forward-button' onClick={handleSkip}> <i class="fa-solid fa-forward-step"></i> </button>

          <button className={repeat ? 'repeat-button active' : 'repeat-button'} onClick={handleRepeat}> <i class="fa-solid fa-repeat"></i> </button>
        </div>

        <div id='volume-controls-container'>
          {/* <input
            type='range'
            id='song-play-bar'
            min={0}
            max={duration || ''}
            step={1}
            value={currentTime}
            onChange={handleCurrentTime}
          /> */}
          <Slider
            min={0}
            max={duration || ''}
            step={.1}
            value={currentTime}
            onChange={handleCurrentTime}
            trackStyle={
              { backgroundColor: '#1ed760' }
            }
            railStyle={
              { backgroundColor: '#4d4d4d' }
            }
            handleStyle={[
              {
                backgroundColor: 'white',
                border: 'none',
                opacity: 1
              }
            ]}
          />
        </div>
      </div>

      <div id='song-volume-bar'>
        <Slider
          min={0}
          max={.5}
          step={0.01}
          value={volume}
          onChange={handleVolume}
          trackStyle={
            { backgroundColor: '#1ed760' }
          }
          railStyle={
            { backgroundColor: '#4d4d4d' }
          }
          handleStyle={[
            {
              backgroundColor: 'white',
              border: 'none',
              opacity: 1
            }
          ]}
        />
      </div>
      {/* <input
        type='range'
        id='song-volume-bar'
        min={0}
        max={1}
        step={0.01}
        value={volume}
        onChange={handleVolume}
      /> */}
    </div >
  )
}

export default MediaPlayer