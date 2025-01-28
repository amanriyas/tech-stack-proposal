import './App.css';
import axios from 'axios';
import React, { useEffect, useState } from 'react';

function App() {
  const [data, setData] = useState(null);

  useEffect(() => {
    axios
      .get('http://127.0.0.1:8000/') // Django API endpoint
      .then((response) => setData(response.data.message)) // Access the `message` key
      .catch((error) => console.error('Error fetching data:', error));
  }, []);

  return (
    <>
      <div>
        <h1>{data}</h1> {/* This will display the "Hello World" message */}
      </div>
    </>
  );
}

export default App;
