import React, {useState} from "react";

import classes from './TimerButton.module.css'

export default function TimerButton() {

    const [text, setText] = useState("START")

    async function buttonClicked()
    {
        await fetch("http://localhost:8000/timer", {
            method: "POST", body: JSON.stringify({
            command: text,
          }),
          headers: {
            "Content-Type": "application/json"}
        })
        .then(response => response.json())
        .then((response) => {
            setText((text) => text === "START" ? "STOP" : "START")
        })
        .catch((err) => {
          console.log(err)});
    }

    return(
            <button className={classes.TimerButton}
                    onClick={buttonClicked}>
                {text}
            </button>
    );
}