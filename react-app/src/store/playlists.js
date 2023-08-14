const SET_USER_PLAYLISTS = '/playlists/current'
const SET_PLAYLIST_SONGS = '/playlists/songs'
const SET_SINGLE_PLAYLIST = '/playlists/singlePlaylist'

const setUsersPlaylists = (playlists) => ({
  type: SET_USER_PLAYLISTS,
  playlists
})

const setSinglePlaylist = (playlist) => ({
  type: SET_SINGLE_PLAYLIST,
  playlist
})

const setPlaylistSongs = (songs) => ({
  type: SET_PLAYLIST_SONGS,
  songs
})

export const getUsersPlaylists = () => async (dispatch) => {
  const response = await fetch(`/api/playlists/current`)

  if (response.ok) {
    const { playlists } = await response.json()
    dispatch(setUsersPlaylists(playlists))
    return playlists
  } else {
    return response
  }
}

export const getPlaylist = (playlistId) => async (dispatch) => {
  const response = await fetch(`/api/playlists/${playlistId}`)

  if (response.ok) {
    const { playlist } = await response.json()
    dispatch(setSinglePlaylist(playlist))
    return playlist
  } else {
    return response
  }
}

export const getPlaylistSongs = (playlistId) => async (dispatch) => {
  const response = await fetch(`/api/playlists/${playlistId}/songs`)

  if (response.ok) {
    const { songs } = await response.json()
    dispatch(setPlaylistSongs(songs))
    return songs
  } else {
    return response
  }
}

const initialState = { usersPlaylists: null, playlistSongs: null, singlePlaylist: null }

export default function playlists(state = initialState, action) {
  switch (action.type) {
    case SET_USER_PLAYLISTS:
      return { ...state, usersPlaylists: action.playlists }
    case SET_PLAYLIST_SONGS:
      return { ...state, playlistSongs: action.songs }
    case SET_SINGLE_PLAYLIST:
      return { ...state, singlePlaylist: action.playlist }
    default:
      return state
  }
}