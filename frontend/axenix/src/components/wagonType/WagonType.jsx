import './WagonType.css'
import { useState, useEffect } from 'react';


export default function WagonType({ setWagonTypes, wagonTypes }) {
    
    const [selectedWagonTypes, setSelectedWagonTypes] = useState([]);

    const handleCheckboxChange = (e) => {
        const { checked, nextSibling } = e.target;
        const label = nextSibling.textContent.trim();

        if (checked) {
            setSelectedWagonTypes([...selectedWagonTypes, label]);
        } else {
            setSelectedWagonTypes(selectedWagonTypes.filter(type => type !== label));
        }

        
        setWagonTypes(selectedWagonTypes);
        
    };

    useEffect(() => {
        console.log(selectedWagonTypes);
        setWagonTypes(selectedWagonTypes);
    }, [selectedWagonTypes])

    return (
        <div className="wagonType">
            <h3>Тип вагона</h3>
            <div><ul>
                <li>
                    <input type="checkbox" onChange={handleCheckboxChange}></input> Плацкарт
                </li>
                <li>
                    <input type="checkbox" onChange={handleCheckboxChange} ></input> Купе
                </li>
            </ul>
            </div>

        </div>
    )
}