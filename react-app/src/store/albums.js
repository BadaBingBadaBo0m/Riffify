const ADD_ALBUM = 'albums/post'
const SET_ALBUMS = '/albums/all'
const SET_SINGLE_ALBUM = '/album'
const SET_ALBUM_SONGS = 'album/songs'

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

const addPost = (post) => ({
  type: ADD_ALBUM,
  post
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

export const createImage = (post) => async (dispatch) => {
  const response = await fetch(`/api/album/new`, {
    method: "POST",
    //   headers: {
    //     'Accept': 'application/json',
    //     "Content-Type": "application/json",
    //   },
    body: post
  });

  if (response.ok) {
    const { resPost } = await response.json();
    dispatch(addPost(resPost));
  } else {
    console.log("There was an error making your post!")
  }
};

const initialState = { albumList: null, singleAlbum: null }

export default function albums(state = initialState, action) {
  switch (action.type) {
    case SET_ALBUMS:
      return { ...state, albumList: action.albums }
    case SET_SINGLE_ALBUM:
      return { ...state, singleAlbum: action.album }
    case SET_ALBUM_SONGS:
      return { ...state, albumSongs: action.songs }
    // case ADD_ALBUM:
    //   return { ...state, albums: action.post }
    default:
      return state
  }
}