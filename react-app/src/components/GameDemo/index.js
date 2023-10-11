import React from "react";
import { Unity, useUnityContext } from "react-unity-webgl";

function Demo() {
  const { unityProvider } = useUnityContext({
    loaderUrl: "Build/RhythmDemo.loader.js",
    dataUrl: "Build/RhythmDemo.data",
    frameworkUrl: "Build/RhythmDemo.framework.js",
    codeUrl: "Build/RhythmDemo.wasm",
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

