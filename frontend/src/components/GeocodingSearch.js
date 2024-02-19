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

    const isWithinRioDeJaneiro = (result) => {
        const rioDeJaneiroBounds = {
            minLat: -23.0000,
            maxLat: -22.8000,
            minLng: -43.8000,
            maxLng: -43.1000,
        };

        return (
            result.geometry.coordinates[1] >= rioDeJaneiroBounds.minLat &&
            result.geometry.coordinates[1] <= rioDeJaneiroBounds.maxLat &&
            result.geometry.coordinates[0] >= rioDeJaneiroBounds.minLng &&
            result.geometry.coordinates[0] <= rioDeJaneiroBounds.maxLng
        );
    };

    const handlePointSelection = (result) => {
        if (isWithinRioDeJaneiro(result)) {
            setSelectedItem(result);
            if (typeof onPointSelect === 'function') {
                onPointSelect(result);
            } else {
                console.error('onPointSelect não é uma função');
            }
        } else {

            setSelectedItem(null);
            setResults([]);
        }
    };

    return (
        <div id='location_container'>
            <input id='location_input' type="text" value={query} onChange={(e) => setQuery(e.target.value)} placeholder="Insira uma localidade ou ponto de ônibus" />
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
