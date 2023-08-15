const CREATE_ALBUM = 'albums/post'
const SET_ALBUMS = '/albums/all'
const SET_SINGLE_ALBUM = '/album'
const SET_ALBUM_SONGS = 'album/songs'
const DELETE_ALBUM = 'albums/delete'
const SET_USERS_ALBUMS = 'albums/current'
const CLEAR_STATE = 'albums/clear'
const CREATE_SONG = 'albums/songs/new'

const setAlbums = (albums) => ({
  type: SET_ALBUMS,
  albums
})

const setSingleAlbum = (album) => ({
  type: SET_SINGLE_ALBUM,
  album
})

const setUsersAlbums = (albums) => ({
  type: SET_USERS_ALBUMS,
  albums
})

export const setAlbumSongs = (songs) => ({
  type: SET_ALBUM_SONGS,
  songs
})

const actionCreateAlbum = (album) => ({
  type: CREATE_ALBUM,
  album
})

export const actionClearAlbumsState = () => ({
  type: CLEAR_STATE
})

// const actionCreateSong = (song) => ({
//   type: CREATE_SONG,
//   song
// })

const actionDeleteAlbum = (album) => ({
  type: DELETE_ALBUM
})

export const getAllAlbums = () => async (dispatch) => {
  const response = await fetch('/api/albums');

  if (response.ok) {
    // const data = await response.json();
    const { albums } = await response.json();

    dispatch(setAlbums(albums));
    return albums;
  }
}

export const getUsersAlbums = () => async (dispatch) => {
  const response = await fetch('/api/albums/current');

  if (response.ok) {
    const { albums } = await response.json()
    dispatch(setUsersAlbums(albums))
    return albums
  }

  return response
}

export const getSingleAlbum = (id) => async (dispatch) => {
  const response = await fetch(`/api/albums/${id}`);

  if (response.ok) {
    const data = await response.json();

    dispatch(setSingleAlbum(data))
  }

  if (response.errors) {
    console.log(response.errors)
  }
}

export const createSongForAlbum = (albumId, song) => async (dispatch) => {
  const response = await fetch(`/api/songs/new/${albumId}`, {
    method: 'POST',
    body: song
  })

  console.log(response)
  if (response.ok) {
    const { song } = response.json()
    // await actionCreateSong(song)
    return response
  } else {
    return response
  }
}

export const getSongsForAlbum = (albumId, userId) => async (dispatch) => {
  let response
  if (userId) {
    response = await fetch(`/api/songs/${albumId}`);
  } else {
    response = await fetch(`/api/songs/loggedOut/${albumId}`);
  }

  if (response.ok) {
    const data = await response.json();

    dispatch(setAlbumSongs(data))
  }
}

export const createAlbum = (album) => async (dispatch) => {
  const response = await fetch(`/api/albums/new`, {
    method: "POST",
    body: album
  });

  if (response.ok) {
    const new_album = await response.json();
    await dispatch(actionCreateAlbum(new_album));
    return new_album
  } else {
    return response
  }
};

export const updateAlbum = (id, album) => async (dispatch) => {
  const response = await fetch(`/api/albums/${id}`, {
    method: 'PUT',
    body: album
  })

  if (response.ok) {
    const album = await response.json();
    dispatch(setSingleAlbum(album))
    return album
  } else {
    return response.json()
  }
}

export const deleteAlbum = (id) => async (dispatch) => {
  const response = await fetch(`/api/albums/${id}`, {
    method: 'DELETE'
  })

  if (response.ok) {
    dispatch(actionDeleteAlbum())
    return { 'message': 'Successfully deleted' }
  } else {
    return response.errors
  }
}

export const deleteSong = (songId) => async (dispatch) => {
  const response = await fetch(`/api/songs/${songId}`, {
    method: 'DELETE'
  })

  if (response.ok) {
    // await actionCreateSong(song)
    return response
  } else {
    return response
  }
}

export const updateSong = (song, songId) => async (dispatch) => {
  const response = await fetch(`/api/songs/${songId}`, {
    method: 'PUT',
    body: song
  })

  if (response.ok) {
    return response
  } else {
    return response
  }
}

const initialState = { albumList: null, singleAlbum: null, usersAlbums: null }

export default function albums(state = initialState, action) {
  switch (action.type) {
    case SET_ALBUMS:
      return { ...state, albumList: action.albums }
    case SET_SINGLE_ALBUM:
      return { ...state, singleAlbum: action.album }
    case SET_ALBUM_SONGS:
      return { ...state, albumSongs: action.songs }
    case CREATE_ALBUM:
      return { ...state, singleAlbum: action.album, usersAlbums: [...state.usersAlbums, action.album] }
    case DELETE_ALBUM:
      return { ...state, singleAlbum: null }
    case SET_USERS_ALBUMS:
      return { ...state, usersAlbums: action.albums }
    case CLEAR_STATE:
      return { ...state, albumList: state.albumList, singleAlbum: null, usersAlbums: null }
    // case CREATE_SONG:
    //   return { ...state, albumSongs: [...state.albumSongs, action.song] }
    default:
      return state
  }
}