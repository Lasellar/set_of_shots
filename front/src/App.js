import logo from './logo.svg';
import './App.css';
import {useEffect} from "react";

function App() {

  function test() {
    fetch("http://127.0.0.1:8000/bars/zinziver/")  // Убедитесь, что здесь правильный адрес
        .then(response => {
          if (!response.ok) {
            throw new Error('Network response was not ok');
          }
          return response.json();  // Или response.text(), если это не JSON
        })
        .then(data => {
          console.log(data);  // Обрабатываем полученные данные
        })
        .catch(error => {
          console.error('There has been a problem with your fetch operation:', error);
        });
  }

  // Вызов функции после монтирования компонента
  useEffect(() => {
    test();
  }, []);

  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>
          lox
        </p>
        <a
          className="App-link"
          href="https://reactjs.org"
          target="_blank"
          rel="noopener noreferrer"
        >
          Learn React
        </a>
      </header>
    </div>
  );
}

export default App;
