import React, { useState, useEffect } from 'react';
import axios from 'axios';
import GeocodingSearch from './components/GeocodingSearch';

function App() {
    const [selectedBusLine, setSelectedBusLine] = useState('');
    const [busData, setBusData] = useState([]);

    useEffect(() => {
        axios.get('http://127.0.0.1:8000/linhas-onibus')
            .then(response => {
                const data = response.data;
                const select = document.getElementById('linhas-onibus');
                data.linhas.forEach(linha => {
                    const option = document.createElement('option');
                    option.text = linha;
                    select.add(option);
                });
            })
            .catch(error => {
                console.error('Erro ao buscar as linhas de ônibus:', error);
            });
    }, []);

    const handleBusLi