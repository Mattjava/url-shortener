import { useEffect, useRef, useState } from 'react'
import './App.css'
import MainContainer from './container'

const INTERVAL_TIME = 6000;

function App() {
    const [count, setCount] = useState(0)
    const tested = useRef(false);

    useEffect(() => {
      if(tested.current) {
        return;
      }

      const inter = setInterval(() => {
      try {
        fetch('/api/url/').then((response) => {
          if(response.status != 200) {
              throw Error("URL or API server not found");
          }
          console.log("Connected!");
        });
        } catch (error) {
            console.log("Failed to connect to API.: " + error);
        }
        }, INTERVAL_TIME);
      tested.current = true;
    }, []);

  return (
    <><MainContainer/></>
  )
}

export default App
