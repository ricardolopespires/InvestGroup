"use client"

import CountPopulation from "@/components/CountPopulation"
import CountrieCurrency from "@/components/CountrieCurrency"
import {
    Card,
    CardContent,
    CardDescription,
    CardFooter,
    CardHeader,
    CardTitle,
} from "@/components/ui/card"
import { Separator } from "@/components/ui/separator"
import axios from 'axios'
import { useParams } from 'next/navigation'
import React, { useEffect } from 'react'

const Page = () => {
    const [countrie, setCountrie] = React.useState<any>({}) // Tipagem temporária como 'any'
    const [loading, setLoading] = React.useState(true)
    const params = useParams()

    useEffect(() => {
        const fetchCountries = async () => {
            try {
                const res = await axios.get(`https://restcountries.com/v3.1/alpha/${params.id}`)
                setCountrie(res.data[0])
                setLoading(false) // Dados carregados, desativa o loading
            } catch (error) {
                console.error("Error fetching countries:", error)
                setLoading(false) // Em caso de erro, também desativa o loading
            }
        }
        fetchCountries()
    }, [params])

    if (loading) {
        return <div>Carregando...</div> // Mostra um loading enquanto os dados não chegam
    }

    return (
        <main className="flex flex-col min-h-screen mx-16 gap-4 text-black -mt-[90px] z-40">
            <div className="flex gap-2">
                <div className="w-5/6">
                    <Card>
                        <CardHeader>
                            <div className="flex items-center justify-between gap-2">
                                <div>
                                    <CardTitle className="flex items-center gap-2">
                                        <img
                                            src={countrie.coatOfArms?.png}
                                            alt={countrie.name?.common}
                                            className="w-11 h-11 rounded-sm"
                                        />
                                        <span>{countrie.name?.common}</span>
                                    </CardTitle>
                                    <CardDescription>{countrie.translations?.por?.official}</CardDescription>
                                </div>
                                <CountPopulation population={countrie.population} />
                            </div>
                            <Separator className="my-4" />
                        </CardHeader>
                        <CardContent>
                            <p>Card Content</p>
                        </CardContent>
                        <CardFooter>
                            <p>Card Footer</p>
                        </CardFooter>
                    </Card>
                </div>
                <div className="w-1/6">
                    {countrie.currencies && (
                        <CountrieCurrency currency={Object.keys(countrie.currencies)[0]} />
                    )}
                </div>
            </div>
        </main>
    )
}

export default Page