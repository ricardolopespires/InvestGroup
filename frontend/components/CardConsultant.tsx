import React from 'react';

const CardConsultant: React.FC = () => {
  return (
    <div className="relative w-80 p-4 rounded-lg flex flex-col items-center justify-center border bg-white mb-6">
      <div className="h-40 w-60  flex items-center justify-center bg-gray-100 shadow-md">
        <div className="h-[calc(100%-25px)] w-[calc(100%-25px)]  overflow-hidden">
          <img 
            className="h-full w-full object-cover" 
            src="https://images.unsplash.com/photo-1492288991661-058aa541ff43?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=500&q=60" 
            alt="Consultant" 
          />
        </div>
      </div>
      <div className="absolute top-4 left-4 text-lg text-gray-600 cursor-pointer opacity-70">
        <i className="fas fa-arrow-left"></i>
      </div>
      <div className="absolute top-4 right-4 text-lg text-gray-600 cursor-pointer opacity-70">
        <i className="fas fa-ellipsis-v"></i>
      </div>
      <div className="text-xl font-medium text-gray-800 mt-4">Max Andrellino</div>
      <div className="text-lg text-gray-600 mt-1">Crypto Ativos</div>
      <div className="flex mt-6 space-x-3">
        <a href="#" className="h-10 w-10 flex items-center justify-center rounded-full bg-gray-100 hover:bg-gray-200">
          <i className="fab fa-facebook-f text-blue-600"></i>
        </a>
        <a href="#" className="h-10 w-10 flex items-center justify-center rounded-full bg-gray-100 hover:bg-gray-200">
          <i className="fab fa-twitter text-blue-400"></i>
        </a>
        <a href="#" className="h-10 w-10 flex items-center justify-center rounded-full bg-gray-100 hover:bg-gray-200">
          <i className="fab fa-instagram text-pink-600"></i>
        </a>
        <a href="#" className="h-10 w-10 flex items-center justify-center rounded-full bg-gray-100 hover:bg-gray-200">
          <i className="fab fa-youtube text-red-600"></i>
        </a>
      </div>
      <a href={"/consultants/overview/1"} className='w-full'>
      <div className="flex w-full justify-between mt-8">        
        <button className="w-full py-3 text-sm font-medium text-gray-800 rounded-lg border-none bg-gray-100 hover:bg-gray-200 shadow-md">
          Mais Informações
        </button>                
      </div>
      </a>
      <div className="flex w-full justify-between mt-8 text-sm text-gray-800">
        <div className="flex items-center space-x-2 cursor-pointer">
          <i className="far fa-heart"></i>
          <i className="icon-2 fas fa-heart opacity-0"></i>
          <span>20.4k</span>
        </div>
        <div className="flex items-center space-x-2 cursor-pointer">
          <i className="far fa-comment"></i>
          <i className="icon-2 fas fa-comment opacity-0"></i>
          <span>14.3k</span>
        </div>
        <div className="flex items-center space-x-2 cursor-pointer">
          <i className="fas fa-share"></i>
          <span>12.8k</span>
        </div>
      </div>
    </div>
  );
};

export default CardConsultant;
