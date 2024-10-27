import { inject } from "mobx-react";
import PlaceCount from "../placeCount/PlaceCount";
import WagonType from "../wagonType/WagonType";
import './Parametrs.css'
import { useState, useEffect } from "react";
import { NavLink } from "react-router-dom";
import { useSearchContext } from "../../contexts/searchContexts/SearchContextProvider";


export default function Parametrs({date}){
    const [wagonTypes, setWagonTypes] = useState([]);
    const {start, toggleStart, end, toggleEnd} = useSearchContext();

    useEffect(() => {
        console.log("Start updated: ", start);
        console.log("End updated: ", end);
    }, [start, end]);

    const handlerClick = () => {
        setTimeout(() => {
            console.log("ОТПРАВКА", date, wagonTypes, start, end);
        }, 0);
        // console.log('Start ' + typeof(start), end.length);
    }

    return(
        <div className="parametrs">
            <WagonType setWagonTypes={setWagonTypes} wagonTypes={wagonTypes}/>
            {/* <PlaceCount/> */ } 
            {/* <button className="searchBtn" onClick={handlerClick}>Поиск</button> */}
            <NavLink to={"/choice"} className={"searchBtn"} onClick={handlerClick} >Поиск</NavLink>
        </div>
    )
}