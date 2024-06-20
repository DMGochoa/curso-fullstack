import { useEffect, useState } from "react";
import Navbar from "../../components/navbar";
import TransactionModal from "../../components/transactionModal";
import "./transactions.css";

const Transactions = () => {
    const [transactions, setTransactions] = useState([]);
    const [isModalOpen, setIsModalOpen] = useState(false);

    const token = localStorage.getItem("token");

    useEffect(() => {
        const fetchTransactions = async () => {
        try {
            const response = await fetch(`http://localhost:8000/transactions/`, {
            headers: {
                Authorization: `Bearer ${token}`,
            },
            });
            const data = await response.json();
            if (response.ok) {
            setTransactions(data);
            } else {
            console.error("Failed to fetch transactions:", data.message);
            }
        } catch (error) {
            console.error("Error:", error);
        }
        };

        fetchTransactions();
    }, [token]);

    const handleSaveTransaction = () => {
        // Refetch transactions after adding a new one
        const fetchTransactions = async () => {
        try {
            const response = await fetch(`http://localhost:8000/transactions/`, {
            headers: {
                Authorization: `Bearer ${token}`,
            },
            });
            const data = await response.json();
            if (response.ok) {
            setTransactions(data);
            } else {
            console.error("Failed to fetch transactions:", data.message);
            }
        } catch (error) {
            console.error("Error:", error);
        }
        };

        fetchTransactions();
    };

    return (
        <div className="page-container">
        <Navbar />
        <div className="transactions-content">
            <h1>Transactions</h1>
            <table>
            <thead>
                <tr>
                <th>Type</th>
                <th>Category</th>
                <th>Account</th>
                <th>Quantity</th>
                <th>Date</th>
                </tr>
            </thead>
            <tbody>
                {transactions?.map((transaction) => (
                <tr key={transaction.id}>
                    <td>{transaction.type.name}</td>
                    <td>{transaction.category.name}</td>
                    <td>{transaction.account.name}</td>
                    <td>{transaction.quantity}</td>
                    {/* Change format tu dd-mm-yyyy */}
                    <td>{new Date(transaction.date).toLocaleDateString()}</td>
                </tr>
                ))}
            </tbody>
            </table>
            <button
            className="add-transaction-button"
            onClick={() => setIsModalOpen(true)}
            >
            Add Transaction
            </button>
            <TransactionModal
            isOpen={isModalOpen}
            onClose={() => setIsModalOpen(false)}
            onSave={handleSaveTransaction}
            />
        </div>
        </div>
    );
};

export default Transactions;
