import React, { useState } from 'react';
import axios from 'axios';

const GeocodingSearch = () => {
    const [query, setQuery] = useState('');
    const [results, setResults] = useState([]);

    const handleGeocodingSearch = async () => {
        try {
            const response = await axios.get(`http://localhost:8000/geocoding?query=${query}`);
            setResults(response.data || []); // Certifique-se de inicializar com um array vazio se a resposta for undefined
        } catch (error) {
            console.error('Erro na pesquisa de geocodificação:', error);
        }
    };

    return (
        <div>
            <input type="text" value={query} onChange={(e) => setQuery(e.target.value)} placeholder="Insira o endereço ou local" />
            <button onClick={handleGeocodingSearch}>Pesquisar</button>
            <ul>
                {results.map((result, index) => (
                    <li key={index}>{result.properties.name} - Lat: {result.geometry.coordinates[1]}, Lng: {result.geometry.coordinates[0]}</li>
                ))}
            </ul>
        </div>
    );
};

export default GeocodingSearch;
