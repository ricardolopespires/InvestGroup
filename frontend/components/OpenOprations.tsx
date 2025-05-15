"use client";

import { zodResolver } from "@hookform/resolvers/zod";
import { useForm } from "react-hook-form";
import { z } from "zod";
import React, { useState, useEffect } from "react";
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
import { Loader2 } from "lucide-react";

// Define form schema with validation and type coercion
const formSchema = z.object({
  type: z.enum(["buy", "sell"], {
    errorMap: () => ({ message: "Selecione o tipo de operação" }),
  }),
  operation: z.enum(["Market", "Sell Limit", "Buy Limit", "Sell Stop", "Buy Stop"], {
    errorMap: () => ({ message: "Selecione o tipo de operação" }),
  }), 
  price: z
    .string()
    .optional()
    .transform((val) => (val ? parseFloat(val) : undefined))
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

// Define component props
interface OpenOperationsProps {
  isVisible: boolean;
  onClose: () => void;
  Symbol: string;
}

const OpenOperations: React.FC<OpenOperationsProps> = ({ isVisible, onClose, Symbol }) => {
  const [isLoading, setIsLoading] = useState(false);
  const [isFormValid, setIsFormValid] = useState(false);

  const form = useForm<z.infer<typeof formSchema>>({
    resolver: zodResolver(formSchema),
    defaultValues: {
      type: "buy",
      operation: "Market",   
      price: "",
      takeprofit: "",
      stoploss: "",
    },
    mode: "onChange",
  });

  // Watch form values to determine button state
  useEffect(() => {
    const subscription = form.watch((values) => {
      const isValid = form.formState.isValid && !!values.type && !!values.operation;
      setIsFormValid(isValid);
    });
    return () => subscription.unsubscribe();
  }, [form]);

  // Handle form submission
  const onSubmit = async (values: z.infer<typeof formSchema>) => {
    setIsLoading(true);
    try {
      console.log("Form submitted:", { ...values, Symbol });
      // Simulate API call
      await new Promise((resolve) => setTimeout(resolve, 1000));
      form.reset();
      onClose();
    } catch (error) {
      console.error("Submission error:", error);
    } finally {
      setIsLoading(false);
    }
  };

  // Handle modal close
  const handleClose = (e: React.MouseEvent<HTMLDivElement>) => {
    if (e.target instanceof HTMLElement && e.target.id === "wrapper") {
      onClose();
    }
  };

  if (!isVisible) return null;

  return (
    <div
      id="wrapper"
      onClick={handleClose}
      role="dialog"
      aria-labelledby="modal-title"
      aria-modal="true"
      className="fixed inset-0 bg-black bg-opacity-25 flex justify-center items-center z-50"
    >
      <Card className="w-[450px] flex flex-col gap-1 p-4 bg-white shadow-lg rounded-lg">
        <CardHeader>
          <CardTitle id="modal-title" className="flex gap-2 text-xl items-center justify-start">
            <MdCurrencyExchange className="text-lg" />
            <span>Nova Operação - {Symbol}</span>
          </CardTitle>
          <CardDescription>Abrir uma nova operação</CardDescription>
          <Separator />
        </CardHeader>

        <CardContent>
          <Form {...form}>
            <form onSubmit={form.handleSubmit(onSubmit)} className="space-y-4">
              {/* Type Selection */}
              <FormField
                control={form.control}
                name="type"
                render={({ field }) => (
                  <FormItem>
                    <FormLabel>Tipo</FormLabel>
                    <div className="flex items-center justify-between text-xs gap-1 bg-slate-100 rounded-md p-1.5">
                      <button
                        type="button"
                        className={cn(
                          "w-[49%] h-7 rounded-l-sm transition-colors",
                          field.value === "buy" ? "bg-green-500 text-white" : "text-slate-600 hover:bg-slate-200"
                        )}
                        onClick={() => form.setValue("type", "buy", { shouldValidate: true })}
                        aria-pressed={field.value === "buy"}
                      >
                        Compra
                      </button>
                      <button
                        type="button"
                        className={cn(
                          "w-[49%] h-7 rounded-r-sm transition-colors",
                          field.value === "sell" ? "bg-red-500 text-white" : "text-slate-600 hover:bg-slate-200"
                        )}
                        onClick={() => form.setValue("type", "sell", { shouldValidate: true })}
                        aria-pressed={field.value === "sell"}
                      >
                        Venda
                      </button>
                    </div>
                    <FormMessage />
                  </FormItem>
                )}
              />

              {/* Operation Type */}
              <FormField
                control={form.control}
                name="operation"
                render={({ field }) => (
                  <FormItem>
                    <FormLabel>Tipo de Operação</FormLabel>
                    <Select onValueChange={field.onChange} value={field.value}>
                      <FormControl>
                        <SelectTrigger>
                          <SelectValue placeholder="Selecione o tipo de operação" />
                        </SelectTrigger>
                      </FormControl>
                      <SelectContent>
                        {["Market", "Sell Limit", "Buy Limit", "Sell Stop", "Buy Stop"].map((op) => (
                          <SelectItem key={op} value={op}>
                            {op}
                          </SelectItem>
                        ))}
                      </SelectContent>
                    </Select>
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
                    <FormLabel>Preço (Opcional)</FormLabel>
                    <FormControl>
                      <Input
                        placeholder="0.0"
                        type="number"
                        step="0.01"
                        min="0"
                        {...field}
                        value={field.value || ""}
                        onChange={(e) => field.onChange(e.target.value)}
                        aria-describedby="price-error"
                      />
                    </FormControl>
                    <FormMessage id="price-error" />
                  </FormItem>
                )}
              />

              {/* Take Profit */}
              <FormField
                control={form.control}
                name="takeprofit"
                render={({ field }) => (
                  <FormItem>
                    <FormLabel>Take Profit (Opcional)</FormLabel>
                    <FormControl>
                      <Input
                        placeholder="0.0"
                        type="number"
                        step="0.01"
                        min="0"
                        {...field}
                        value={field.value || ""}
                        onChange={(e) => field.onChange(e.target.value)}
                        aria-describedby="takeprofit-error"
                      />
                    </FormControl>
                    <FormMessage id="takeprofit-error" />
                  </FormItem>
                )}
              />

              {/* Stop Loss */}
              <FormField
                control={form.control}
                name="stoploss"
                render={({ field }) => (
                  <FormItem>
                    <FormLabel>Stop Loss (Opcional)</FormLabel>
                    <FormControl>
                      <Input
                        placeholder="0.0"
                        type="number"
                        step="0.01"
                        min="0"
                        {...field}
                        value={field.value || ""}
                        onChange={(e) => field.onChange(e.target.value)}
                        aria-describedby="stoploss-error"
                      />
                    </FormControl>
                    <FormMessage id="stoploss-error" />
                  </FormItem>
                )}
              />

              {/* Submit Button */}
              <div className="flex justify-end gap-2">
                <Button
                  type="button"
                  variant="outline"
                  onClick={onClose}
                  disabled={isLoading}
                >
                  Cancelar
                </Button>
                <Button
                  type="submit"
                  className="bg-green-500 hover:bg-green-600 text-white"
                  disabled={!isFormValid || isLoading}
                >
                  {isLoading ? (
                    <>
                      <Loader2 className="mr-2 h-4 w-4 animate-spin" />
                      Processando...
                    </>
                  ) : (
                    "Confirmar"
                  )}
                </Button>
              </div>
            </form>
          </Form>
        </CardContent>
      </Card>
    </div>
  );
};

export default OpenOperations;