"use client"

import React, { useState } from 'react'
import { zodResolver } from "@hookform/resolvers/zod"
import { Loader2 } from "lucide-react";
import { useForm } from "react-hook-form"
import { z } from "zod"
import { Button } from "@/components/ui/button"
import {
  Form,
  FormControl,
  FormDescription,
  FormField,
  FormItem,
  FormLabel,
  FormMessage,
} from "@/components/ui/form"
import { Input } from "@/components/ui/input"
import { postSubscribed } from '@/lib/actions/actions.newsletter'
import { toast } from 'react-toastify'

// Definindo o esquema de validação com Zod
const formSchema = z.object({
  email: z.string().min(2, ).email({
    message: "Por favor, insira um endereço de e-mail válido.",
  }),
})


type FormValues = z.infer<typeof formaSchema>;

const Newsletter = () => {

  const [isLoading, setIsLoading] = useState(false);


  // Definindo o formulário com react-hook-form e Zod
  const form = useForm<z.infer<typeof formSchema>>({
    resolver: zodResolver(formSchema),
    defaultValues: {
      email: "",
    },
  })

  
  const submit = async (data: FormValues) => {
    setIsLoading(true);
    
    try {
      // Simulação de envio (você pode integrar uma API aqui)

      const res = await postSubscribed({EmailData:data})
      
      // Simulação de sucesso
      setTimeout(() => {
     
        form.reset() // Limpa o formulário após envio
      }, 1000)

      if(res.status === 201) {
        toast.success(res.message)
      }else{
        toast.error(res.message)
      }
      // After successful submission
      form.reset();
    } catch (err) {
      toast.error("Dados incorretos")

    } finally {
      setIsLoading(false);
    }
  };


  return (
    <div className="pb-20 pt-20">
      <div className="grid grid-cols-1 lg:grid-cols-2 gap-6">
        <div className="flex flex-col items-center justify-center gap-4">
          <h2 className="text-4xl text-center">Quer ficar informado?</h2>
          <p className="w-[80%] lg:w-[60%] text-center">
            Inscreva-se na newsletter para receber as postagens antes de todo mundo.
            Enviaremos um e-mail com links para todos os artigos.
          </p>
        </div>
        <div className="flex w-full h-full">
          <Form {...form}>
            <form
              onSubmit={form.handleSubmit(submit)}
              className="w-full flex items-center gap-1 max-w-xl "
            >
              <FormField
                control={form.control}
                name="email"
                render={({ field }) => (
                  <FormItem className='w-full'>
                    <FormControl>
                      <Input
                        id="email"
                        placeholder="Digite seu e-mail"
                        {...field}
                        className="w-full rounded-r"
                      />
                    </FormControl>                  
                    {/* Exibindo mensagens de erro */}
                    <FormMessage />
                  </FormItem>
                )}
              />
                   <Button
                      type="submit"
                      className="w-40 text-sm text-white rounded-l bg-gradient-to-r from-[#0B2353] to-[#364FCE]"
                      disabled={isLoading}
                    >
                      {isLoading ? (
                        <>
                          <Loader2 size={20} className="animate-spin" />{" "}
                          &nbsp; Enviando...
                        </>
                      ) : (
                        "inscrever-se"
                      )}
                    </Button>
            </form>
          </Form>
        </div>
      </div>
    </div>
  )
}

export default Newsletter
