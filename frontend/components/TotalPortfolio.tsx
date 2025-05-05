import { GoTriangleDown, GoTriangleUp } from "react-icons/go";






import React from 'react'

const TotalPortfolio = () => {
  return (
    <div>
    <div className="mb-1 text-sm text-gray-500">Total Portfolio</div>
    <div className="flex items-center gap-2">
      <div className="flex h-8 w-8 items-center justify-center rounded-lg bg-teal-100">
        <svg viewBox="0 0 24 24" className="h-5 w-5 text-teal-600" fill="none" stroke="currentColor">
          <path
            d="M12 8c-1.657 0-3 .895-3 2s1.343 2 3 2 3 .895 3 2-1.343 2-3 2m0-8c1.11 0 2.08.402 2.599 1M12 8V7m0 1v8m0 0v1m0-1c-1.11 0-2.08-.402-2.599-1M21 12a9 9 0 11-18 0 9 9 0 0118 0z"
            strokeWidth="2"
            strokeLinecap="round"
            strokeLinejoin="round"
          />
        </svg>
      </div>
      <div className='flex  items-center gap-4'>
      <span className="text-3xl font-semibold">$145,628.01</span>
      <div className='flex items-center gap-1 text-xs text-white bg-blue-950  p-2 rounded-sm'>
      <GoTriangleUp className="text-lg"/>
      <span>20%</span>
      </div>
      </div>
    </div>
  </div>
  )
}

export default TotalPortfolio