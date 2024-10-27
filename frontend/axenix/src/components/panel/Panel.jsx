import { NavLink } from "react-router-dom";

import "./Panel.css"
import Choice from ".././../pages/choice/Choice"

function Panel( props) {
    const { data } = props;
    return (
        <div className="panel">
            <div className="column">
                <h1>Сервис для заказа билетов</h1>
                <div className="smallText">
                    <p>Lorem ipsum dolor sit amet consectetur.</p>
                    <p>adipisicing elit. Quia ducimus laudantium.</p>
                </div>
                <ul>
                    <li className="galka">
                        <div >
                            <img src="/img/group 190.svg" alt="" />
                        </div>
                        Можем и то </li>
                    <li>
                        <div className="galka">
                            <img src="img/group 190.svg" alt="" />
                        </div>
                        И то</li>
                    <li>
                        <div className="galka">
                            <img src="/img/group 190.svg" alt="" />
                        </div>
                        И то</li>
                </ul>
                <NavLink to={"parametrs"}><button>Найти</button></NavLink>  

                {/* {
                    data.map((link) =>
                    <NavLink to={link.path} key={link.path} className={({ isActive }) => (isActive ? "active" : "")}>{link.value}</NavLink>)
                }
                </div> */}
            </div>
            <img src="img/Group 197.svg" alt="" />

        </div>


    )
}

export default Panel