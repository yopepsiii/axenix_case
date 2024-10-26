import { inject } from "mobx-react";
import PlaceCount from "../placeCount/PlaceCount";
import WagonType from "../wagonType/WagonType";
import './Parametrs.css'
import { useState, useEffect } from "react";


export default function Parametrs({date}){
    const [wagonTypes, setWagonTypes] = useState([]);

    const handlerClick = () => {
        
        console.log(date, wagonTypes);
    }

    return(
        <div className="parametrs">
            <WagonType setWagonTypes={setWagonTypes} wagonTypes={wagonTypes}/>
            {/* <PlaceCount/> */ } 
            <button className="searchBtn" onClick={handlerClick}>Поиск</button>
        </div>
    )
}