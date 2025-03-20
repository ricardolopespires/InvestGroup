


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
import { FaSitemap } from 'react-icons/fa6';

const ApiMetaTrader = ({isVisible, onClose}) => {

    if(!isVisible) return null;

    const handleClose = (e) => {
        if(e.target.id === "wrapper") onClose();
    }
    
  return (
    <div id='wrapper' onClick={handleClose} role='dialog' className='fixed inset-0 bg-black bg-opacity-25 back  flex justify-center items-center'>
        <Card className="w-[450px]">
            <CardHeader>
                <CardTitle className='flex items-center gap-2'>
                <img className="h-10 w-10 rounded-full object-cover" src="https://smarttbot.com/wp-content/uploads/2020/01/logo-mt5.png" alt="profile" />
                    <span>MetaTrader</span>
                </CardTitle>
                <CardDescription>Adicionar uma nova Conta MetaTrader.</CardDescription>
            </CardHeader>
            <CardContent>

            </CardContent>
        </Card>

    </div>
  )
}

export default ApiMetaTrader

