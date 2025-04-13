"use client";

import { zodResolver } from "@hookform/resolvers/zod";
import { useForm } from "react-hook-form";
import { z } from "zod";
import React from "react";
import { Button } from "@/components/ui/button";
import { Separator } from "@/components/ui/separator";
import {
  Card,
  CardContent,
  CardHeader,
  CardTitle,
  CardDescription,
} from "@/components/ui/card";
import { MdCurrencyExchange } from "react-icons/md";
import {
  Form,
  FormControl,
  FormField,
  FormItem,
  FormLabel,
  FormMessage,
} from "@/components/ui/form";
import {
  Select,
  SelectContent,
  SelectItem,
  SelectTrigger,
  SelectValue,
} from "@/components/ui/select";
import { cn } from "@/lib/utils";
import { Input } from "@/components/ui/input";

// Define the form schema with proper type coercion and validation
const formSchema = z.object({
  type: z.enum(["buy", "sell"], {
    errorMap: () => ({ message: "Tipo de operação inválido" }),
  }),
  operation: z.enum(["Market", "Sell Limit", "Buy Limit", "Sell Stop", "Buy Stop"], {
    errorMap: () => ({ message: "Tipo de operação inválido" }),
  }),
  amount: z
    .string()
    .min(1, { message: "Quantidade deve ser maior que 0" })
    .transform((val) => parseFloat(val)) // Convert string to number
    .refine((val) => !isNaN(val) && val > 0, {
      message: "Quantidade deve ser um número maior que 0",
    }),
  price: z
    .string()
    .optional()
    .transform((val) => (val ? parseFloat(val) : undefined)) // Convert to number if provided
    .refine((val) => val === undefined || (!isNaN(val) && val >= 0), {
      message: "Preço deve ser um número válido",
    }),
  takeprofit: z
    .string()
    .optional()
    .transform((val) => (val ? parseFloat(val) : undefined))
    .refine((val) => val === undefined || (!isNaN(val) && val >= 0), {
      message: "Take Profit deve ser um número válido",
    }),
  stoploss: z
    .string()
    .optional()
    .transform((val) => (val ? parseFloat(val) : undefined))
    .refine((val) => val === undefined || (!isNaN(val) && val >= 0), {
      message: "Stop Loss deve ser um número válido",
    }),
});

const CreatedOperations = ({ isVisible, onClose }) => {
  const [type, setType] = React.useState("buy");

  const form = useForm({
    resolver: zodResolver(formSchema),
    defaultValues: {
      type: "buy",
      operation: "",
      amount: "",
      price: "",
      takeprofit: "",
      stoploss: "",
    },
  });

  function onSubmit(values) {
    console.log(values);
    // Optionally reset form or close modal here
    // form.reset();
    // onClose();
  }

  if (!isVisible) return null;

  const handleClose = (e) => {
    if (e.target.id === "wrapper") onClose();
  };

  return (
    <div
      id="wrapper"
      onClick={handleClose}
      role="dialog"
      className="fixed inset-0 bg-black bg-opacity-25 flex justify-center items-center z-50"
    >
      <Card className="w-[450px] flex flex-col gap-1 p-4 bg-white shadow-lg rounded-lg">
        <CardHeader>
          <CardTitle className="flex gap-2 text-xl items-center justify-start">
            <MdCurrencyExchange className="text-lg" />
            <span>Nova Operação</span>
          </CardTitle>
          <CardDescription>Abrir uma nova operação</CardDescription>
          <Separator />
        </CardHeader>

        <CardContent>
          <Form {...form}>
            <form onSubmit={form.handleSubmit(onSubmit)} className="space-y-4">
              {/* Type Selection */}
              <div className="flex items-center justify-between text-xs gap-1 bg-slate-100 rounded-md p-1.5">
                <button
                  type="button"
                  className={cn(
                    "w-[49%] h-7 rounded-l-sm",
                    type === "buy" ? "bg-green-500 text-white" : "text-slate-600"
                  )}
                  onClick={() => {
                    setType("buy");
                    form.setValue("type", "buy"); // Sync with form state
                  }}
                >
                  Compra
                </button>
                <button
                  type="button"
                  className={cn(
                    "w-[49%] h-7 rounded-r-sm",
                    type === "sell" ? "bg-red-500 text-white" : "text-slate-600"
                  )}
                  onClick={() => {
                    setType("sell");
                    form.setValue("type", "sell"); // Sync with form state
                  }}
                >
                  Venda
                </button>
              </div>

              {/* Operation Type */}
              <FormField
                control={form.control}
                name="operation"
                render={({ field }) => (
                  <FormItem>
                    <FormLabel>Tipo de Operação</FormLabel>
                    <Select onValueChange={field.onChange} defaultValue={field.value}>
                      <FormControl>
                        <SelectTrigger>
                          <SelectValue placeholder="Selecione o tipo de operação" />
                        </SelectTrigger>
                      </FormControl>
                      <SelectContent>
                        <SelectItem value="Market">Market</SelectItem>
                        <SelectItem value="Sell Limit">Sell Limit</SelectItem>
                        <SelectItem value="Buy Limit">Buy Limit</SelectItem>
                        <SelectItem value="Sell Stop">Sell Stop</SelectItem>
                        <SelectItem value="Buy Stop">Buy Stop</SelectItem>
                      </SelectContent>
                    </Select>
                    <FormMessage />
                  </FormItem>
                )}
              />

              {/* Amount */}
              <FormField
                control={form.control}
                name="amount"
                render={({ field }) => (
                  <FormItem>
                    <FormLabel>Lote</FormLabel>
                    <FormControl>
                      <Input placeholder="0.0" type="number" step="0.1" {...field} />
                    </FormControl>
                    <FormMessage />
                  </FormItem>
                )}
              />

              {/* Price */}
              <FormField
                control={form.control}
                name="price"
                render={({ field }) => (
                  <FormItem>
                    <FormLabel>Preço</FormLabel>
                    <FormControl>
                      <Input placeholder="0" type="number" step="0.01" {...field} />
                    </FormControl>
                    <FormMessage />
                  </FormItem>
                )}
              />

              {/* Take Profit */}
              <FormField
                control={form.control}
                name="takeprofit"
                render={({ field }) => (
                  <FormItem>
                    <FormLabel>Take Profit</FormLabel>
                    <FormControl>
                      <Input placeholder="0" type="number" step="0.01" {...field} />
                    </FormControl>
                    <FormMessage />
                  </FormItem>
                )}
              />

              {/* Stop Loss */}
              <FormField
                control={form.control}
                name="stoploss"
                render={({ field }) => (
                  <FormItem>
                    <FormLabel>Stop Loss</FormLabel>
                    <FormControl>
                      <Input placeholder="0" type="number" step="0.01" {...field} />
                    </FormControl>
                    <FormMessage />
                  </FormItem>
                )}
              />

              {/* Submit Button */}
              <div className="flex justify-end gap-2">
                <Button type="submit">Adicionar</Button>
              </div>
            </form>
          </Form>
        </CardContent>
      </Card>
    </div>
  );
};

export default CreatedOperations;