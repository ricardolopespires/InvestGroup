"use client";

import Logout from "@/app/auth/Logout/page";
import { quizSituation } from "@/lib/actions/actions.quiz";
import { useEffect, useState } from "react";

interface Answer {
    id: number;
    text: string;
}

interface Question {
    id: number;
    title: string;
    answers: Answer[];
}

const Page = () => {
    const [questions, setQuestions] = useState<Question[]>([]);
    const [currentQuestionIndex, setCurrentQuestionIndex] = useState(0);
    const [selectedAnswers, setSelectedAnswers] = useState<number[]>([]);

    useEffect(() => {
        const fetchData = async () => {
            try {
                const res = await quizSituation();
                if (res && Array.isArray(res.questions)) {
                    setQuestions(res.questions);
                } else {
                    console.error("Erro: Estrutura de resposta inesperada", res);
                }
            } catch (error) {
                console.error("Erro ao buscar o quiz:", error);
            }
        };

        fetchData();
    }, []);

    const handleAnswerClick = (answerId: number) => {
        // Armazena a resposta selecionada
        setSelectedAnswers([...selectedAnswers, answerId]);

        
        // Vai para a próxima questão ou finaliza
        if (currentQuestionIndex < questions.length - 1) {
            setCurrentQuestionIndex(currentQuestionIndex + 1);
        } else {
            console.log("Quiz concluído! Respostas:", [...selectedAnswers, answerId]);
            // Aqui você pode adicionar lógica para quando o quiz terminar
        }
    };

    const currentQuestion = questions[currentQuestionIndex];

    return (
        <div className="w-full h-full flex flex-col items-center justify-center">
            <header className="w-full h-20 flex items-center shadow-md justify-between">
                <div className="container flex items-center w-full gap-4">
                    <img src="/images/logo.png" alt="Logo-white" className="h-12 ml-4" />
                </div>
                <div className="text-2xl mr-9">
                    <Logout />
                </div>
            </header>

            <h1 className="text-4xl text-center mt-16 mb-10">Análise do situação Financeira do Investidor</h1>
            <div className="container flex flex-col mt-16 mb-10">
                {questions.length > 0 && currentQuestion ? (
                    <div className="mb-8">
                        <p className="text-xl flex items-center gap-2 font-bold">
                            <span>{currentQuestionIndex + 1}</span>
                            <span>-</span>
                            <span>{currentQuestion.title}</span>
                        </p>

                        <div className="flex flex-col gap-4 mt-4 w-full justify-center">
                            {currentQuestion.answers.map((answer) => (
                                <button
                                    key={answer.id}
                                    onClick={() => handleAnswerClick(answer.id)}
                                    className="border border-blue-900 text-blue-900 text-xl hover:bg-blue-950 hover:text-white p-4 rounded-lg transition-colors"
                                >
                                    {answer.answer_text}
                                </button>
                            ))}
                        </div>

                        <p className="mt-4 text-gray-600">
                            Pergunta {currentQuestionIndex + 1} de {questions.length}
                        </p>
                    </div>
                ) : (
                    <p className="text-xl text-center">Carregando perguntas...</p>
                )}
            </div>
        </div>
    );
};

export default Page;