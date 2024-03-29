// App.js

import React, { useState, useEffect } from 'react';
import axios from 'axios';
import GeocodingSearch from './components/GeocodingSearch';
import BusLineInfo from './components/BusLineInfo';

function App() {
  const [selectedBusLine, setSelectedBusLine] = useState('');
  const [busData, setBusData] = useState([]);
  const [departureTime, setDepartureTime] = useState('');
  const [selectedPoint, setSelectedPoint] = useState(null);
  const [referenceTravelTime, setReferenceTravelTime] = useState(null);
  const [pointSelected, setPointSelected] = useState(false);
  const [userEmail, setUserEmail] = useState('');

  useEffect(() => {
    const referencePoint = { lat: -22.9519, lng: -43.2106 };

    const fetchData = async () => {
      try {
        if (pointSelected) {
          const locations = [{ id: 'bus', coords: referencePoint }];
          const departure_searches = [{
            id: 'departure_search',
            departure_location_id: 'bus',
            arrival_location_ids: busData.map(bus => bus.ordem),
            departure_time: departureTime,
            travel_time: 1800,
            user_email: userEmail,
          }];

          const response = await axios.post('http://127.0.0.1:8000/calculate-travel-time', { locations, departure_searches });

          const travelTimeResult = response.data.results.find(result => result.search_id === 'bus');
          setReferenceTravelTime(travelTimeResult ? Math.floor(travelTimeResult.locations[0].properties[0].travel_time / 60) : null);
        }
      } catch (error) {
        console.error('Erro ao calcular o tempo de viagem até o ponto de referência:', error);
      }
    };

    if (departureTime) {
      fetchData();
    }
  }, [departureTime, busData, pointSelected]);

  const handleBusLineSelection = async (busLine) => {
    setSelectedBusLine(busLine);
    try {
      const response = await axios.get(`http://127.0.0.1:8000/bus-data/${busLine}`);
      const simulatedBusData = response.data.map(bus => ({
        ...bus,
        tempoPartida: Math.floor(Math.random() * 1800) + 300,
      })) || [];
      setBusData(simulatedBusData);
    } catch (error) {
      console.error('Erro ao obter os dados dos ônibus da linha:', error);
    }
  };

  useEffect(() => {
    const fetchBusLines = async () => {
      try {
        const response = await axios.get('http://127.0.0.1:8000/linhas-onibus');
        const data = response.data;
        const select = document.getElementById('linhas-onibus');

        select.innerHTML = '';

        const defaultOption = document.createElement('option');
        defaultOption.value = '';
        defaultOption.text = 'Selecione uma linha de ônibus';
        select.add(defaultOption);

        if (data.linhas && data.linhas.length > 0) {
          data.linhas.forEach(linha => {
            const option = document.createElement('option');
            option.value = linha;
            option.text = linha;
            select.add(option);
          });
        } else {
          console.error('Erro: Nenhuma linha de ônibus encontrada.');
        }
      } catch (error) {
        console.error('Erro ao buscar as linhas de ônibus:', error);
      }
    };

    fetchBusLines();
  }, [pointSelected]);

  const handlePointSelection = (result) => {
    console.log('Ponto selecionado:', result);
    setSelectedPoint(result);
    setPointSelected(true);
  };

  const handleDepartureTimeSelection = (time) => {
    setDepartureTime(time);
  };

  const handleGeocodingSearch = () => {

    setSelectedBusLine('');
    setBusData([]);
    setDepartureTime('');
    setSelectedPoint(null);
    setReferenceTravelTime(null);
    setPointSelected(false);
    
  };

  const handleEmailSubscription = async () => {
    try {
        const response = await axios.post('http://localhost:8000/subscribe', { email: userEmail });
        console.log(response.data.message);
    } catch (error) {
        console.error('Erro ao cadastrar o e-mail:', error);
    }
};

  return (
    <div className='container'>
      <div className='content_container'>
        <h1>Bem-vindo ao Bus App</h1>
        <h3>Este é um aplicativo que permite visualizar informações de ônibus, calcular tempos de viagem e receber notificações por e-mail quando um ônibus está a 10 minutos de distância.</h3>
        <input id='email_input'
                type="email"
                value={userEmail}
                onChange={(e) => setUserEmail(e.target.value)}
                placeholder="Insira seu e-mail para notificações"
            />
        <GeocodingSearch onPointSelect={(result) => handlePointSelection(result)} />
        <select id="linhas-onibus" onChange={(e) => handleBusLineSelection(e.target.value)} disabled={!pointSelected}>
          {}
        </select>
        <input type="time" value={departureTime} onChange={(e) => handleDepartureTimeSelection(e.target.value)} />
        <button onClick={handleGeocodingSearch}>Limpar Pesquisa</button>
        {selectedBusLine && <BusLineInfo selectedBusLine={selectedBusLine} busData={busData} />}
      </div>
    </div>
  );
}

export default App;
