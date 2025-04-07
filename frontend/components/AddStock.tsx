"use client"

import { zodResolver } from "@hookform/resolvers/zod"
import { useForm } from "react-hook-form"
import { z } from "zod"
import React from 'react'
import { Button } from "@/components/ui/button"
import {
  Card,
  CardContent,
  CardHeader,
  CardTitle,
  CardDescription,
} from "@/components/ui/card"
import { SiMarketo } from 'react-icons/si'
import {
  Form,
  FormControl,
  FormDescription,
  FormField,
  FormItem,
  FormLabel,
  FormMessage,
} from "@/components/ui/form"
import SelectedStock from "@/components/SelectedStock"

const formSchema = z.object({
  name: z.string().min(2, {
    message: "Username must be at least 2 characters.",
  }),
})

const AddStock = ({ isVisible, onClose }) => {
  const form = useForm({
    resolver: zodResolver(formSchema),
    defaultValues: {
      name: "",
    },
  })

  function onSubmit(values) {
    console.log(values)
  }

  if (!isVisible) return null;

  const handleClose = (e) => {
    if (e.target.id === "wrapper") onClose();
  }

  return (
    <div 
      id='wrapper' 
      onClick={handleClose} 
      role='dialog' 
      className='fixed inset-0 bg-black bg-opacity-25 flex justify-center items-center'
    >
      <Card className="w-[450px] flex flex-col gap-4 p-4 bg-white shadow-lg rounded-lg justify-start">
        <CardHeader className='flex flex-col gap-2'>
          <CardTitle className='flex gap-2 text-xl justify-start'>
            <SiMarketo className='text-amber-400'/>
            <span>Ações</span>
          </CardTitle>
          <CardDescription className="text-left">
            Adicionar uma nova ação para acompanhar.
          </CardDescription>
          <span className='border w-full'/>
        </CardHeader>
        <CardContent>
          <Form {...form}>
            <form onSubmit={form.handleSubmit(onSubmit)} className="space-y-8">
              <FormField
                control={form.control}
                name="name"
                render={({ field }) => (
                  <FormItem className="flex flex-col items-start">
                    <FormLabel className="text-left">Selecione a Ação</FormLabel>
                    <FormControl>
                      <SelectedStock 
                        onValueChange={field.onChange}
                        value={field.value}
                      />
                    </FormControl>
                    <FormMessage className="text-left" />
                  </FormItem>
                )}
              />
              <div className="flex justify-end gap-2">              
                <Button type="submit">Adicionar</Button>
              </div>
            </form>
          </Form>
        </CardContent>
      </Card>
    </div>
  )
}

export default AddStock