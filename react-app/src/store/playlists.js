const SET_USER_PLAYLISTS = '/playlists/current'

const setUsersPlaylists = (playlists) => ({
  type: SET_USER_PLAYLISTS,
  playlists
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

const initialState = { usersPlaylists: null }

export default function playlists(state = initialState, action) {
  switch (action.type) {
    case SET_USER_PLAYLISTS:
      return { ...state, usersPlaylists: action.playlists }
    default:
      return state
  }
}