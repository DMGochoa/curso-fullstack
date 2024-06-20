import { useState } from 'react';
import { Link } from 'react-router-dom';
import './navbar.css';

const Navbar = () => {
    const [isExpanded, setIsExpanded] = useState(false);

    const toggleNavbar = () => {
        setIsExpanded(!isExpanded);
    };

    return (
        <nav className={`navbar ${isExpanded ? 'expanded' : ''}`}>
        <button className="navbar-toggle" onClick={toggleNavbar}>
            ☰
        </button>
        <div className="navbar-logo">
            <Link to="/">Logo</Link>
        </div>
        <ul className="navbar-links">
            <li>
            <Link to="/transactions">General</Link>
            </li>
            <li>
            <Link to="/dashboard">Dashboard</Link>
            </li>
            <li>
            <Link to="/settings">Configuración</Link>
            </li>
        </ul>
        </nav>
    );
};

export default Navbar;
