import React from "react";
import Navbar from "../components/navbar";
import Header from "../components/header";
import Feature from "../components/feature";
import Footer from "../components/footer";

const Home = () => {
    return (
        <>
            <Navbar />

            <section id="header">
                <Header />
            </section>

            <section id="feature">
                <Feature />
            </section>

            <section id="footer">
                <Footer />
            </section>
        </>
    )
}

export default Home;