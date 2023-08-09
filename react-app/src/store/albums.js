const ADD_ALBUM = 'albums/post'
const SET_ALBUMS = '/albums/all'

const setAlbums = (albums) => ({
  type: SET_ALBUMS,
  albums
})

const addPost = (post) => ({
  type: ADD_ALBUM,
  post
})

export const getAllAlbums = () => async (dispatch) => {
  const response = await fetch('/api/albums')

  if (response.ok) {
    const data = await response.json();

    dispatch(setAlbums(data))
    return data
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

const initialState = { albumList: null }

export default function albums(state = initialState, action) {
  switch (action.type) {
    case SET_ALBUMS:
      return { ...state, albumList: action.albums }
    // case ADD_ALBUM:
    //   return { ...state, albums: action.post }
    default:
      return state
  }
}