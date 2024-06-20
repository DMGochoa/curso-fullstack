import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import Login from '../login';
import Dashboard from '../dashboard';
import Transactions from '../transactions';
import './app.css';

const App = () => {
    return (
        <Router>
            <Routes>
                <Route path="/" element={<Login />} />
                <Route path="/dashboard" element={<Dashboard />} />
                <Route path="/transactions" element={<Transactions />} />
            </Routes>
        </Router>
    );
};

export default App;