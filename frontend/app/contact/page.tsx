"use client" 

import * as React from "react";
import { Loader2 } from "lucide-react";
import { Button } from "@/components/ui/button";
import { zodResolver } from "@hookform/resolvers/zod";
import * as z from "zod";
import { useForm } from "react-hook-form";
import {
  Card,
  CardContent,
} from "@/components/ui/card";
import { Input } from "@/components/ui/input";
import { Textarea } from "@/components/ui/textarea";
import {
  Form,
  FormField,
  FormItem,
  FormLabel,
  FormMessage,
} from "@/components/ui/form";
const formaSchema = z.object({
  first_name: z.string().min(5, "O nome é obrigatório"),
  last_name: z.string().min(5, "Sobrenome é obrigatório"),
  email: z.string().email("Email é obrigatório"),
  message: z.string().min(5, "Mensagem é obrigatória"),
});

type FormValues = z.infer<typeof formaSchema>;



import Responsive from '@/components/home/Responsive'
import { toast } from "react-toastify";
import { createMassage } from "@/lib/atcions/actions.contact";


const page = () => {

  const [isLoading, setIsLoading] = React.useState(false);

  const form = useForm<FormValues>({
    resolver: zodResolver(formaSchema),
    defaultValues: {
      first_name: "",
      last_name: "",
      email: "",
      message: "",
    },
  });

  const submit = async (data: FormValues) => {
    setIsLoading(true);
    
    try {
      // Simulate API submission or other async tasks

      const res = await createMassage({data:data})

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
  // Add your page content here, for example:
  <div className="">
        <Responsive/>
        <div className="flex items-center justify-center h-full ">
        <Card className="mt-40">
          <CardContent>
            <div className="bg-gray-900 p-10 text-white rounded">
              <p className="mt-4 text-sm leading-7 font-regular uppercase">
                Contato
              </p>
              <h3 className="text-3xl sm:text-4xl leading-normal font-extrabold tracking-tight">
                Entrar em <span className="text-indigo-600">contato</span>
              </h3>
              <p className="mt-4 leading-7 text-gray-200">
                Fique à vontade para entrar em contato conosco. Estamos sempre
                abertos para discutir novos projetos, ideias criativas ou
                oportunidades de fazer parte de suas visões.
              </p>
            </div>
          
          <Form {...form}>
              <form onSubmit={form.handleSubmit(submit)} className="p-10">
                <div className="space-y-4">
                  <div className="grid grid-cols-2 gap-4">
                    <FormField
                      control={form.control}
                      name="first_name"
                      render={({ field }) => (
                        <FormItem>
                          <FormLabel>Primeiro Nome</FormLabel>
                          <Input
                            id="first_name"
                            placeholder="Primeiro Nome"
                            {...field}
                          />
                          <FormMessage />
                        </FormItem>
                      )}
                    />
                    <FormField
                      control={form.control}
                      name="last_name"
                      render={({ field }) => (
                        <FormItem>
                          <FormLabel>Último Nome</FormLabel>
                          <Input
                            id="last_name"
                            placeholder="Último Nome"
                            {...field}
                          />
                          <FormMessage />
                        </FormItem>
                      )}
                    />
                  </div>
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
                  <FormField
                    control={form.control}
                    name="message"
                    render={({ field }) => (
                      <FormItem>
                        <FormLabel>Mensagem</FormLabel>
                        <Textarea
                          id="message"
                          className="h-[160px]"
                          placeholder="Digite a sua mensagem"
                          {...field}
                        />
                        <FormMessage />
                      </FormItem>
                    )}
                  />
                  <div className="grid w-full items-center gap-1.5">
                    <Button
                      type="submit"
                      className="w-60 text-sm text-white bg-gradient-to-r from-[#0B2353] to-[#364FCE]"
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
                </div>
              </form>
            </Form>
          </CardContent>
          </Card>

          </div>
      
  </div>
  )
}

export default page
