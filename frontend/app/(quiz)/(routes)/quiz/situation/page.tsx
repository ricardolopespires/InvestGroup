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
  const [click, setClick] = useState(0)
  const [quiz, setQuiz] = useState([]);
  const [formData, setFormData] = useState({
    id: "",
    usuario:"",
  });



  const user = JSON.parse(localStorage.getItem('user'))

  useEffect(() => {
    const getUserData = async () => {
      try {
        const res = await AxiosInstance.get(`/api/v1/auth/user/${user.email}`);           
        return res.data;
      } catch (error) {
        console.error('Erro ao obter dados:', error);
        return [];
      }
    };

    getUserData()
      .then(Data => {
        setQuiz(Data);
      })
      .catch(error => {
        console.error('Erro ao obter condomínios:', error);
      });
  }, []);

  useEffect(() => {
        const getUserData = async () => {
            try {
                const res = await AxiosInstance.get("/api/v1/quiz/details/4445");       
                
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
        setClick(click + 1)      
      };

     
  useEffect(() => {
    if (click === 15) {
      const perfilIdMap = {
        1: { min: 0, max: 15 },
        2: { min: 15, max: 30 },
        3: { min: 30, max: 45 },
       
      };
  
      const formData = {
        usuario: [quiz.id]
      };
  
      let perfilId;
      for (const id in perfilIdMap) {
        const intervalo = perfilIdMap[id];
        if (total > intervalo.min && total <= intervalo.max) {
          perfilId = id;
          break;
        }
      }
  
      if (perfilId) {
        formData["id"] = perfilId;
        quiz["situation"] = true
        
        /*Adicionando o perfil do investido na Api */
        AxiosInstance.put(`/api/v1/auth/situation/${perfilId}/username/`, formData);
        /*Marcando como concluido o questinario */
        AxiosInstance.put(`/api/v1/auth/user/${user.email}`,quiz)
        /*retornando para dashboard */
        router.push("/dashboard")
      }
    }
  }, [click, total, quiz]);



  return (
    <div className='flex w-full h-screen px-40'>
    <div className='flex flex-col relative top-[40px] w-full space-y-7'>
        <div className='flex flex-col justify-center w-full items-center relative top-[70px]'>
            <Image src={"/images/logo.png"} width={190} height={190} alt='logo'/>
            <h1 className='flex text-[40px] '>Situação Financeira do Investidor</h1>
        </div>
        <div className="flex flex-col items-start relative top-[40px]">
        <h4 className="mt-10 text-xl">Question {currentQuestion + 1} of {data.length}</h4>
            <div className="mt-4 text-2xl">
                {data[currentQuestion] && data[currentQuestion].name }
            </div>
        </div>
        <div className="flex flex-col w-[60%] items-start relative top-[70px]">
            {data[currentQuestion] && data[currentQuestion].answers.map((item, i) => (
                <div
                key={i}
                className="flex items-start w-full py-1 pl-5 m-2 ml-0 space-x-2 cursor-pointer rounded-xl"
                >     
               <button onClick={handleNext} value={item.score}
                      className="w-full justify-start py-3 border-2 hover:bg-yellow-400 hover:text-white hover:font-semibold hover:border-yellow-400 text-gray-600  rounded-lg"
                    >{item.name}
                    </button>
                </div>
            ))}
             {click === 15 && (
            // Se for a última pergunta, exibe uma mensagem especial
            <div className="mt-4 text-lg font-semibold text-green-600">
              Parabéns, você respondeu todas as perguntas! total: {total}
            </div>
          )}
        </div>
    
    </div>
  </div>
  )
}

export default page
