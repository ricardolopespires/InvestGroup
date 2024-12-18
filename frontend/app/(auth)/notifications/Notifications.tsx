import React, { useState } from 'react';
import { FaRegBell } from 'react-icons/fa';
import {
  Popover,
  PopoverContent,
  PopoverTrigger,
} from '@/components/ui/popover';
import { Separator } from "@/components/ui/separator"

const Notifications = () => {
  // Inicializa o estado como um array vazio, indicando que não há notificações.
  const [notifications, setNotifications] = useState([]);
  const [showModal, setShowModal] = useState(false);

  return (
    <Popover>
      <PopoverTrigger asChild>
        <div className="relative flex items-center cursor-pointer" onClick={() => setShowModal(true)}>
          {/* Verifica se há notificações */}
          {notifications.length > 0 && (
            <div className="absolute top-0 right-0 w-2 h-2 bg-red-500 rounded-full animate-ping"></div>
          )}
          {/* Ícone de notificação */}
          <FaRegBell className={`text-2xl ${notifications.length > 0 ? 'text-gray-500' : 'text-gray-400'}`} />
        </div>
      </PopoverTrigger>
      <PopoverContent className="w-80 bg-white h-[400px]">
        <div className="grid gap-4">
          <div className="space-y-2 ">
            <h1 className="text-xl font-semibold ">Notificações</h1>
            <hr />           
            <p className="text-xs text-muted-foreground">
              Você tem {notifications.length} novas notificações..
            </p>
          </div>
          <div className='w-full h-full'>              
              {notifications.length === 0 ? (
                <p className="flex items-center justify-center text-sm text-muted-foreground mt-40">
                  Nenhuma nova notificação  
                </p>
              ) : (
                <ul className="space-y-2">
                  {notifications.map((notification, index) => (
                    <li key={index} className="p-2 bg-gray-100 rounded">
                      {notification.message}
                    </li>
                  ))}
                </ul>
              )}
          </div>
        </div>
      </PopoverContent>
    </Popover>
  );
};

export default Notifications;
