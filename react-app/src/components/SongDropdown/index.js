import React, { useRef, useState, useEffect } from 'react'
import { useSelector, useDispatch } from "react-redux";
import OpenModalButton from '../OpenModalButton'
import ConfirmModal from '../ConfirmModal';
import { useModal } from '../../context/Modal';
import './songdropdown.css'
import { useHistory } from 'react-router-dom';
import { deleteSong, getSongsForAlbum } from '../../store/albums';
import SongForm from '../SongForm';

const SongDropdown = ({ song, album }) => {
  const user = useSelector((state) => state.session.user);
  const playlists = useSelector((state) => state.playlists.usersPlaylists)
  const { closeModal } = useModal()
  const dispatch = useDispatch();
  const [showMenu, setShowMenu] = useState(false);
  const [showPlaylistMenu, setShowPlaylistMenu] = useState(false);
  const songDropdownRef = useRef();

  useEffect(() => {
    if (!showMenu) return;

    const closeMenu = (e) => {
      if (songDropdownRef.current && !songDropdownRef.current.contains(e.target)) {
        setShowPlaylistMenu(false)
        setShowMenu(false);
      }
    };

    document.addEventListener("click", closeMenu); //close menu on click anywhere on document exept menu or button

    return () => document.removeEventListener("click", closeMenu);
  }, [showMenu, song]);

  const ToggleMenu = () => {
    if (!showMenu) setShowMenu(true);
    else setShowMenu(false)
  }

  const handleSongDelete = async (id) => {
    const confirm = await dispatch(deleteSong(song.id))

    if (confirm.ok) {
      await dispatch(getSongsForAlbum(album.id))
      closeModal()
    }
  }

  const classShowMenu = showMenu ? "song-dropdown-container" : "song-dropdown-container hidden"
  const showPlaylistDropdown = showPlaylistMenu ? 'song-add-to-playlist-list-dropdown' : 'song-add-to-playlist-list-dropdown hidden'

  return (
    <>
      <div ref={songDropdownRef} id='song-dropdown-ref-div'>
        {user &&
          <i className="fa-solid fa-ellipsis" id='song-dropdown-button' onClick={ToggleMenu}></i>}

        <div className={classShowMenu}>
          <ul className='song-dropdown'>

            <li className='song-dropdown-li'>
              {user && user.id === song.created_by && <div className='song-dropdown-button'>
                <OpenModalButton
                  buttonText={'Delete song'}
                  modalComponent={
                    <ConfirmModal
                      modalTitle={`Are you sure you want to delete ${song.name}`}
                      yesHandler={handleSongDelete}
                    />}
                />
              </div>}
            </li>

            <li className='song-dropdown-li'>
              {user && user.id === song.created_by && <div className='song-dropdown-button'>
                <OpenModalButton
                  buttonText={'Edit song'}
                  modalComponent={
                    <SongForm type={'edit'} albumId={album.id} song={song} />}
                />
              </div>}
            </li>

            <li className='song-dropdown-li'>
              {user && playlists.length > 0 && <div className='song-dropdown-button'>
                <button onClick={() => setShowPlaylistMenu(!showPlaylistMenu)}>Add to playlist</button>
              </div>}
            </li>

          </ul>

          <ul className={showPlaylistDropdown}>
            <h2 className='playlists-list-dropdown-header'>Playlists</h2>
            {playlists.map(playlist => (
              <li>
                <button className='song-playlist-dropdown-button'>{playlist.name}</button>
              </li>
            ))}
          </ul>
        </div>
      </div>
    </>
  )
}

export default SongDropdown;