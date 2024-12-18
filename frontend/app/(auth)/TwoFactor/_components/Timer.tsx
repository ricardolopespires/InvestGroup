import { useEffect, useState } from 'react';
import { useAtom } from 'jotai';
import { counterAtom } from '@/store/store';


const Timer = () => {
  const [time, setTime] = useAtom(counterAtom);

  useEffect(() => {
    const interval = setInterval(() => {
      setTime(prev => {
        if (prev > 0) {
          return prev - 1;
        } else {
          clearInterval(interval);
          return 0;
        }
      });
    }, 1000);

    return () => clearInterval(interval);
  }, [setTime]);

  return (
    <div>
      <h1>0 : {time} </h1>
    </div>
  );
};

export default Timer;