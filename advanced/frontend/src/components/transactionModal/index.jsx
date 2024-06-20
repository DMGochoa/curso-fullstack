import { useState, useEffect } from 'react';
import './transactionModal.css';

const TransactionModal = ({ isOpen, onClose, onSave }) => {
    const [transactionTypes, setTransactionTypes] = useState([]);
    const [accounts, setAccounts] = useState([]);
    const [categories, setCategories] = useState([]);
    const [newTransaction, setNewTransaction] = useState({
        type_id: '',
        category_id: '',
        account_id: '',
        quantity: '',
        date: '',
    });

    const userId = parseInt(localStorage.getItem('userId'));
    const token = localStorage.getItem('token');

    useEffect(() => {
        if (isOpen) {
        const fetchTransactionTypes = async () => {
            try {
            const response = await fetch('http://localhost:8000/transaction_types', {
                headers: {
                'Authorization': `Bearer ${token}`,
                },
            });
            const data = await response.json();
            if (response.ok) {
                setTransactionTypes(data);
            } else {
                console.error('Failed to fetch transaction types:', data.message);
            }
            } catch (error) {
            console.error('Error:', error);
            }
        };

        const fetchAccounts = async () => {
            try {
            const response = await fetch(`http://localhost:8000/accounts/user`, {
                headers: {
                'Authorization': `Bearer ${token}`,
                },
            });
            const data = await response.json();
            if (response.ok) {
                setAccounts(data);
            } else {
                console.error('Failed to fetch accounts:', data.message);
            }
            } catch (error) {
            console.error('Error:', error);
            }
        };

        const fetchCategories = async () => {
            try {
            const response = await fetch('http://localhost:8000/transaction_categories', {
                headers: {
                'Authorization': `Bearer ${token}`,
                },
            });
            const data = await response.json();
            if (response.ok) {
                setCategories(data);
            } else {
                console.error('Failed to fetch categories:', data.message);
            }
            } catch (error) {
            console.error('Error:', error);
            }
        };

        fetchTransactionTypes();
        fetchAccounts();
        fetchCategories();
        }
    }, [isOpen, userId, token]);

    const handleInputChange = (e) => {
        const { name, value } = e.target;
        setNewTransaction((prevState) => ({
        ...prevState,
        [name]: value,
        }));
    };

    const handleSubmit = async (e) => {
        e.preventDefault();
        try {
        const response = await fetch('http://localhost:8000/transactions', {
            method: 'POST',
            headers: {
            'Content-Type': 'application/json',
            'Authorization': `Bearer ${token}`,
            },
            body: JSON.stringify({
            ...newTransaction,
            type_id: parseInt(newTransaction.type_id),
            category_id: parseInt(newTransaction.category_id),
            account_id: parseInt(newTransaction.account_id),
            quantity: parseInt(newTransaction.quantity),
            user_id: userId,
            }),
        });
        if (response.ok) {
            onSave();
            setNewTransaction({
            type_id: '',
            category_id: '',
            account_id: '',
            quantity: '',
            date: '',
            });
            onClose();
        } else {
            console.error('Failed to add transaction');
        }
        } catch (error) {
        console.error('Error:', error);
        }
    };

    if (!isOpen) {
        return null;
    }

    return (
        <div className="modal">
        <div className="modal-content">
            <span className="close" onClick={onClose}>
            &times;
            </span>
            <form onSubmit={handleSubmit}>
            <div>
                <label htmlFor="type_id">Type</label>
                <select name="type_id" value={newTransaction.type_id} onChange={handleInputChange}>
                <option value="">Select Type</option>
                {transactionTypes.map((type) => (
                    <option key={type.id} value={type.id}>
                    {type.name}
                    </option>
                ))}
                </select>
            </div>
            <div>
                <label htmlFor="category_id">Category</label>
                <select name="category_id" value={newTransaction.category_id} onChange={handleInputChange}>
                <option value="">Select Category</option>
                {categories.map((category) => (
                    <option key={category.id} value={category.id}>
                    {category.name}
                    </option>
                ))}
                </select>
            </div>
            <div>
                <label htmlFor="account_id">Account</label>
                <select name="account_id" value={newTransaction.account_id} onChange={handleInputChange}>
                <option value="">Select Account</option>
                {accounts.map((account) => (
                    <option key={account.id} value={account.id}>
                    {account.name}
                    </option>
                ))}
                </select>
            </div>
            <div>
                <label htmlFor="quantity">Quantity</label>
                <input
                type="number"
                name="quantity"
                value={newTransaction.quantity}
                onChange={handleInputChange}
                required
                />
            </div>
            <div>
                <label htmlFor="date">Date</label>
                <input
                type="date"
                name="date"
                value={newTransaction.date}
                onChange={handleInputChange}
                required
                />
            </div>
            <button type="submit">Add Transaction</button>
            </form>
        </div>
        </div>
    );
};

export default TransactionModal;
