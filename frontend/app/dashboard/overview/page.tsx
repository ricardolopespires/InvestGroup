

import React from 'react';

const Page: React.FC = () => {
  return (
    <div className="dashboard-overview">
      <header className="header">
        <h1>Bem-vindo de volta!</h1>
        <nav>
          <ul>
            <li>Overview</li>
            <li>Transaction</li>
            <li>Invoices</li>
            <li>Statistics</li>
          </ul>
        </nav>
      </header>
      
      <section className="financial-summary">
        <div className="card">
          <h2>Saldo Total</h2>
          <p>$32,456.00</p>
          <button>Transferir</button>
          <button>Solicitar</button>
        </div>
        <div className="card">
          <h2>Renda Total</h2>
          <p>$10,456.00</p>
        </div>
        <div className="card">
          <h2>Limite de Gastos</h2>
          <p>$2,456.00 de $10,000.00</p>
        </div>
        <div className="card">
          <h2>Despesas Totais</h2>
          <p>$2,456.00</p>
        </div>
      </section>

      <section className="saving-plans">
        <h2>Planos de Poupança</h2>
        <ul>
          <li>Comprar carro novo - $5,000.00</li>
          <li>Plano de casamento - $3,500.00</li>
          <li>Comprar PS5 - $500.00</li>
        </ul>
      </section>

      <section className="transaction-history">
        <h2>Histórico de Transações</h2>
        <table>
          <thead>
            <tr>
              <th>Nome</th>
              <th>Tipo</th>
              <th>Data</th>
              <th>Quantia</th>
              <th>Status</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td>Plano Figma Pro</td>
              <td>Assinatura</td>
              <td>20 Out 2022</td>
              <td>$64.00</td>
              <td>Concluído</td>
            </tr>
            <tr>
              <td>Fiverr Internacional</td>
              <td>Receber</td>
              <td>20 Out 2022</td>
              <td>$100.00</td>
              <td>Concluído</td>
            </tr>
          </tbody>
        </table>
      </section>
    </div>
  );
}

export default Page;