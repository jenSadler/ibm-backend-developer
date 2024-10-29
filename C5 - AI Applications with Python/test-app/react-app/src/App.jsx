import { useState,useEffect } from 'react'
import './App.css'

function App() {
  const [data, setData] = useState(null);

  useEffect(() => {
    fetch(`${import.meta.env.VITE_API_URL}/greeting`)
        .then(response => {
            if (!response.ok) {
                throw new Error("Network response was not ok");
            }
            return response.json(); // Parse JSON only if response is ok
        })
        .then(data => setData(data))
        .catch(error => console.error("Fetch error:", error));
  }, []);

  return (
      <div>
          <h1>React and Flask Example</h1>
          {data ? <p>{data.hello}</p> : <p>Loading...</p>}
      </div>
  );
}

export default App
