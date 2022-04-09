import MetaTrader5 as mt5






def MQL5(request, login, server, passowrd):

 
    # estabelecemos a conexão com o terminal MetaTrader 5 para a conta especificada
    if not mt5.initialize(login=25115284, server="MetaQuotes-Demo",password="4zatlbqx"):
        mt5.shutdown()
        return  "initialize() failed, error code =",mt5.last_error()
   
    else:
        mt5.shutdown()


        