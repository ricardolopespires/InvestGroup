"use client"
import * as React from "react";
import { Loader2 } from "lucide-react";
import { Button } from "@/components/ui/button";
import { zodResolver } from "@hookform/resolvers/zod";
import * as z from "zod";

import {
    Card,
    CardContent,
    CardDescription,
    CardFooter,
    CardHeader,
    CardTitle,
  } from "@/components/ui/card"
import { Input } from "@/components/ui/input"
import { Label } from "@radix-ui/react-label"
import Image from "next/image"

import {
  Form,
  FormField,
  FormItem,
  FormLabel,
  FormMessage,
} from "@/components/ui/form";
import { useState } from "react";
import { useForm } from "react-hook-form";
import { toast } from "react-toastify";
import { userResetPassword } from "@/lib/actions/actions.user";



const formSchema = z.object({
  email: z.string().email("Email é obrigatório"),
})


type FormValues = z.infer<typeof formSchema>



const Page = () => {
  const [isLoading, setIsLoading] = useState(false);

  const form = useForm<FormValues>({
    resolver:zodResolver(formSchema),
    defaultValues: {
      email:"",
    },
  });

  const submit = async (data:FormValues)=>{
    setIsLoading(true); 

    try{
      const res = await userResetPassword({data})
      
      console.log(res.status);     
      if (res.status === 200){
        toast.success("Um link para redefinir sua senha foi enviado para seu email")
        form.reset()
      }else{
        toast.error("Não foi possível enviar o email")
        form.reset()
      }

    }catch{
      toast.error("As informações estão erradas")
    }
    setIsLoading(false);
  };
  return (
    <div className="flex w-full h-screen inset-0 items-center justify-center">      
        <Card className="w-[520px] h-[360px] rounded ">
            <CardHeader className="flex flex items-center justify-center ">
                <CardTitle className='flex flex-col items-center justify-center gap-4 cursor-pointer'>
                <a href="/">
                  <img src={'/images/logo.png'} alt="logo" className="w-40" />
                </a>
                <span>Esqueceu sua senha?</span>
                </CardTitle>
                <CardDescription className="text-xs flex flex-col ">
                  <span>Digite seu endereço de e-mail, enviaremos um link para redefinir sua senha!</span>             
                </CardDescription>
            </CardHeader>
            <CardContent>
            <Form {...form}>
              <form onSubmit={form.handleSubmit(submit)}  className="space-y-6">
              <FormField
                    control={form.control}
                    name="email"
                    render={({ field }) => (
                      <FormItem>
                        <FormLabel>Email</FormLabel>
                        <Input
                          id="email"
                          placeholder="Digite o seu email"
                          {...field}
                        />
                        <FormMessage />
                      </FormItem>
                    )}
                  />
                  <div className=" w-full items-center gap-1.5">
                    <Button
                      type="submit"
                      className="w-full text-sm text-white bg-gradient-to-r from-[#0B2353] to-[#364FCE]"
                      disabled={isLoading}
                    >
                      {isLoading ? (
                        <>
                          <Loader2 size={20} className="animate-spin" />{" "}
                          &nbsp; Enviando...
                        </>
                      ) : (
                        "Enviar os dados"
                      )}
                    </Button>
              </div>          
              </form>
            </Form>
            </CardContent>
            <CardFooter className=" flex flex-col space-y-4 w-full">           
              <div className="flex items-center justify-between w-full text-xs">
                  <a className="text-indigo-700 hover:text-pink-700 float-left" href="/auth/Sign-In"><span className="text-gray-400">Lembrou a senha?</span> login </a>                
              </div>
            </CardFooter>
        </Card>
      
    </div>
  )
}

export default Page
