// import { createContext, useContext, useEffect } from "react";
import { useSearchAppContext } from "./SearchContext";


// const Context = createContext(null);

// export const SearchContextProvider = ({ children, ...props }) => {
//     const context =  useSearchAppContext(props);
//     return <Context.Provider value={context}>{children}</Context.Provider>;
// };

// export function useSearchContext() {
//     const context = useContext(Context);
//     if (!context) throw new Error('Use app context within provider!');
//     return context;
// };

import { createContext, useContext, useState } from "react";

const SearchContext = createContext();

export const SearchContextProvider = ({ children }) => {
    const [start, setStart] = useState(""); // Начальное значение
    const [end, setEnd] = useState("");     // Начальное значение

    const toggleStart = (newStart) => {
        setStart(newStart);  // Обновление значения start
    };

    const toggleEnd = (newEnd) => {
        setEnd(newEnd);  // Обновление значения end
    };

    return (
        <SearchContext.Provider value={{ start, toggleStart, end, toggleEnd }}>
            {children}
        </SearchContext.Provider>
    );
};

export const useSearchContext = () => useContext(SearchContext);