import "../styles/results.css"
import Logo from "../assets/koiZen.svg"
import React, { useEffect } from 'react'
import { useState } from 'react';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome'
import { faMagnifyingGlass } from '@fortawesome/free-solid-svg-icons'
import { motion, useAnimationControls } from "framer-motion";
import Header from "./header"
import Koi from "../assets/koi-img.jpg"

function Results() {

    const [query, setQuery] = useState('');
    // const [age, setAge] = useState('20');
    // const ageAsNumber = Number(age);
    function search(formData) {
        const query = formData.get("query");
        alert(`You searched for '${query}'`);
    }

    return (
        <div className="results-page">
            <div className="banner">
                <div className="column">
                    <Header />
                </div>
                <div className="column">
                    <img className="koi-img-card" src={Koi} alt="Fish Search Result" />
                </div>
            </div>
        </div>

    );
}

export default Results;
