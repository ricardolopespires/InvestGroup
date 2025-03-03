"use client"
import AxiosInstance from '@/services/AxiosInstance';
import { useParams, useRouter } from 'next/navigation';
import React, { useState } from 'react'
import { zodResolver } from "@hookform/resolvers/zod";
import * as z from "zod";
import { useForm, Controller } from "react-hook-form";
import { toast } from 'react-toastify';


import {
  Card,
  CardContent,
  CardDescription,
  CardFooter,
  CardHeader,
  CardTitle,
} from "@/components/ui/card"
import { Button } from '@/components/ui/button';
import { Input } from '@/components/ui/input'; // Importando o Input, caso não tenha sido importado
import { Loader2 } from 'lucide-react';

// Definindo o schema de validação com Zod
const formSchema = z.object({
  password: z.string().min(8, "A senha deve ter pelo menos 8 caracteres"),
  confirm_password: z.string().min(8, "A confirmação de senha deve ter pelo menos 8 caracteres"),
}).refine(data => data.password === data.confirm_password, {
  message: "As senhas não coincidem",
  path: ["confirm_password"]
});

type FormValues = z.infer<typeof formSchema>;

const ResetPassword = () => {

  const [isLoading, setIsLoading] = useState(false);
  const navigate = useRouter(); 
  
  const { uidb64, token } = useParams();



  const {
    control,
    handleSubmit,
    formState: { errors }
  } = useForm<FormValues>({
    resolver: zodResolver(formSchema)
  });

  const submit = async (data: FormValues) => {
    setIsLoading(true);

    try {
      // Adicionando o uid e token ao corpo da requisição
      const formData = { ...data, uidb64, token };

      console.log(formData);

      // Fazendo a requisição para redefinir a senha com os dados do formulário
      const res = await AxiosInstance.patch('/api/v1/auth/set-new-password/', formData);
      if (res.status === 200) {
        toast.success("Senha redefinida com sucesso!");
        navigate.push("/Sign-In"); // Redirecionar para a página de login após sucesso
      } else {
        toast.error("Não foi possível redefinir a senha.");
      }
    } catch (error) {
      toast.error("Erro ao redefinir a senha.");
    }
    setIsLoading(false);
  }

  return (
    <div className="flex w-full h-screen items-center justify-center">
      <Card className="w-[499px]">
        <CardHeader>
          <CardTitle className="text-2xl">Redefinir Senha</CardTitle>
          <CardDescription>Insira os dados abaixo para redefinir sua senha.</CardDescription>
        </CardHeader>
        <CardContent>
          <form onSubmit={handleSubmit(submit)} className="space-y-6">
            <div>
              <label htmlFor="password" className="block">Nova Senha</label>
              <Controller
                name="password"
                control={control}
                render={({ field }) => (
                  <Input
                    type="password"
                    id="password"
                    placeholder="Digite sua nova senha"
                    {...field}
                    className="w-full"
                  />
                )}
              />
              {errors.password && <p className="text-red-500">{errors.password.message}</p>}
            </div>

            <div>
              <label htmlFor="confirm_password" className="block">Confirmar Senha</label>
              <Controller
                name="confirm_password"
                control={control}
                render={({ field }) => (
                  <Input
                    type="password"
                    id="confirm_password"
                    placeholder="Confirme sua nova senha"
                    {...field}
                    className="w-full"
                  />
                )}
              />
              {errors.confirm_password && <p className="text-red-500">{errors.confirm_password.message}</p>}
            </div>

            <CardFooter>
              <div className="w-full items-center gap-1.5">
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
                    "Redefinir Senha"
                  )}
                </Button>
              </div>
            </CardFooter>
          </form>
        </CardContent>
      </Card>
    </div>
  )
}

export default ResetPassword;
