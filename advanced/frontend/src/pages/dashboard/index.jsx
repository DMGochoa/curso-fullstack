import { useEffect, useState } from 'react';
import Navbar from '../../components/navbar';
import LineChart from '../../components/lineChart';
import './dashboard.css';

const Dashboard = () => {
    const [summaryData, setSummaryData] = useState([]);
    const token = localStorage.getItem('token');

    useEffect(() => {
        const fetchSummary = async () => {
        try {
            const response = await fetch('http://localhost:8000/transactions/summary', {
            headers: {
                Authorization: `Bearer ${token}`,
            },
            });
            const data = await response.json();
            if (response.ok) {
            setSummaryData(data);
            } else {
            console.error('Failed to fetch summary data:', data.message);
            }
        } catch (error) {
            console.error('Error:', error);
        }
        };

        fetchSummary();
    }, [token]);

    return (
        <div className="page-container">
        <Navbar />
        <div className="dashboard-content">
            <h1>Dashboard</h1>
            <div className="chart-container">
            <LineChart data={summaryData} />
            </div>
        </div>
        </div>
    );
};

export default Dashboard;
