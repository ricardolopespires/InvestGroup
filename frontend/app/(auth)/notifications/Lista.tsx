import {
  Card,
  CardContent,
  CardDescription,
  CardFooter,
  CardHeader,
  CardTitle,
} from "@/components/ui/card";
import React from 'react';
import { ScrollArea } from "@/components/ui/scroll-area"
import { Separator } from "@/components/ui/separator"


const Lista = ({ isVisible, onClose }) => {
  if (!isVisible) return null;

  const handleClose = (e) => {
      if (e.target.id === "wrapper") onClose();
  };




  return (
      <div
          id="wrapper"
          className="fixed inset-0 flex items-start justify-end p-4 right-[205px] top-10 absolute"
          onClick={handleClose}
      >
          <Card className="w-[350px] h-[240px] bg-white shadow-lg">
              <CardHeader>
                  <CardTitle>Notificações</CardTitle>                 
              </CardHeader>
              <CardContent>
              <ScrollArea className="h-90 w-full">
  
              </ScrollArea>
              </CardContent>
          </Card>
      </div>
  );
};

export default Lista;
