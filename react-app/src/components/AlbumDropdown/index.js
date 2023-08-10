import React, { useRef, useState, useEffect } from 'react'
import { useSelector, useDispatch } from "react-redux";
import './albumdropdown.css'

const AlbumDropdown = ({ album }) => {
  const user = useSelector((state) => state.session.user);
  const [showMenu, setShowMenu] = useState(false);
  const albumDropdownRef = useRef()

  useEffect(() => {
    if (!showMenu) return;

    const closeMenu = (e) => {
      if (albumDropdownRef.current && !albumDropdownRef.current.contains(e.target))
        setShowMenu(false);
    };

    document.addEventListener("click", closeMenu); //close menu on click anywhere on document exept menu or button

    return () => document.removeEventListener("click", closeMenu);
  }, [showMenu]);

  const ToggleMenu = () => {
    if (!showMenu) setShowMenu(true);
    else setShowMenu(false)
  }

  const classShowMenu = showMenu ? "album-dropdown-container" : "album-dropdown-container hidden"

  const ownedAlbum =
    user && user.id === album.created_by_id
      ? "ul-channel"
      : "hidden";
  const notOwnedAlbum =
    user && user.id !== album.created_by_id
      ? "ul-channel"
      : "hidden";

  return (
    <>
      {user &&
        <i class="fa-solid fa-ellipsis" id='album-dropdown-button' onClick={ToggleMenu}></i>}

      <div ref={albumDropdownRef}>
        <div className={classShowMenu}>
          <ul className={ownedAlbum}>
            <li>Bruh</li>
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

export default AlbumDropdown;