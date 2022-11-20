import React, {useEffect, useState} from "react";

import classes from './TimerButton.module.css'

export default function TimerButton() {

    const [text, setText] = useState("START")


    useEffect(() => {
        const interval = setInterval(() => {
            fetch("http://localhost:8000/timer/status", {
            method: "GET",
          headers: {
            "Content-Type": "application/json"}
        })
        .then(response => response.json())
        .then((response) => {
            setText(response.status === "STARTED" ? "STOP" : "START");
        })
        .catch((err) => {
          console.log(err)});
        }, 1000);
        return () => clearInterval(interval);
    }, []);

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