import "./Panel.css"
function Panel() {
    return (
            <div className="panel">
                <div className="column">
                <h1>Дайте деняг</h1>
                <p>Думайте текст сами, бла бла бла бла</p>
                <p>бла бла бла бла бла бла бла</p>
                <ul>
                    <li>
                        <div className="galka">
                            <img src="img/Done.svg" alt="" />
                        </div>
                        Можем и то</li>
                        <li>
                        <div className="galka">
                            <img src="img/Done.svg" alt="" />
                        </div>
                        И то</li>
                        <li>
                        <div className="galka">
                            <img src="img/Done.svg" alt="" />
                        </div>
                        И то</li>
                </ul>
                <input type="submit" value ="Найти" />
                </div>
                <img src="img/Train.svg" alt="" />

            </div>
    

    )
}

export default Panel