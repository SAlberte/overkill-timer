import React, {useState} from "react";
import Dropdown from 'react-bootstrap/Dropdown';
import classes from './TimeSetter.module.css';


export default function TimeSetter() {

    const [hours, setHours] = useState(0)
    const [minutes, setMinutes] = useState(0)
    const [seconds, setSeconds] = useState(0)
    const allHours = Array.from(Array(100).keys())
    const allMinutes = Array.from(Array(60).keys())
    const allSeconds = Array.from(Array(60).keys())

    async function buttonClicked()
    {
        await fetch("http://localhost:8000/timer/time", {
            method: "POST", body: JSON.stringify({
            hours: hours,
            minutes: minutes,
            seconds: seconds
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

    function handleHours(event: React.ChangeEvent<HTMLSelectElement>) {
        event.preventDefault();
        setHours(Number(event.target.value));
    }

    function handleMinutes(event: React.ChangeEvent<HTMLSelectElement>) {
        event.preventDefault();
        setMinutes(Number(event.target.value));
    }

    function handleSeconds(event: React.ChangeEvent<HTMLSelectElement>) {
        event.preventDefault();
        setSeconds(Number(event.target.value));
    }

    return(
        <div>
        <div className={classes.TimeSetter}>
            <div className={classes.Setter}>
                <div className={classes.SelectorLabel}/>
                    hours
                    <select onChange={handleHours} className={classes.Selector}>
                        {allHours.map((val) => <option value={val}>{val}</option>)}
                    </select>
            </div>
            <div className={classes.Setter}>
                <div className={classes.SelectorLabel}/>
                minutes
                     <select onChange={handleMinutes} className={classes.Selector}>
                        {allMinutes.map((val) => <option value={val}>{val}</option>)}
                    </select>
            </div>
            <div className={classes.Setter}>
                    <div className={classes.SelectorLabel}/>
                    seconds
                    <select onChange={handleSeconds} className={classes.Selector} >
                        {allSeconds.map((val) => <option value={val}>{val}</option>)}
                    </select>
            </div>
        </div>
        <button className={classes.SetterButton}
            onClick={buttonClicked}>
                SET
        </button>
    </div>
    );
}