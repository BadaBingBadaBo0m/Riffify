import React from "react";
import "rc-slider/assets/index.css";
import Slider from "rc-slider";
const style = { width: 400, margin: 50 };
const marks = {
  "-10": "-10°C",
  0: <strong>0°C</strong>,
  26: "26°C",
  37: "37°C",
  50: "50°C",
  100: {
    style: {
      color: "red",
    },
    label: <strong>100°C</strong>,
  },
};
function log(value) {
  console.log(value); //eslint-disable-line
}
function SongPlayBar() {
  return (
    <div>
      <div style={style}>
        <p>Range Slider with marks, `step=null`, pushable, draggableTrack</p>
        <Slider
          range
          min={-10}
          marks={marks}
          step={null}
          onChange={log}
          defaultValue={[-10, 0]}
          allowCross={false}
          pushable
        />
      </div>
    </div>
  );
}
export default SongPlayBar;