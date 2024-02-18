import Search from "./components/search"
import MyForm from "./components/results"

import './App.css';
import React from 'react';
import ReactDOM from 'react-dom/client';
import { BrowserRouter, Routes, Route } from "react-router-dom";

function App() {
  return (
    <div className="App">
      <div className="App-header">
        <BrowserRouter>
          {/* <Navbar/> */}
          <Routes>
            <Route path="query" element={<MyForm />} />
            <Route path="/" element={<Search />}>
            </Route>
          </Routes>
          {/* <Navbar/> */}
        </BrowserRouter>


      </div>
    </div>
  );
}

const root = ReactDOM.createRoot(document.getElementById('root'));
// root.render(<App />);
export default App;
