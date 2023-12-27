import React from 'react';
import Navbar from './components/Navbar';
import './App.css';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';  // Import Routes instead of Switch
import Home from './components/pages/Home';

function App() {
  return (
    <>
      <Router>
        <Navbar />
        <Routes> {/* Change Switch to Routes */}
          <Route path='/' element={<Home />} />
        </Routes>
      </Router>
    </>
  );
}

export default App;

