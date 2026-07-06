import { useEffect, useState } from "react";
import "./App.css";

function App() {
  const [health, setHealth] = useState(null);
  const [version, setVersion] = useState(null);

  useEffect(() => {
    fetch("/api/health")
      .then((res) => res.json())
      .then((data) => setHealth(data))
      .catch(() => setHealth({ status: "DOWN" }));

    fetch("/api/version")
      .then((res) => res.json())
      .then((data) => setVersion(data));
  }, []);

  return (
    <div className="container">
      <h1>CI/CD Docker Compose Project</h1>

      <div className="card">
        <h2>Backend Status</h2>

        <p>
          Status:
          <strong>{health ? health.status : "Loading..."}</strong>
        </p>

        <p>
          Service:
          <strong>{health ? health.service : "Loading..."}</strong>
        </p>

        <p>
          Version:
          <strong>{version ? version.version : "Loading..."}</strong>
        </p>
      </div>
    </div>
  );
}

export default App;