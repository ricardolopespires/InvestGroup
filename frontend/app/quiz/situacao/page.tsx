"use client";

import Logout from "@/app/auth/Logout/page";
import {  quizSituation, quizUserAnswers, updatedQuizSituation  } from "@/lib/actions/actions.quiz";
import { GrAchievement } from "react-icons/gr";
import { useEffect, useState } from "react";
import { useRouter } from "next/navigation";



const QuizPage = () => {
  const [questions, setQuestions] = useState<Question[]>([]);
  const [currentQuestionIndex, setCurrentQuestionIndex] = useState(0);
  const [selectedAnswers, setSelectedAnswers] = useState<number[]>([]);
  const [isLoading, setIsLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);


    const router = useRouter();

  const user: User | null = JSON.parse(localStorage.getItem("user") || "null");

  useEffect(() => {
    const fetchQuestions = async () => {
      try {
        setIsLoading(true);
        const response = await quizSituation();
        
        if (!response || !Array.isArray(response.questions)) {
          throw new Error("Estrutura de resposta inválida");
        }
        
        setQuestions(response.questions);
      } catch (err) {
        console.error("Erro ao buscar o quiz:", err);
        setError("Erro ao carregar as perguntas. Tente novamente.");
      } finally {
        setIsLoading(false);
      }
    };

    fetchQuestions();
  }, []);

  const handleAnswerClick = async (answerIndex: number) => {
    if (!user) return;

    const newSelectedAnswers = [...selectedAnswers, answerIndex];
    setSelectedAnswers(newSelectedAnswers);
    
    const currentQuestion = questions[currentQuestionIndex];
    
    // Envia a resposta do usuário
    if (newSelectedAnswers.length <= questions.length) {
      try {
        await quizUserAnswers({
          UserId: user.email,
          QuestionId: currentQuestion.title,
          AnwserId: currentQuestion.answers[answerIndex].answer_text || currentQuestion.answers[answerIndex].text
        });
      } catch (err) {
        console.error("Erro ao salvar resposta:", err);
      }
    }

    // Processa próxima pergunta ou finaliza
    if (currentQuestionIndex < questions.length - 1) {
      setCurrentQuestionIndex(currentQuestionIndex + 1);
    } else {
      try {
        const totalScore = newSelectedAnswers.reduce((sum, value) => sum + value, 0);
        const response = await updatedQuizSituation ({
          ValueId: totalScore,
          userId: user.email,
        });

        console.log(response);
        if (response.status === 200) {
            localStorage.setItem('situacao', JSON.stringify(true)); 
            router.push("/dashboard/overview");
        }
      } catch (err) {
        console.error("Erro ao atualizar perfil:", err);
      }
    }
  };

  const currentQuestion = questions[currentQuestionIndex];
  const isQuizCompleted = selectedAnswers.length >= questions.length;

  return (
    <div className="w-full min-h-screen flex flex-col items-center">
      <header className="w-full h-20 flex items-center justify-between shadow-md px-4">
        <a href={"/"} className="flex items-center gap-2 ">
            <div className="flex items-center gap-4 cursor-pointer">      
                <img src="/images/logo.png" alt="Logo" className="h-12" />          
            </div>
        </a>
        <div className="text-2xl">
          <Logout />
        </div>
      </header>

      {error ? (
        <div className="mt-16 text-red-600 text-xl">{error}</div>
      ) : isQuizCompleted ? (
        <div className="flex flex-col items-center justify-center mt-60 gap-4">
          <GrAchievement className="text-[140px] text-amber-500" />
          <p className="text-xl text-center">Obrigado por completar o quiz!</p>
        </div>
      ) : (
        <div className="flex flex-col items-center w-full max-w-4xl px-4">
          <h1 className="text-4xl text-center mt-16 mb-10">            
            Análise do situação Financeira do Investidor
          </h1>

          {isLoading ? (
            <p className="text-xl text-center mt-16">Carregando perguntas...</p>
          ) : currentQuestion ? (
            <div className="my-10 w-full">
              <p className="text-xl flex items-center gap-2 font-bold mb-6">
                <span>{currentQuestionIndex + 1}</span>
                <span>-</span>
                <span>{currentQuestion.title}</span>
              </p>

              <div className="flex flex-col gap-4">
                {currentQuestion.answers.map((answer, index) => (
                  <button
                    key={answer.id}
                    onClick={() => handleAnswerClick(index)}
                    className="border border-blue-900 text-blue-900 text-xl hover:bg-blue-950 hover:text-white p-4 rounded-lg transition-colors disabled:opacity-50 disabled:cursor-not-allowed"
                    disabled={!user}
                  >
                    {answer.answer_text || answer.text}
                  </button>
                ))}
              </div>

              <p className="mt-6 text-gray-600">
                Pergunta {currentQuestionIndex + 1} de {questions.length}
              </p>
            </div>
          ) : null}
        </div>
      )}
    </div>
  );
};

export default QuizPage;