





import React from 'react'

 
import { Button } from "@/components/ui/button"
import {
  Card,
  CardContent,
  CardDescription,
  CardFooter,
  CardHeader,
  CardTitle,
} from "@/components/ui/card"
import { SiMarketo } from 'react-icons/si';

const AddStock = ({isVisible, onClose}) => {

    if(!isVisible) return null;

    const handleClose = (e) => {
        if(e.target.id === "wrapper") onClose();
    }


  return (
       <div id='wrapper' onClick={handleClose} role='dialog' className='fixed inset-0 bg-black bg-opacity-25 back  flex justify-center items-center'>
        <Card className="w-[450px]">
            <CardHeader className='flex flex-col gap-2'>
                <CardTitle className='flex  gap-2 text-xl'>
                    <SiMarketo className='text-amber-400'/>
                    <span className=''>Ações</span>
                </CardTitle>
                
                <CardDescription>Adicionar uma nova ação para acompanhar.</CardDescription>
                <span className='border'/>
            </CardHeader>
            <CardContent>

            </CardContent>
        </Card>

    </div>
  )
}

export default AddStock