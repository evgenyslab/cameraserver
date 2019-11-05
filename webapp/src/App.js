import React from 'react';
import logo from './logo.svg';
import './App.css';


function App() {
  return (
    <div className="App">
      <header className="App-header">
        <img src="http://192.168.0.26:7777" />
        <p>
          Edit <code>src/App.js</code> and save to reload.
        </p>
        <form onSubmit={e => { e.preventDefault(); }} >
          <label>
            Command:
            <input type="text" name="name" />
          </label>
          <input type="submit" value="Submit" />
        </form>
      </header>
    </div>
  );
}

export default App;
