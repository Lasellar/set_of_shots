import './App.module.css';
import AppHeader from "../components/AppHeader/AppHeader";

function App() {
  // function test() {
  //   fetch("http://127.0.0.1:8000/bars/zinziver/")  // Убедитесь, что здесь правильный адрес
  //       .then(response => {
  //         if (!response.ok) {
  //           throw new Error('Network response was not ok');
  //         }
  //         return response.json();  // Или response.text(), если это не JSON
  //       })
  //       .then(data => {
  //         console.log(data);  // Обрабатываем полученные данные
  //       })
  //       .catch(error => {
  //         console.error('There has been a problem with your fetch operation:', error);
  //       });
  // }
  //
  // // Вызов функции после монтирования компонента
  // useEffect(() => {
  //   test();
  // }, []);

  return (
    <div className="App">
     <AppHeader />
        <h1>app</h1>
    </div>
  );
}

export default App;
