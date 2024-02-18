import React, { useState } from 'react';
import axios from 'axios';

const GeocodingSearch = ({ onPointSelect }) => {
  const [query, setQuery] = useState('');
  const [results, setResults] = useState([]);
  const [selectedItem, setSelectedItem] = useState(null);

  const handleGeocodingSearch = async () => {
    try {
      const response = await axios.get(`http://localhost:8000/geocoding?query=${query}`);
      setResults(response.data || []);
    } catch (error) {
      console.error('Erro na pesquisa de geocodificação:', error);
    }
  };

  const handlePointSelection = (result) => {
    setSelectedItem(result);
    if (typeof onPointSelect === 'function') {
      onPointSelect(result);
    } else {
      console.error('onPointSelect não é uma função');
    }
  };

  return (
    <div>
      <input type="text" value={query} onChange={(e) => setQuery(e.target.value)} placeholder="Insira uma localidade ou ponto" />
      <button onClick={handleGeocodingSearch}>Pesquisar</button>
      <ul>
        {Array.isArray(results) &&
          results.map((result, index) => (
            <li key={index} onClick={() => handlePointSelection(result)} style={{ backgroundColor: selectedItem === result ? 'lightblue' : 'white' }}>
              {result.properties.name} - Lat: {result.geometry.coordinates[1]}, Lng: {result.geometry.coordinates[0]}
            </li>
          ))}
      </ul>
    </div>
  );
};

export default GeocodingSearch;
