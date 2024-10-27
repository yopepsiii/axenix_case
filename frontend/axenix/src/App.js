import './App.css';
import React from 'react';
import { BrowserRouter, Routes, Route, Link, useNavigate } from 'react-router-dom';
import Header from './components/header/Header';
import Main from './pages/main/Main'
import Choice from './pages/choice/Choice'
import PlaceChoice from './pages/placeChoice/PlaceChoice';
import Parametrs from './components/parametrs/Parametrs';
import ParametrsPage from './pages/ParametrsPage/ParametrsPage';

function App() {
  return (
    <div className="App">
      <BrowserRouter>
        <Header />
        <Routes>
          <Route path='/' element={<Main/>}/>
          <Route path='choice' element={<Choice/>}/>
          <Route path='parametrs' element={<ParametrsPage/>}/>
          <Route path='placechoice' element={<PlaceChoice/>}/>
        </Routes>
      </BrowserRouter>
    </div>
  );
}

export default App; 