import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import Employees from "./components/Employees";
import Register from "./components/Register";
import EditEmployee from "./components/EditEmployee";

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<Employees />} />
        <Route path="/register" element={<Register />} />
        <Route path="/edit/:id" element={<EditEmployee />} />
        
      </Routes>
    </Router>
  );
}

export default App;