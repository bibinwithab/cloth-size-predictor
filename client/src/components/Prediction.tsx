import React, { useState } from "react";
import axios from "axios";

interface UserMeasurements {
  chest: number;
  shoulder: number;
  front_length: number;
  sleeve_length: number;
}

const Prediction: React.FC = () => {
  const [chest, setChest] = useState<string>("");
  const [shoulder, setShoulder] = useState<string>("");
  const [frontLength, setFrontLength] = useState<string>("");
  const [sleeveLength, setSleeveLength] = useState<string>("");
  const [predictedSize, setPredictedSize] = useState<string>("");

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();

    const userMeasurements: UserMeasurements = {
      chest: parseFloat(chest),
      shoulder: parseFloat(shoulder),
      front_length: parseFloat(frontLength),
      sleeve_length: parseFloat(sleeveLength),
    };

    try {
      const response = await axios.post(
        "http://localhost:8000/predict",
        userMeasurements
      );
      setPredictedSize(response.data.predicted_size);
    } catch (error) {
      console.error("There was an error predicting the size!", error);
    }
  };

  return (
    <div className="bg-white p-6 sm:p-8 md:p-10 lg:p-12 rounded shadow-md w-full max-w-md mx-auto">
      <form onSubmit={handleSubmit}>
        <div className="mb-4">
          <label className="block text-gray-700 text-sm font-bold mb-2">
            Chest (in inches)
          </label>
          <input
            type="number"
            value={chest}
            onChange={(e) => setChest(e.target.value)}
            className="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 focus:outline-none focus:ring-2 focus:ring-blue-500"
          />
        </div>
        <div className="mb-4">
          <label className="block text-gray-700 text-sm font-bold mb-2">
            Shoulder (in inches)
          </label>
          <input
            type="number"
            value={shoulder}
            onChange={(e) => setShoulder(e.target.value)}
            className="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 focus:outline-none focus:ring-2 focus:ring-blue-500"
          />
        </div>
        <div className="mb-4">
          <label className="block text-gray-700 text-sm font-bold mb-2">
            Front Length (in inches)
          </label>
          <input
            type="number"
            value={frontLength}
            onChange={(e) => setFrontLength(e.target.value)}
            className="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 focus:outline-none focus:ring-2 focus:ring-blue-500"
          />
        </div>
        <div className="mb-4">
          <label className="block text-gray-700 text-sm font-bold mb-2">
            Sleeve Length (in inches)
          </label>
          <input
            type="number"
            value={sleeveLength}
            onChange={(e) => setSleeveLength(e.target.value)}
            className="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 focus:outline-none focus:ring-2 focus:ring-blue-500"
          />
        </div>
        <button
          type="submit"
          className="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded w-full"
        >
          Predict Size
        </button>
      </form>
      {predictedSize && (
        <div className="mt-4 p-4 bg-green-100 rounded shadow-md text-center">
          <p className="text-lg">
            Predicted Size: <strong>{predictedSize}</strong>
          </p>
        </div>
      )}
    </div>
  );
};

export default Prediction;
