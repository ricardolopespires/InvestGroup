"use client";

import React, { useEffect, useState } from "react";
import { motion } from "framer-motion";
import { cn } from "@/lib/utils";
import { getDetailAdvisors,  patchIsActiveAdvisors } from "@/lib/actions/actions.advisors";

interface IsActiveRoboProps {
  AdvisorId: string;
}


const IsActiveBalancing = ({AdvisorId}) => {
      const [toggle, setToggle] = useState<boolean>(false);
      const [loading, setLoading] = useState<boolean>(false);
    
      useEffect(() => {
        const fetchData = async () => {
          const res = await getDetailAdvisors({ AdvisorId: AdvisorId });    
          setToggle(res?.is_active);
        };
        fetchData();
      }, [AdvisorId]);
    
      const handleToggle = async () => {
        try {
          setLoading(true);
          const newState = !toggle;
          await patchIsActiveAdvisors({
            AdvisorId: AdvisorId,
            data: { is_active: newState },
          });
          setToggle(newState);
        } catch (error) {
          console.error("Erro ao atualizar status do robô:", error);
        } finally {
          setLoading(false);
        }
      };
  return (
       <div
          className={cn(
            "flex h-6 w-12 cursor-pointer rounded-full p-[1px] border has-tooltip transition-opacity",
            toggle ? "bg-green-700 justify-end border-green-700" : "bg-white justify-start",
            loading && "opacity-50 pointer-events-none"
          )}
          onClick={handleToggle}
        >
          <motion.div
            className={cn("h-5 w-5 rounded-full", toggle ? "bg-white" : "bg-blue-950")}
            layout
            transition={{ type: "spring", stiffness: 100, duration: 0.2 }}
          />
          <span
            className={cn(
              "tooltip rounded shadow-lg py-2 px-4 bg-gray-100 -mt-11 text-xs",
              toggle ? "text-green-600" : "text-red-600"
            )}
          >
            {toggle ? "Ativado" : "Desativado"}
          </span>
        </div>
  )
}

export default IsActiveBalancing