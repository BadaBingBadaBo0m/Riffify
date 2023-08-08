const ADD_ALBUM = 'albums/post'

const addPost = (post) => ({
    type: ADD_ALBUM,
    post
})

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

const initialState = { albums: null }

export default function albumReducer(state = initialState, action) {
    switch (action.type) {
        case ADD_ALBUM:
            return { ...state, albums: action.post }
        default:
            return state
    }
}