

  
// Interface para o perfil de investidor
interface PerfilInvestidor {
  id: number;
  minimo: number;
  maximo: number;
  nome?: string;
  descricao?: string;
  [key: string]: any; // Para outras propriedades que possam vir na resposta
}

// Interface para respostas de erro
interface ErrorResponse {
  status: number;
  message: string;
}


interface perfilInvestidorProps{
  PerfilId:number;
}

interface UserIdProps{
  UserId:number;
}


interface upatedPerfilInvestidorProps{

  PerfilId:number;
  data:{
    id: number;
    nome: string;
    descricao: string;
    objective: string;
    time_horizon: string;
    risk_tolerance: string
    preference: string;
    sentence: string;
    minimo: number;
    maximo: number;
    investidor: [ ]
  }
}

interface UpdatedSituationInvestidorProps{
  situationId:number;
  data:{
    id: number;
    nome: string;
    descricao: string;
    objective: string;
    time_horizon: string;
    risk_tolerance: string
    preference: string;
    sentence: string;
    minimo: number;
    maximo: number;
    investidor: [ ]
  }

}

interface SituationInvestidorProps
{
  situationId:number;
}

// Interfaces para tipagem
interface UpdateQuizParams {
  ValueId: number;
  userId: number;
}

interface getUserInfoProps {
  userId: string;
  // Adicione outros campos do usuário conforme necessário
}

interface QuizResponse {
  status: 'success' | 'error';
  data?: any;
  message?: string;
  timestamp?: string;
}

 interface UserIdProps{
  userId: number; 
 }


  interface UserStatusProps{
  userId: number;
  data: {
    id: number;
    email: string;
    is_active: boolean;
    situation: boolean;
    perfil: boolean;
    two_factor: boolean;
}
}

// Tipagem dos parâmetros e retorno
interface UpdateQuizParams {
    ValueId: string | number;
    userId: string | number;
  }
  
  interface UserInfo {
    id: number | string;
    // Adicione outras propriedades do usuário se necessário
  }
  
  interface QuizResponse {
    status: 'success' | 'error';
    data?: any;
    message?: string;
    timestamp: string;
  }
  

  
  interface Answer {
    id: number;
    text: string;
    answer_text?: string;
  }
  
  interface Question {
    id: number;
    title: string;
    answers: Answer[];
  }
  
  interface User {
    email: string;
  }