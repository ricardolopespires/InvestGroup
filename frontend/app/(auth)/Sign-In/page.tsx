"use client";

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
} from "@/components/ui/card";
import {
  Form,
  FormField,
  FormItem,
  FormLabel,
  FormMessage,
} from "@/components/ui/form";
import { Input } from "@/components/ui/input";
import { useState } from "react";
import { useForm } from "react-hook-form";
import Navbar from "@/components/home/navbar";
import { toast } from "react-toastify";

import Image from "next/image";
import { useRouter } from "next/navigation";
import { SignIn } from "@/lib/atcions/actions.user";

const formSchema = z.object({
  email: z.string().email("Email é obrigatório"),
  password: z.string().min(5, "Senha é obrigatória"),

});

type FormValues = z.infer<typeof formSchema>;

const Page = () => {
  const [isLoading, setIsLoading] = useState(false);

  const  router  = useRouter();

  const form = useForm<FormValues>({
    resolver: zodResolver(formSchema),
    defaultValues: {
      email: "",   
      password: "",
    
    },
  });


  
  const submit = async (data: FormValues) => {
    setIsLoading(true);
  
      const res = await SignIn({ data:data });
      
      console.log(res);
      // Simulate API submission or other async tasks
      if (res.status === 200) {
        await router.push('/dashboard/overview')
        toast.success("Parabéns Login sucedido")           
      }else if(res.status === 400){
        toast.error(res.message)
        form.reset();
      }else{
        toast.error(res.message)
        form.reset();
      }
      // After successful submission
      setIsLoading(false)
  };
  return (
    <div className="flex w-full h-screen inset-0 items-center justify-center">
        <Card className="w-[400px] h-[490px] rounded">
            <CardHeader>
                <CardTitle className='flex items-center justify-center mb-4 cursor-pointer'>
                    <a href="/">
                    <Image src={"/images/logo.png"} width={160} height={160} alt='logotipo'/>
                    </a>
                </CardTitle>
                <CardDescription>Digite seu e-mail e senha para acessar sua conta..</CardDescription>
            </CardHeader>
            <CardContent>
            <Form {...form}>
            <form onSubmit={form.handleSubmit(submit)} className="space-y-6 mt-4">
              <FormField
                control={form.control}
                name="email"
                render={({ field }) => (
                  <FormItem>
                    <FormLabel className="text-xs font-semibold">Email</FormLabel>
                    <Input
                      id="email"
                      placeholder="Digite o seu email"
                      className="text-xs"
                      {...field}
                    />
                    <FormMessage />
                  </FormItem>
                )}
              />
              <FormField
                control={form.control}
                name="password"
                render={({ field }) => (
                  <FormItem>
                    <FormLabel className="text-xs font-semibold">Senha</FormLabel>
                    <Input
                      type="password"
                      id="password"
                      placeholder="Senha"
                      className="text-xs focus:outline-none"
                      {...field}
                    />
                    <FormMessage />
                  </FormItem>
                )}
              />
                      <div className="grid w-full items-center gap-1.5">
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
                    "Entrar"
                  )}
                </Button>
              </div>
                </form>
              </Form>
             
            </CardContent>
            <CardFooter className="mt-4 flex flex-col space-y-4 w-full">
       
            <div className="flex items-center justify-between w-full text-xs">
                <a className="text-indigo-700 hover:text-pink-700 float-left" href="/Forgot"><span className="text-gray-400">Esqueceu sua</span> senha?</a>
                <a className="text-indigo-700 hover:text-pink-700 float-right" href="/Sign-Up">Criar uma conta</a>
            </div>
            </CardFooter>
        </Card>
      
    </div>
  )
}

export default Page

