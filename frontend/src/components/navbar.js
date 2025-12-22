import React, { useState } from "react";
import { useNavigate } from "react-router-dom";


function Navbar() {
    const [isOpen, setIsOpen] = useState(false);
    const navigate = useNavigate();

    const toggleMenu = () => setIsOpen(!isOpen);

    const handleNavClick = (link) => {
        const isRoute = link.startsWith("/");

        if (isRoute) {
            navigate(link);
        } else {
            const element = document.querySelector(link);
            if (element) {
                element.scrollIntoView({ behavior: "smooth", block: "start" });
            }
        }

        setIsOpen(false); // close menu after click
    };

    return (
        <header className="fixed top-0 left-0 w-full bg-neutral-800 z-50">
            <div className="mx-auto flex h-16 max-w-screen-xl items-center px-4">

                {/* Logo */}
                <span
                    onClick={() => handleNavClick("#header")}
                    className="text-indigo-400 font-semibold cursor-pointer"
                >
                    STUDIOFY
                </span>

                {/* Desktop Menu */}
                <nav className="hidden md:flex ml-auto">
                    <ul className="flex gap-6 text-base text-yellow-400">
                        <li>
                            <button onClick={() => handleNavClick("#header")} className="hover:text-rose-400">
                                Home
                            </button>
                        </li>
                        <li>
                            <button onClick={() => handleNavClick("#feature")} className="hover:text-rose-400">
                                Feature
                            </button>
                        </li>
                        <li>
                            <button onClick={() => handleNavClick("#footer")} className="hover:text-rose-400">
                                About
                            </button>
                        </li>
                    </ul>
                </nav>

                {/* Hamburger */}
                <button
                    onClick={toggleMenu}
                    className="ml-auto md:hidden rounded bg-gray-100 p-2 text-gray-600"
                    aria-label="Toggle Menu"
                >
                    ☰
                </button>
            </div>

            {/* Mobile Menu */}
            <div
                className={`md:hidden bg-neutral-900 transition-all duration-300 overflow-hidden ${isOpen ? "max-h-60 opacity-100" : "max-h-0 opacity-0"
                    }`}
            >
                <ul className="flex flex-col gap-4 p-4 text-white">
                    <li>
                        <button onClick={() => handleNavClick("#header")} className="text-left">
                            Home
                        </button>
                    </li>
                    <li>
                        <button onClick={() => handleNavClick("#feature")} className="text-left">
                            Feature
                        </button>
                    </li>
                    <li>
                        <button onClick={() => handleNavClick("#footer")} className="text-left">
                            About
                        </button>
                    </li>
                </ul>
            </div>
        </header>
    );
}

export default Navbar;
