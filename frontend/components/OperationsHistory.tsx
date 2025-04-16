import { getTransactions } from '@/lib/actions/actions.transactions'
import React from 'react'
import DatePicker from 'react-datepicker'
import 'react-datepicker/dist/react-datepicker.css'
import { ScrollArea } from './ui/scroll-area'
import { cn } from '@/lib/utils'

const OperationsHistory = ({ symbol, Asset, UserId }) => {
    const [operations, setOperations] = React.useState([])
    const [filteredOperations, setFilteredOperations] = React.useState([])
    const [loading, setLoading] = React.useState(true)
    const [error, setError] = React.useState(null)
    const [startDate, setStartDate] = React.useState(null)
    const [endDate, setEndDate] = React.useState(null)

    const fetchOperations = async () => {
        try {
            const response = await getTransactions({ symbol, UserId })
            setOperations(response)
            setFilteredOperations(response)
        } catch (error) {
            setError(error)
        } finally {
            setLoading(false)
        }
    }

    const filterByDate = () => {
        if (!startDate && !endDate) {
            setFilteredOperations(operations)
            return
        }

        const filtered = operations.filter(op => {
            const opDate = new Date(op.date)
            const start = startDate ? new Date(startDate) : null
            const end = endDate ? new Date(endDate) : null

            if (end) end.setHours(23, 59, 59, 999)

            if (start && end) {
                return opDate >= start && opDate <= end
            } else if (start) {
                return opDate >= start
            } else if (end) {
                return opDate <= end
            }
            return true
        })

        setFilteredOperations(filtered)
    }

    React.useEffect(() => {
        fetchOperations()
    }, [symbol, UserId])

    React.useEffect(() => {
        filterByDate()
    }, [startDate, endDate, operations])

    if (loading) return <div className="text-center">Carregando...</div>
    if (error) return <div className="text-center text-red-500">Erro: {error.message}</div>

    return (
        <div className="flex flex-col items-center justify-center w-full h-full">
            {/* Filtro de Datas */}
      

            {/* Cabeçalho da tabela */}
            <div className="w-full grid grid-cols-11 items-center justify-center h-9 text-xs bg-gray-100">
                <div className='flex items-center justify-center'>Ativo</div>
                <div className='flex items-center justify-center'>Nº</div>
                <div className='flex items-center justify-center'>Data</div>
                <div className='flex items-center justify-center'>Tipo</div>
                <div className='flex items-center justify-center'>Volume</div>
                <div className='flex items-center justify-center'>Entrada</div>
                <div className='flex items-center justify-center'>S/L</div>
                <div className='flex items-center justify-center'>T/P</div> 
                <div className='flex items-center justify-center'>Saída</div>
                <div className='flex items-center justify-center'>Lucro</div>
                <div className='flex items-center justify-center'></div>
            </div>

            {/* Lista de operações */}
            <ScrollArea className="h-[400px] w-full">
                {filteredOperations.length > 0 ? (
                    filteredOperations.map((operation, i) => (
                        <div key={i} className="grid grid-cols-11 items-center justify-center border-b h-9 border-gray-300 text-xs px-1">
                            <div className="text-center">{operation.asset}</div>
                            <div className="text-center">{operation.id}</div>
                            <div className="text-center">{new Date(operation.date).toLocaleDateString('pt-BR')}</div>
                            <div className={cn("text-center",
                                operation.type === 1 ? "text-green-500" : "text-red-500"
                            )}>
                                {operation.type === 1 ? 'Buy' : 'Sell'}
                            </div>
                            <div className="text-center">{operation.volume}</div>
                            <div className="text-center">{operation.price_entry}</div>
                            <div className="text-center">{operation.sl}</div>
                            <div className="text-center">{operation.tp}</div>
                            <div className="text-center">{operation.exit}</div>
                            <div className={cn("text-center",
                                operation.profit > 0 ? "text-green-500" : "text-red-500"
                            )}>{operation.profit}</div>
                            <div className="text-center"></div>
                        </div>
                    ))
                ) : (
                    <p className="text-center text-gray-500 py-4">
                        Nenhuma operação encontrada para o período selecionado
                    </p>
                )}
            </ScrollArea>
        </div>
    )
}

export default OperationsHistory
