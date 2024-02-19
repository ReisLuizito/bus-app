import React from 'react';
import BusTable from './BusTable';

const BusLineInfo = ({ selectedBusLine, busData }) => {
  return (
    <div>
      <h2>Ônibus da linha {selectedBusLine}</h2>
      <BusTable busData={busData} />
    </div>
  );
};

export default BusLineInfo;
