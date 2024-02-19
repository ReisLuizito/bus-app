import React from 'react';

const BusTable = ({ busData }) => {
  return (
    <table>
      <thead>
        <tr>
          <th>Linha</th>
          <th>Velocidade</th>
          <th>Tempo até o local de partida</th>
        </tr>
      </thead>
      <tbody>
        {busData.map((bus, index) => (
          <tr key={index}>
            <td>{bus.linha}</td>
            <td>{bus.velocidade} km/h</td>
            <td>{bus.tempoPartida !== null ? `${bus.tempoPartida} seg` : '-'}</td>
          </tr>
        ))}
      </tbody>
    </table>
  );
};

export default BusTable;
