import React, { useState, useEffect } from "react";
import { useDispatch } from "react-redux";
import { Route, Switch } from "react-router-dom";
import SignupFormPage from "./components/SignupFormPage";
import LoginFormPage from "./components/LoginFormPage";
import UploadPicture from "./components/AWSForm";
import HomePage from "./components/Homepage";
import Recommended from './components/Recommended'
import AlbumForm from "./components/AlbumForm";
import AlbumInfo from "./components/AlbumInfo";
import { authenticate } from "./store/session";
// import Navigation from "./components/Navigation";

function App() {
  const dispatch = useDispatch();
  const [isLoaded, setIsLoaded] = useState(false);
  useEffect(() => {
    dispatch(authenticate()).then(() => setIsLoaded(true));
  }, [dispatch]);

  return (
    <>
      {isLoaded && (
        <Switch>
          <Route exact path='/' >
            <HomePage Content={Recommended} />
          </Route>
          <Route path='/new-album' >
            <HomePage Content={AlbumForm} />
          </Route>
          <Route path='/albums/:albumId' >
            <HomePage Content={AlbumInfo} />
          </Route>
          {/* <Route path="/login" >
            <LoginFormPage />
          </Route>
          <Route path="/signup">
            <SignupFormPage />
          </Route> */}
          <Route path='/upload'>
            <UploadPicture />
          </Route>
        </Switch>
      )}
    </>
  );
}

export default App;
