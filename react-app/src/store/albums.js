const CREATE_ALBUM = 'albums/post'
const SET_ALBUMS = '/albums/all'
const SET_SINGLE_ALBUM = '/album'
const SET_ALBUM_SONGS = 'album/songs'
const DELETE_ALBUM = 'albums/delete'

const setAlbums = (albums) => ({
  type: SET_ALBUMS,
  albums
})

const setSingleAlbum = (album) => ({
  type: SET_SINGLE_ALBUM,
  album
})

const setAlbumSongs = (songs) => ({
  type: SET_ALBUM_SONGS,
  songs
})

const actionCreateAlbum = (album) => ({
  type: CREATE_ALBUM,
  album
})

const actionDeleteAlbum = (album) => ({
  type: DELETE_ALBUM
})

export const getAllAlbums = () => async (dispatch) => {
  const response = await fetch('/api/albums');

  if (response.ok) {
    const data = await response.json();

    dispatch(setAlbums(data));
    return data;
  }
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

export const getSongsForAlbum = (id) => async (dispatch) => {
  const response = await fetch(`/api/songs/${id}`);

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
    dispatch(actionCreateAlbum(album));
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

const initialState = { albumList: null, singleAlbum: null }

export default function albums(state = initialState, action) {
  switch (action.type) {
    case SET_ALBUMS:
      return { ...state, albumList: action.albums }
    case SET_SINGLE_ALBUM:
      return { ...state, singleAlbum: action.album }
    case SET_ALBUM_SONGS:
      return { ...state, albumSongs: action.songs }
    case CREATE_ALBUM:
      return { ...state, singleAlbum: action.album }
    case DELETE_ALBUM:
      return { ...state, singleAlbum: null }
    default:
      return state
  }
}