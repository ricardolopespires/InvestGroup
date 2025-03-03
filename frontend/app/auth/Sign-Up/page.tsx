"use client";

import * as React from "react";
import { Loader2, Eye, EyeOff } from "lucide-react"; // Importando os ícones de olho
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
import { toast } from "react-toastify";
import Image from "next/image";
import { useRouter } from "next/navigation";
import { signUp } from "@/lib/actions/actions.user";

const formSchema = z.object({
  email: z.string().email("Email é obrigatório"),
  first_name: z.string().min(5, "O nome é obrigatório"),
  last_name: z.string().min(5, "Sobrenome é obrigatório"),
  password: z.string().min(5, "Senha é obrigatória"),
  password2: z.string().min(5, "Confirmação é obrigatória"),
});

type FormValues = z.infer<typeof formSchema>;

const Page = () => {
  const [isLoading, setIsLoading] = useState(false);
  const [showPassword, setShowPassword] = useState(false); // Estado para controlar a visibilidade da senha
  const [showPassword2, setShowPassword2] = useState(false); // Estado para controlar a visibilidade da confirmação da senha

  const router = useRouter();

  const form = useForm<FormValues>({
    resolver: zodResolver(formSchema),
    defaultValues: {
      email: "",
      first_name: "",
      last_name: "",
      password: "",
      password2: "",
    },
  });

  const submit = async (data: FormValues) => {
    setIsLoading(true);

    const res = await signUp({ data });
    console.log(data);
    console.log(res);
    if (res.status === 201) {
      router.push("/auth/otp/verify");
      toast.success("Parabéns cadastro bem sucedido");
    } else if (res.status === 400) {
      toast.error(res.message);
      form.reset();
    } else {
      toast.error(res.message);
      form.reset();
    }
    setIsLoading(false);
  };

  return (
    <div className="flex w-full h-screen items-center justify-center">
      <Card className="w-[470px] h-[770px] rounded">
        <CardHeader>
          <CardTitle className="flex items-center justify-center mb-4 cursor-pointer">
            <a href="/">
              <Image src="/images/logo.png" width={160} height={160} alt="logotipo" />
            </a>
          </CardTitle>
          <CardDescription className="text-xs">
            Bem-vindo à nossa página de registro! Comece criando sua conta.
          </CardDescription>
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
                name="first_name"
                render={({ field }) => (
                  <FormItem>
                    <FormLabel className="text-xs font-semibold">Primeiro Nome</FormLabel>
                    <Input
                      id="first_name"
                      placeholder="Primeiro Nome"
                      className="text-xs"
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
                    <FormLabel className="text-xs font-semibold">Último Nome</FormLabel>
                    <Input
                      id="last_name"
                      placeholder="Último Nome"
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
                    <div className="relative">
                      <Input
                        type={showPassword ? "text" : "password"} // Altera para 'text' quando a senha é visível
                        id="password"
                        placeholder="Senha"
                        className="text-xs"
                        {...field}
                      />
                      <div
                        className="absolute right-2 top-1/2 transform -translate-y-1/2 cursor-pointer text-gray-400"
                        onClick={() => setShowPassword(!showPassword)} // Alterna o estado de visibilidade da senha
                      >
                        {showPassword ? (
                          <EyeOff size={20} /> // Ícone de olho fechado quando a senha está visível
                        ) : (
                          <Eye size={20} /> // Ícone de olho aberto quando a senha está oculta
                        )}
                      </div>
                    </div>
                    <FormMessage />
                  </FormItem>
                )}
              />
              <FormField
                control={form.control}
                name="password2"
                render={({ field }) => (
                  <FormItem>
                    <FormLabel className="text-xs font-semibold">Confirme a Senha</FormLabel>
                    <div className="relative">
                      <Input
                        type={showPassword2 ? "text" : "password"} // Altera para 'text' quando a confirmação da senha é visível
                        id="password2"
                        placeholder="Confirme a senha"
                        className="text-xs"
                        {...field}
                      />
                      <div
                        className="absolute right-2 top-1/2 transform -translate-y-1/2 cursor-pointer text-gray-400"
                        onClick={() => setShowPassword2(!showPassword2)} // Alterna o estado de visibilidade da confirmação da senha
                      >
                        {showPassword2 ? (
                          <EyeOff size={20} /> // Ícone de olho fechado para confirmação da senha
                        ) : (
                          <Eye size={20} /> // Ícone de olho aberto para confirmação da senha
                        )}
                      </div>
                    </div>
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
                      <Loader2 size={20} className="animate-spin" /> &nbsp; Enviando...
                    </>
                  ) : (
                    "Enviar os dados"
                  )}
                </Button>
              </div>
            </form>
          </Form>
        </CardContent>
        <CardFooter className="flex flex-col w-full">
          <div className="flex items-center w-full space-x-2 text-xs">
            <div className="signup-link">Você já é um membro?</div>
            <a className="text-indigo-700 hover:text-pink-700" href="/auth/Sign-In">
              Faça login
            </a>
          </div>
        </CardFooter>
      </Card>
    </div>
  );
};

export default Page;
