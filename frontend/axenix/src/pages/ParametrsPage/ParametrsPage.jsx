import { useState } from "react";
import CalendarBlock from "../../components/calendarBlock/CalendarBlock";
import Parametrs from "../../components/parametrs/Parametrs";

import './ParametrsPage.css'

export default function ParametrsPage() {
    const [date, setDate] = useState('')
    return (
        <div className="container">
            <CalendarBlock setDate={setDate}/>
            <Parametrs date={date}/>
        </div>
    )
}