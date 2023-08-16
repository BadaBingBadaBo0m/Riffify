const SET_USER_PLAYLISTS = '/playlists/current'
const SET_PLAYLIST_SONGS = '/playlists/songs'
const SET_SINGLE_PLAYLIST = '/playlists/singlePlaylist'
const CREATE_PLAYLIST = '/playlists/new'
const DELETE_PLAYLIST = '/playlists/delete'
const UPDATE_PLAYLIST = '/playlist/update'

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

const setNewPlaylist = (playlist) => ({
  type: CREATE_PLAYLIST,
  playlist
})

const actionDeletePlaylist = () => ({
  type: DELETE_PLAYLIST
})

const actionUpdatePlaylist = (playlist) => ({
  type: UPDATE_PLAYLIST,
  playlist
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

export const createPlaylist = (count) => async (dispatch) => {
  const response = await fetch(`/api/playlists/new/${count}`, {
    method: 'POST'
  })

  if (response.ok) {
    const { playlist } = await response.json()
    dispatch(setNewPlaylist(playlist))
    return playlist
  } else {
    return response
  }
}

export const deletePlaylist = (id) => async (dispatch) => {
  const response = await fetch(`/api/playlists/${id}`, {
    method: 'DELETE'
  })
}

export const updatePlaylist = (id, playlist) => async (dispatch) => {
  const response = await fetch(`/api/playlists/${id}`, {
    method: 'PUT',
    body: playlist
  })

  if (response.ok) {
    const playlist = await response.json()
    dispatch(actionUpdatePlaylist(playlist))
    return playlist
  } else {
    return await response.json()
  }
}

export const addSongToPlaylist = (playlistId, songId) => async (dispatch) => {
  const response = await fetch(`/api/playlists/${playlistId}/song/${songId}`, {
    method: 'POST'
  })

  if (response.ok) {
    const { songs } = await response.json()
    dispatch(setPlaylistSongs(songs))
    return response
  } else {
    return response
  }
}

export const removeSongFromPlaylist = (playlistId, songId) => async (dispatch) => {
  const response = await fetch(`/api/playlists/${playlistId}/song/${songId}`, {
    method: 'DELETE'
  })

  return response
}

export const getLikedSongs = () => async (dispatch) => {
  const response = await fetch(`/api/playlists/likedSongs`)

  if (response.ok) {
    const { songs } = await response.json()
    dispatch(setPlaylistSongs(songs))
    return response
  } else {
    return response
  }
}

export const addSongToLikedSongs = (songId) => async (dispatch) => {
  const response = await fetch(`/api/playlists/likedSongs/${songId}`, {
    method: 'POST'
  })

  return response
}

export const removeSongFromLikedSongs = (songId) => async (dispatch) => {
  const response = await fetch(`/api/playlists/likedSongs/${songId}`, {
    method: 'DELETE'
  })

  return response
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
    case CREATE_PLAYLIST:
      return { ...state, usersPlaylists: [...state.usersPlaylists, action.playlist] }
    case DELETE_PLAYLIST:
      return { ...state, singlePlaylist: null }
    case UPDATE_PLAYLIST:
      return { ...state, singlePlaylist: action.playlist }
    default:
      return state
  }
}