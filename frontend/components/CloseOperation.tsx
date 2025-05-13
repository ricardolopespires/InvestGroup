import { postCloseOperations } from "@/lib/actions/actions.operations";
import { IoClose } from "react-icons/io5";
import { toast } from "react-toastify";


const CloseOperation = ({ticket}) => {


  const user = JSON.parse(localStorage.getItem('user'))


    const handleClick = async (e: React.MouseEvent<HTMLButtonElement>) => {
      e.preventDefault(); // Prevent default button behavior if needed
      if (ticket) {
        // Call the function to handle the operation with the ticket
        const res = await postCloseOperations({ticket:ticket, UserId:user.email});      
        if(res.status === 200){
        toast.success("Operação fechada com sucesso!")
    
        }else{
          toast.error("Erro ao fechar operação!")
        }
      }
    };

  return (
    <div>
       <button 
       className="bg-red-500 text-white h-6 w-6 rounded-sm text-lg flex items-center justify-center"
       onClick={handleClick}
       ><IoClose /></button>
    </div>
  );
};


// You can add your logic here to handle closing operations, such as fetching data, handling user input, etc.
export default CloseOperation;




