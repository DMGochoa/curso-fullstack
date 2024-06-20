import { useState } from 'react';
import { Link } from 'react-router-dom';
import './Navbar.css';

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
            <Link to="/">General</Link>
            </li>
            <li>
            <Link to="/">Dashboard</Link>
            </li>
            <li>
            <Link to="/">Configuración</Link>
            </li>
        </ul>
        </nav>
    );
};

export default Navbar;