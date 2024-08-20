import "./App.css";
import Prediction from "./components/Prediction";

function App() {
  return (
    <div className="min-h-screen bg-gray-300 flex flex-col justify-center items-center">
      <h1 className="text-3xl font-bold mb-4">Cloth Size Predictor</h1>
      <Prediction />
    </div>
  );
}

export default App;
