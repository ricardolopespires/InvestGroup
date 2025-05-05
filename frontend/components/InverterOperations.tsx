import React from 'react';
import { useState, useEffect } from 'react';
import { MdCurrencyExchange } from 'react-icons/md'; // Assuming you're using react-icons for MdCurrencyExchange
import {postInversorOperations}  from "@/lib/actions/actions.operations"; // Adjust the import path as necessary



const InverterOperations = ({ operation }) => {


  const handleOperation = async (ticket: number, type: string) => {
    // Logic to handle the operation with ticket and type
    console.log(`Handling operation: Ticket=${ticket}, Type=${type}`);
    // Add your async logic here
  };

  const handleClick = (e: React.MouseEvent<HTMLButtonElement>) => {
    e.preventDefault(); // Prevent default button behavior if needed
    if (operation && operation.ticket && operation.type) {
        postInversorOperations({ticket:operation.ticket, type:operation.type});
    }
  };

  return (
    <div className="inverter-operations">
      <button
        className="bg-blue-500 text-white h-6 w-6 rounded-sm text-sm flex items-center justify-center"
        onClick={handleClick}
      >
        <MdCurrencyExchange />
      </button>
    </div>
  );
};

export default InverterOperations;