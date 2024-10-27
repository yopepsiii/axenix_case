import Calendar from "react-calendar"
// import 'react-calendar/dist/Calendar.css';
import './CalendarBlock.css'
import './Calendar.css'
import {Provider} from "mobx-react";

let month = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'];

let data;

export default function CalendarBlock({setDate}){
    
    const handlerClick = (e, day) =>{
        let m = String(e).split(' ');
        let data = m[2] + '.' + (month.indexOf(m[1]) + 1) + '.' + m[3];
        console.log(m, data);
        setDate(data)
    }
    return(
        <div className="calendar">
            <h3>Календарь</h3>
            <Calendar onClickDay={handlerClick}/>
        </div>
    )
}