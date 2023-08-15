import React, { useRef, useState, useEffect } from 'react'
import { useSelector, useDispatch } from "react-redux";
import OpenModalButton from '../OpenModalButton'
import ConfirmModal from '../ConfirmModal';
import { useModal } from '../../context/Modal';
import { getPlaylistSongs, removeSongFromPlaylist } from '../../store/playlists';

const PlaylistSongDropdown = ({ playlist, song }) => {
  const user = useSelector((state) => state.session.user);
  const playlists = useSelector((state) => state.playlists.usersPlaylists)
  const { closeModal } = useModal()
  const dispatch = useDispatch();
  const [showMenu, setShowMenu] = useState(false);
  const [showPlaylistMenu, setShowPlaylistMenu] = useState(false);
  const [playlistConfirmTooltip, setPlaylistConfirmTooltip] = useState(false)
  const [playlistMessage, setPlaylistMessage] = useState(null)
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

  const handleRemoveSong = async (playlistId, songId) => {
    await dispatch(removeSongFromPlaylist(playlistId, songId))
    await dispatch(getPlaylistSongs(playlistId))
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
                  buttonText={'Remove song'}
                  modalComponent={
                    <ConfirmModal
                      modalTitle={`Are you sure you want to remove ${song.name}`}
                      yesHandler={() => handleRemoveSong(playlist.id, song.id)}
                    />}
                />
              </div>}
            </li>

          </ul>
        </div>
      </div>
    </>
  )
}

export default PlaylistSongDropdown