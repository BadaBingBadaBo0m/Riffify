import React from "react";
import { Unity, useUnityContext } from "react-unity-webgl";

function Demo() {
  const { unityProvider } = useUnityContext({
    loaderUrl: "Build/RythmGame.loader.js",
    dataUrl: "Build/RythmGame.data",
    frameworkUrl: "Build/RythmGame.framework.js",
    codeUrl: "Build/RythmGame.wasm",
  });

  return (
    <div>
      <h1>game</h1>
      <Unity
        style={{
          width: "80%",
          // backgroundColor: "red"
        }}
        unityProvider={unityProvider}
      />
    </div>
  )
}

export default Demo

