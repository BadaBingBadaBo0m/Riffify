import React, { useRef, useState, useEffect } from 'react'
import { useSelector, useDispatch } from "react-redux";
import OpenModalButton from '../OpenModalButton'
import ConfirmModal from '../ConfirmModal';
import SongForm from '../SongForm';
import { deleteAlbum, getUsersAlbums } from '../../store/albums';
import { useHistory } from 'react-router-dom';
import PlaylistForm from '../PlaylistForm';
import './playlistDropdown.css'
import { deletePlaylist, getUsersPlaylists } from '../../store/playlists';

const PlaylistDropdown = ({ playlist }) => {
  const user = useSelector((state) => state.session.user);
  // const album = useSelector((state) => state.albums.singleAlbum)
  const dispatch = useDispatch();
  const history = useHistory()
  const [showMenu, setShowMenu] = useState(false);
  const albumDropdownRef = useRef();

  useEffect(() => {
    if (!showMenu) return;

    const closeMenu = (e) => {
      if (albumDropdownRef.current && !albumDropdownRef.current.contains(e.target))
        setShowMenu(false);
    };

    document.addEventListener("click", closeMenu); //close menu on click anywhere on document exept menu or button

    return () => document.removeEventListener("click", closeMenu);
  }, [showMenu, playlist]);

  const ToggleMenu = () => {
    if (!showMenu) setShowMenu(true);
    else setShowMenu(false)
  }

  const handleDelete = async () => {
    const res = await dispatch(deletePlaylist(playlist.id))
    dispatch(getUsersPlaylists())
    history.push('/')
  }

  const classShowMenu = showMenu ? "album-dropdown-container" : "album-dropdown-container hidden"

  const ownedAlbum =
    user && user.id === playlist.owner_id
      ? "album-dropdown"
      : "hidden";
  const notOwnedAlbum =
    user && user.id !== playlist.owner_id
      ? "album-dropdown"
      : "hidden";

  return (
    <>
      <div ref={albumDropdownRef} id='album-dropdown-ref-div'>
        {user &&
          <i class="fa-solid fa-ellipsis" id='album-dropdown-button' onClick={ToggleMenu}></i>}

        <div className={classShowMenu}>
          <ul className={ownedAlbum}>
            <li className='album-dropdown-li'>
              <div className='album-dropdown-button'>
                <OpenModalButton buttonText={'Edit'} modalComponent={<PlaylistForm playlist={playlist} />} />
              </div>
            </li>
            <li className='album-dropdown-li'>
              <div className='album-dropdown-button'>
                <OpenModalButton
                  buttonText={'Delete'}
                  modalComponent={
                    <ConfirmModal
                      modalTitle={`Are you sure you want to delete ${playlist.name}?`}
                      yesHandler={handleDelete}
                    />
                  }
                />
              </div>
            </li>
          </ul>
        </div>

        <div className={classShowMenu}>
          <ul className={notOwnedAlbum}>
            <li>Bruh not owned</li>
          </ul>
        </div>
      </div>
    </>
  )
}

export default PlaylistDropdown;