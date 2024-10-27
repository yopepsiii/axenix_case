import './App.css';
import React from 'react';
import { BrowserRouter as Router, Routes, Route, Link, useNavigate, BrowserRouter } from 'react-router-dom';
import Header from './components/header/Header';
import Main from './pages/main/Main'
import Choice from './pages/choice/Choice'
import PlaceChoice from './pages/placeChoice/PlaceChoice';

function App() {
  return (
    <div className="App">
      {/* <React.StrictMode>
        <BrowserRouter>
          <Routes>
            <Main />
            <Route path='choice' element={<Choice />} />
          </Routes>
        </BrowserRouter>
      </React.StrictMode>*/}
      <Header />
      <PlaceChoice /> 

    </div>
  );
}

export default App; 