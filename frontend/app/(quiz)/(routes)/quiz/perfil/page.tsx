"use client"

import { questions } from '@/data/questions'
import { useRouter } from 'next/navigation';
import React, { useState, useEffect } from 'react';
import AxiosInstance from '@/services/AxiosInstance'
import Image from 'next/image';

const page = () => {

  const router = useRouter();
  const [currentQuestion, setCurrentQuestion] = useState(0);
  const [data, setData] = useState([]);
  const [total,setTotal]= useState(0);

  useEffect(() => {
        const getUserData = async () => {
            try {
                const res = await AxiosInstance.get("http://localhost:8000/api/v1/quiz/details/4444");       
                return res.data;
            } catch (error) {
                console.error('Erro ao obter dados:', error);
                return [];
            }
        };

        getUserData()
            .then(quizData => {
                setData(quizData.questions);
            })
            .catch(error => {
                console.error('Erro ao obter dados do quiz:', error);
            });
    }, []);

    const handlePrevious = () => {
        const prevQues = currentQuestion - 1;
        prevQues >= 0 && setCurrentQuestion(prevQues);
      };
      
      const handleNext = (event) => {
        const nextQues = currentQuestion + 1;      
        nextQues < data.length && setCurrentQuestion(nextQues);
        const value = parseInt(event.target.value);
        setTotal(total + value);
        console.log(total + value);
      };

      if(currentQuestion === data.length - 1 ){
        router.push('/dashboard');
      }
      
  return (
    <div className='flex w-full h-screen px-40'>
    <div className='flex flex-col relative top-[110px] w-full space-y-7'>
        <div className='flex flex-col justify-center w-full items-center relative top-[70px]'>
            <Image src={"/images/logo.png"} width={190} height={190} alt='logo'/>
            <h1 className='flex text-[40px] '>Perfil do Investidor</h1>
        </div>
        <div className="flex flex-col items-start relative top-[40px]">
        <h4 className="mt-10 text-xl">Question {currentQuestion + 1} of {data.length}</h4>
            <div className="mt-4 text-2xl">
                {data[currentQuestion] && data[currentQuestion].name }
            </div>
        </div>
        <div className="flex flex-col w-full items-start relative top-[70px]">
            {data[currentQuestion] && data[currentQuestion].answers.map((item, i) => (
                <div
                key={i}
                className="flex items-center w-full py-4 pl-5 m-2 ml-0 space-x-2 cursor-pointer rounded-xl"
                >     
               <button onClick={handleNext} value={item.score}
                      className="w-full justify-start py-3 border-2 hover:border-green-600 hover:text-green-600 hover:font-semibold text-gray-600  rounded-lg"
                    >{item.name}
                    </button>
                </div>
            ))}
             {currentQuestion === data.length - 1 && (
            // Se for a última pergunta, exibe uma mensagem especial
            <div className="mt-4 text-lg font-semibold text-green-600">
              Parabéns, você respondeu todas as perguntas!
            </div>
          )}
        </div>
    
    </div>
  </div>
  )
}

export default page
