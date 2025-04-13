import React from 'react'
import DatePicker from 'react-datepicker'
import 'react-datepicker/dist/react-datepicker.css' // Estilo padrão

const OperationsHistory = ({ symbol, Asset, UserId }) => {
    const [operations, setOperations] = React.useState([])
    const [filteredOperations, setFilteredOperations] = React.useState([])
    const [loading, setLoading] = React.useState(true)
    const [error, setError] = React.useState(null)
    const [startDate, setStartDate] = React.useState(null)
    const [endDate, setEndDate] = React.useState(null)

    const fetchOperations = async () => {
        try {
            const response = await fetch(`/api/operations?asset=${Asset}&userId=${UserId}`)
            if (!response.ok) {
                throw new Error('Network response was not ok')
            }
            const data = await response.json()
            setOperations(data)
            setFilteredOperations(data)
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

            // Ajusta o final do dia para incluir todas as operações do dia final
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
    }, [])

    React.useEffect(() => {
        filterByDate()
    }, [startDate, endDate, operations])

    if (loading) return <div className="text-center">Carregando...</div>
    if (error) return <div className="text-center text-red-500">Erro: {error.message}</div>

    return (
        <div className="flex flex-col items-center justify-center w-full h-full p-4">
            <h1 className="text-2xl font-bold mb-6">Histórico de Operações</h1>
            
            {/* Filtro de Datas */}
            <div className="flex flex-col sm:flex-row gap-4 mb-6 w-full max-w-2xl">
                <div className="flex-1">
                    <label className="block text-sm font-medium mb-1 text-gray-700">
                        Data Inicial
                    </label>
                    <DatePicker
                        selected={startDate}
                        onChange={(date) => setStartDate(date)}
                        selectsStart
                        startDate={startDate}
                        endDate={endDate}
                        maxDate={endDate || new Date()} // Não permite data futura se não houver endDate
                        dateFormat="dd/MM/yyyy"
                        placeholderText="Selecione a data inicial"
                        className="w-full p-2 border rounded-md focus:ring-2 focus:ring-blue-500 focus:border-blue-500"
                        isClearable
                    />
                </div>
                <div className="flex-1">
                    <label className="block text-sm font-medium mb-1 text-gray-700">
                        Data Final
                    </label>
                    <DatePicker
                        selected={endDate}
                        onChange={(date) => setEndDate(date)}
                        selectsEnd
                        startDate={startDate}
                        endDate={endDate}
                        minDate={startDate} // Não permite data anterior à inicial
                        maxDate={new Date()} // Não permite data futura
                        dateFormat="dd/MM/yyyy"
                        placeholderText="Selecione a data final"
                        className="w-full p-2 border rounded-md focus:ring-2 focus:ring-blue-500 focus:border-blue-500"
                        isClearable
                    />
                </div>
            </div>

            {/* Lista de Operações Filtradas */}
            <div className="w-full max-w-2xl">
                {filteredOperations.length > 0 ? (
                    <ul className="space-y-3">
                        {filteredOperations.map((operation, index) => (
                            <li 
                                key={index} 
                                className="border p-3 rounded-md shadow-sm bg-white hover:bg-gray-50 transition"
                            >
                                <p className="text-sm">
                                    Data: {new Date(operation.date).toLocaleDateString('pt-BR', {
                                        day: '2-digit',
                                        month: '2-digit',
                                        year: 'numeric',
                                        hour: '2-digit',
                                        minute: '2-digit'
                                    })}
                                </p>
                                {/* Adicione mais campos conforme sua estrutura de dados */}
                            </li>
                        ))}
                    </ul>
                ) : (
                    <p className="text-center text-gray-500">
                        Nenhuma operação encontrada para o período selecionado
                    </p>
                )}
            </div>
        </div>
    )
}

export default OperationsHistory