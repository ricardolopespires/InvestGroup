import MetaTrader5 as mt5
import time
import logging

logger = logging.getLogger(__name__)

class ConectorMT5:
    def __init__(self, conta, senha, servidor, timeout=30, max_tentativas_reconexao=5):
        self.conta = conta
        self.senha = senha
        self.servidor = servidor
        self.timeout = timeout
        self.max_tentativas_reconexao = max_tentativas_reconexao
        self.conectado = False

    def conectar(self):
        if not mt5.initialize():
            logger.error("Falha ao inicializar o MT5")
            return False
        if not mt5.login(self.conta, password=self.senha, server=self.servidor, timeout=self.timeout):
            logger.error(f"Erro ao fazer login: {mt5.last_error()}")
            return False
        self.conectado = True
        logger.info("Conexão com MT5 estabelecida!")
        return True

    def desconectar(self):
        mt5.shutdown()
        self.conectado = False
        logger.info("Desconectado do MT5")

    def reconectar(self):
        tentativas = 0
        while tentativas < self.max_tentativas_reconexao:
            logger.warning(f"Tentativa de reconexão {tentativas + 1}/{self.max_tentativas_reconexao}")
            if self.conectar():
                return True
            tentativas += 1
            time.sleep(5)
        logger.error("Falha ao reconectar após %d tentativas", self.max_tentativas_reconexao)
        return False

    def verificar_conexao(self):
        if not self.conectado or not mt5.account_info():
            logger.warning("Conexão perdida, tentando reconectar...")
            self.desconectar()
            return self.reconectar()
        return True

    def obter_saldo_conta(self):
        if not self.verificar_conexao():
            return None
        info_conta = mt5.account_info()
        if info_conta:
            return info_conta.balance
        else:
            logger.error(f"Erro ao obter informações da conta: {mt5.last_error()}")
            return None

    def obter_posicoes_abertas(self):
        if not self.verificar_conexao():
            return []
        posicoes = mt5.positions_get()
        if posicoes is None:
            logger.error(f"Erro ao obter posições: {mt5.last_error()}")
            return []
        return posicoes