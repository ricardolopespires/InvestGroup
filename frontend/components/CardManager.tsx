import { toCapitalizer } from '@/lib/utils';
import React from 'react';

// Define props interface for type safety
interface CardManagerProps {
  id: string;
  // Optional properties with default values
  name?: string;
  about?: string;
  imageUrl?: string;
  likes?: string;
  comments?: string;
  shares?: string;
  asset?: string;
  assetName?: string;
}

const CardManager: React.FC<CardManagerProps> = ({
  id,
  name,
  about,
  imageUrl,
  likes = '20.4k',
  comments = '14.3k',
  shares = '12.8k',
  asset = 'BTC',
}) => {
  return (
    <div className=" font-poppins">
      <style jsx>{`
        .neumorphic {
          background: #ecf0f3;
          box-shadow: -3px -3px 7px #ffffff, 3px 3px 5px #ceced1;
        }
        .neumorphic-hover:hover::before {
          content: '';
          position: absolute;
          top: 0;
          left: 0;
          right: 0;
          bottom: 0;
          border-radius: 50%;
          background: #ecf0f3;
          box-shadow: inset -3px -3px 7px #ffffff, inset 3px 3px 5px #ceced1;
        }
        .neumorphic-button:hover::before {
          content: '';
          position: absolute;
          top: 0;
          left: 0;
          right: 0;
          bottom: 0;
          border-radius: 5px;
          background: #ecf0f3;
          box-shadow: inset -3px -3px 7px #ffffff, inset 3px 3px 5px #ceced1;
          z-index: -1;
        }
        .social-row::before {
          content: '';
          position: absolute;
          height: 100%;
          width: 2px;
          background: #e0e6eb;
          left: -25px;
        }
        .social-row:first-child::before {
          background: none;
        }
      `}</style>
      <div className="relative w-[270px] p-8 rounded-xl flex flex-col items-center neumorphic">
        {/* Arrow Icon */}
        <div className="absolute left-4 top-4 w-[35px] h-[35px] flex items-center justify-center rounded-full text-[#31344b] opacity-70 cursor-pointer neumorphic-hover">
          <i className="fas fa-arrow-left text-base z-10"></i>
        </div>
        {/* Dots Icon */}
        <div className="absolute right-4 top-4 w-[35px] h-[35px] flex items-center justify-center rounded-full text-[#31344b] opacity-70 cursor-pointer neumorphic-hover">
          <i className="fas fa-ellipsis-v text-base z-10"></i>
        </div>
        {/* Image Area */}
        <div className="w-[150px] h-[150px] rounded-full flex items-center justify-center neumorphic">
          <div className="w-[125px] h-[125px] rounded-full overflow-hidden">
            <img src={imageUrl} alt={name} className="w-full h-full object-cover" />
          </div>
        </div>
        {/* Name */}
        <div className="mt-3 text-[23px] font-medium text-[#31344b]">{name}</div>
        {/* About */}
        <div className="text-[#44476a] font-normal text-base">{toCapitalizer(asset)}</div>
        {/* Social Icons */}
   
        {/* Buttons */}
        <a href={`/agents/managers/${id}`}>  
          <div className="flex w-full justify-between mt-6">
            <button className="relative flex-1 mr-2 py-3 px-6 text-[#31344b] text-base font-normal rounded-md neumorphic neumorphic-button z-10">
              Mais Informações
            </button>      
          </div>
        </a>        
        {/* Social Share */}
        <div className="flex w-full mt-8 px-1 justify-between">
          <div className="relative flex items-center text-[#31344b] text-base cursor-pointer social-row group">
            <i className="far fa-heart"></i>
            <i className="fas fa-heart absolute left-0 top-1/2 -translate-y-1/2 text-[#31344b] opacity-0 transition-opacity duration-300 group-hover:opacity-100"></i>
            <span className="ml-2">{likes}</span>
          </div>
          <div className="relative flex items-center text-[#31344b] text-base cursor-pointer social-row group">
            <i className="far fa-comment"></i>
            <i className="fas fa-comment absolute left-0 top-1/2 -translate-y-1/2 text-[#31344b] opacity-0 transition-opacity duration-300 group-hover:opacity-100"></i>
            <span className="ml-2">{comments}</span>
          </div>
          <div className="relative flex items-center text-[#31344b] text-base cursor-pointer social-row">
            <i className="fas fa-share"></i>
            <span className="ml-2">{shares}</span>
          </div>
        </div>
      </div>
    </div>
  );
};

export default CardManager;