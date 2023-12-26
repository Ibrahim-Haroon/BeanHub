import React, { useState } from 'react';
import { Link } from 'react-router-dom';

function Navbar() {
    const [click, setClick] = useState(false); 
    const handleClick = () => setClick(!click); 
    const closeMobileMenu = () => setClick(false); 
  return (
    <>  
        <nav className="navbar">
            <div className="navbar-container">
                <Link to="/" className="navbar-logo">
<<<<<<< HEAD:scripts/ client/src/components/Navbar.js
                    Beanhub
=======
                    AAAAAAAAAAAAAAAAAAAAAAAAAAA
>>>>>>> 963cbb8e73749c659dff72ee8281d1233bc191ee:scripts/client/src/components/Navbar.js
                </Link>
                <div className='menu-icon'>
                    <i className={click ? 'fas fa-times' : 'fas fa-bars'} />
                </div>
                <ul className={click ? 'nav-menu active' : 'nav-menu'}>
                    <li className='nav-item'>
                        <Link to='/' className='nav-Links' onClick={closeMobileMenu}>
                            Home
                        </Link>
                    </li>
                    <li className='nav-item'>
                        <Link to='/services' className='nav-Links' onClick={closeMobileMenu}>
                            Services
                        </Link>
                    </li>
                    <li className='nav-item'>
                        <Link to='/products' className='nav-links' onClick={closeMobileMenu}>
                            Products
                        </Link>
                    </li>
                    <li className='nav-item'>
                        <Link to='/sign-up' className='nav-links-mobile' onClick={closeMobileMenu}>
                            Sign Up
                        </Link>
                    </li>
                </ul>
            </div>
        </nav>
    </>
  );
}

export default Navbar;