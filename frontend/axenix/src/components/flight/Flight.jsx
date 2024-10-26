import "./Flight.css"
function Flight() {
    return (
        <div className="flights">



            <div className="flightPanel">
                <div className="par">Ростов-на-Дону &#8594; Россошь &#8594; Воронеж &#8594; Москва</div>
                <div className="flightRows">
                    <div className="flightColumn">
                        <h1>11:46</h1>
                        <div className="flightAway">12 янв, понедельник</div>
                        <div className="placeAway">Москва ВК Восточный</div>
                    </div>
                    <div className="flightColumn">
                        <h1>21:55</h1>
                        <div className="flightAway">18 февраля, вторник</div>
                        <div className="placeAway">Санкт-Петербург-Главный</div>
                    </div>
                    <div className="lineVert"></div>
                    <div className="flightColumnForBuy">
                        <h1>1100 ₽</h1>
                        <input type="submit" className="choicePlace" value="Выбрать место" />
                    </div>
                </div>
            </div>

            <div className="flightPanel">
                <div className="par">Ростов-на-Дону &#8594; Россошь &#8594; Воронеж &#8594; Москва</div>
                <div className="flightRows">
                    <div className="flightColumn">
                        <h1>11:46</h1>
                        <div className="flightAway">12 янв, понедельник</div>
                        <div className="placeAway">Москва ВК Восточный</div>
                    </div>
                    <div className="flightColumn">
                        <h1>21:55</h1>
                        <div className="flightAway">18 февраля, вторник</div>
                        <div className="placeAway">Санкт-Петербург-Главный</div>
                    </div>
                    <div className="lineVert"></div>
                    <div className="flightColumnForBuy">
                        <h1>1100 ₽</h1>
                        <input type="submit" className="choicePlace" value="Выбрать место" />
                    </div>
                </div>
            </div>




        </div>


    )
}

export default Flight