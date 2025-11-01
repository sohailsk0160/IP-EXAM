import React, { useState } from "react";

function Student(props) {
  return (
    <div>
      <h3>Student Component (Props Demo)</h3>
      <p>Name: {props.name}</p>
      <p>Course: {props.course}</p>
    </div>
  );
}

function App() {
  const [count, setCount] = useState(0); // state

  return (
    <div>
      <h2>React State & Props Example</h2>

      {/* Props Example */}
      <Student name="Sohail" course="IT Engineering" />
      <Student name="Amaan" course="Computer Engineering" />

      <hr />

      {/* State Example */}
      <h3>Counter (State Demo)</h3>
      <p>Count: {count}</p>
      <button onClick={() => setCount(count + 1)}>
        Increase Count
      </button>
    </div>
  );
}

export default App;
