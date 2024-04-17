



import React, {useEffect, useState} from 'react'
import axios from 'axios'


const Balance = () => {
    const [data, setData] = useState([]);

    useEffect(() => {
  
        axios.get("http://localhost:8000/api/v1/finance/bank/2")
        .then(res => setData(res.data))
        .catch(err => console.error(err))
  
    },[])

  return (
    <div>
        {data.map(( item, i)=>{
            return(
                <div className="flex items-center space-x-2  text-[28px]" key={i}>
                    <h1>{item.balance}</h1><span>{item.currency}</span>
                </div>
            )
        })}
    </div>
  )
}

export default Balance
