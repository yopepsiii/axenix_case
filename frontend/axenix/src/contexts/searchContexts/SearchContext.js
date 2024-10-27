// import { useCallback, useEffect, useState, useContext, createContext } from "react";

// const SearchContext = createContext();

// export const useSearchAppContext = function (props) {
//     const [start, setStart] = useState('');
//     const [end, setEnd] = useState('');

//     const toggleStart = useCallback((s) => {
//         setStart(s);

//     });

//     const toggleEnd = useCallback((s) => {
//         setEnd(s);
//     })
    
//     useEffect(() => {
//         console.log("Start updated: ", start);
//         console.log("End updated: ", end);
//     }, [start, end]);

//     return {
//         start,
//         toggleStart,
//         end,
//         toggleEnd
//     };
// }

// export const useSearchContext = () => useContext(SearchContext);