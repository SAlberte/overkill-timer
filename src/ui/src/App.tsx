import React from 'react';
import classes from './App.module.css';
import TimerButton from "./components/TimerButton/TimerButton";
import TimeSetter from "./components/TimeSetter/TimeSetter";

function App() {
  return (
    <div className={classes.App}>
      <TimerButton/>
        <TimeSetter/>
    </div>)
}

export default App;
