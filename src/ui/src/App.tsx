import React from 'react';
import classes from './App.module.css';
import TimerButton from "./components/TimerButton/TimerButton";

function App() {
  return (
    <div className={classes.App}>
      <TimerButton/>
    </div>)
}

export default App;
