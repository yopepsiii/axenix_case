import { useState } from "react";
import CalendarBlock from "../../components/calendarBlock/CalendarBlock";
import Parametrs from "../../components/parametrs/Parametrs";

import './ParametrsPage.css'
import { SearchContextProvider } from "../../contexts/searchContexts/SearchContextProvider";

export default function ParametrsPage() {
    const [date, setDate] = useState('')
    return (
        <div className="container">
            <CalendarBlock setDate={setDate}/>
            <SearchContextProvider children={<Parametrs date={date}/>}>
                
            </SearchContextProvider>
        </div>
    )
}