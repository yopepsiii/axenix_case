import { useEffect } from 'react';
import { SearchContextProvider, useSearchContext } from '../../contexts/searchContexts/SearchContextProvider'
import './Search.css'

export default function Search() {
    const {start, toggleStart, end, toggleEnd} = useSearchContext();

    const handlerStart = (e) => {
        toggleStart(e.target.value);
    }

    useEffect(() => {
        toggleStart(start);
        console.log("3 " + start);
    }, [start])

    const handlerEnd = (e) => {
        toggleEnd(e.target.value);
    }

    useEffect(() => {
        toggleStart(end);
        console.log("4 " + end);
    }, [end])


    return (
            <form action="" className='search'>
                <input type="text" onChange={handlerStart}/>
                <button><img src="/img/Process.png" alt="" /></button>
                <input type="text" onChange={handlerEnd} />
            </form>

    )

}