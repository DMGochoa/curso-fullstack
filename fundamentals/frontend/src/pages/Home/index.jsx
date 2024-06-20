import "./Home.css";

import { useState } from "react";
import LineChart from "../../components/Plots/Line";
import PieChart from "../../components/Plots/Pie";
import BarChart from "../../components/Plots/bar";

const some_summary_data = [
  {
    date: "2024-03-14",
    type: "withdraw",
    total_amount: 141098.39,
  },
  {
    date: "2023-08-28",
    type: "interest",
    total_amount: 64700.7,
  },
  {
    date: "2023-11-29",
    type: "interest",
    total_amount: 168741.98,
  },
  {
    date: "2024-05-02",
    type: "interest",
    total_amount: 165766.81,
  },
  {
    date: "2023-06-25",
    type: "withdraw",
    total_amount: 174170.32,
  },
  {
    date: "2024-01-13",
    type: "deposit",
    total_amount: 76303.91,
  },
  {
    date: "2023-09-04",
    type: "withdraw",
    total_amount: 189484.33,
  },
  {
    date: "2023-07-22",
    type: "deposit",
    total_amount: 52519.53,
  },
  {
    date: "2023-07-09",
    type: "deposit",
    total_amount: 144381.06,
  },
  {
    date: "2023-10-14",
    type: "interest",
    total_amount: 165718.61,
  },
  {
    date: "2023-12-30",
    type: "deposit",
    total_amount: 163031.29,
  },
  {
    date: "2023-09-08",
    type: "withdraw",
    total_amount: 100728.12,
  },
  {
    date: "2023-07-28",
    type: "withdraw",
    total_amount: 184897.73,
  },
  {
    date: "2023-07-14",
    type: "deposit",
    total_amount: 54991.99,
  },
  {
    date: "2023-11-10",
    type: "withdraw",
    total_amount: 69182.42,
  },
  {
    date: "2023-11-24",
    type: "deposit",
    total_amount: 119871.19,
  },
  {
    date: "2023-10-28",
    type: "withdraw",
    total_amount: 159834.29,
  },
  {
    date: "2024-01-29",
    type: "withdraw",
    total_amount: 140044.62,
  },
  {
    date: "2024-03-13",
    type: "deposit",
    total_amount: 77578.71,
  },
  {
    date: "2024-01-30",
    type: "withdraw",
    total_amount: 6679.47,
  },
  {
    date: "2023-10-07",
    type: "interest",
    total_amount: 138058.97,
  },
  {
    date: "2023-12-20",
    type: "interest",
    total_amount: 70060.53,
  },
  {
    date: "2024-04-24",
    type: "interest",
    total_amount: 22240.33,
  },
  {
    date: "2023-07-14",
    type: "deposit",
    total_amount: 112367.97,
  },
  {
    date: "2024-05-14",
    type: "deposit",
    total_amount: 178840.89,
  },
  {
    date: "2023-07-08",
    type: "deposit",
    total_amount: 43585.41,
  },
  {
    date: "2023-08-16",
    type: "interest",
    total_amount: 182727.93,
  },
  {
    date: "2023-11-30",
    type: "withdraw",
    total_amount: 169086.33,
  },
  {
    date: "2023-11-04",
    type: "deposit",
    total_amount: 63891.85,
  },
  {
    date: "2023-07-10",
    type: "interest",
    total_amount: 18418.49,
  },
];
const some_transactions_data = [
  {
    id: 1,
    account_id: 1,
    type: "Type 1",
    category: "Category 1",
    quantity: 1,
    date: "2021-01-01",
  },
  {
    id: 2,
    account_id: 2,
    type: "Type 2",
    category: "Category 2",
    quantity: 2,
    date: "2021-01-02",
  },
];
const some_accounts_data = [
    { id: 1, name: "Account 1" },
    { id: 2, name: "Account 2" },
];
const some_data_order_by_date = some_summary_data.sort((a, b) => new Date(a.date) - new Date(b.date));
const porcentage_data_by_type = [
	{
		"type": "deposit",
		"total_amount": 80000,
		"percentage": 33.33
	},
	{
		"type": "withdraw",
		"total_amount": 160000,
		"percentage": 56.67
	},
  {
    "type": "interest",
    "total_amount": 20000,
    "percentage": 10
  }
];
const monthly_average_data = [
	{
		"type": "deposit",
		"average_monthly_amount": 80000.0
	},
	{
		"type": "withdraw",
		"average_monthly_amount": 160000.0
	}
];

const Home = () => {
  const [accounts, setAccounts] = useState(some_accounts_data);
  const [transactions, setTransactions] = useState(some_transactions_data);
  const [transactions_summary, setTransactionsSummary] = useState(some_data_order_by_date);
  const [transactions_porcentage, setTransactionsPorcentage] = useState(porcentage_data_by_type);

  return (
    <div className="general-container">
      <div className="filters-container">
        <div className="filters">
          <h3>Filters</h3>
          <div>
            <label htmlFor="account">Account:</label>
            <select name="account">
              {accounts.map((account) => (
                <option key={account.id} value={account.id}>
                  {account.name}
                </option>
              ))}
            </select>
          </div>
        </div>
      </div>
      <div className="info-container">
        <div className="info-table">
          <table>
            <thead>
              <tr>
                <th>Account</th>
                <th>Type</th>
                <th>Category</th>
                <th>Quantity</th>
                <th>Date</th>
              </tr>
            </thead>
            <tbody>
              {transactions.map((transaction) => (
                <tr key={transaction.id}>
                  <td>{transaction.account_id}</td>
                  <td>{transaction.type}</td>
                  <td>{transaction.category}</td>
                  <td>{transaction.quantity}</td>
                  <td>{new Date(transaction.date).toLocaleDateString()}</td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
        <div className="info-charts">
          <div className="top-chart">
            <LineChart data={transactions_summary} />
          </div>
          <div className="bottom-chart">
            <div className="left-chart">
              <BarChart data={monthly_average_data} />
            </div>
            <div className="right-chart">
            <PieChart data={transactions_porcentage} barPadding={1} />
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};

export default Home;
