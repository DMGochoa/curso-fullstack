import { useRoutes, BrowserRouter } from 'react-router-dom'

import Home from './../Home';
import Navbar from './../../components/Navbar';
import './App.css';

const AppRoutes = () => {
    return useRoutes([
        {path: '/', element: <Home />},
    ])
}

const App = () => {
    return (
        <BrowserRouter>
            <Navbar />
            <AppRoutes />
        </BrowserRouter>
    );
};

export default App;