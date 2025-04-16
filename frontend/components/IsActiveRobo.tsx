"use client"
 

import { motion } from "framer-motion"
import { zodResolver } from "@hookform/resolvers/zod"
import { Switch } from "@/components/ui/switch"
import { useForm } from "react-hook-form"
import { z } from "zod"
 
import {
    Form,
    FormControl,
    FormDescription,
    FormField,
    FormItem,
    FormLabel,
  } from "@/components/ui/form"


 
  const FormSchema = z.object({
    is_active: z.boolean().default(false).optional(),
    
  })
   



import React, { useState } from 'react'
import { cn } from "@/lib/utils"

const IsActiveRobo = ({roboId}) => {
    const[toggle, setToggle] = useState<boolean>(false)



  return (
    <div className={cn("flex h-6 w-12 cursor-pointer rounded-full p-[1px] border has-tooltip",
        toggle === false ? "bg-white justify-start":"bg-green-400 justify-end border-green-400 
    )}
    onClick={() => setToggle(!toggle)}>    
        <motion.div className={cn("h-5 w-5 rounded-full", toggle === false ? "bg-blue-950":"bg-white")}
        layout
        transition={{type: "spring", stiffness: 100, duration: 0.2}}/>
         <span className={cn("tooltip rounded shadow-lg py-2 px-4 bg-gray-100 -mt-11 text-xs",
            toggle === false ? "text-red-600":"text-green-600"
         )}>
            {toggle === false ? "Desativado" : "Ativado"}
         </span>
    </div>
  )
}

export default IsActiveRobo