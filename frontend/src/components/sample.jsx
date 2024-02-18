import "../styles/search.css"
import Logo from "../assets/koiZen.svg"
import React, { useEffect } from 'react'
import { useState } from 'react';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome'
import { faMagnifyingGlass } from '@fortawesome/free-solid-svg-icons'
import { motion, useAnimationControls } from "framer-motion";


function Search() {

    const [query, setQuery] = useState('');
    // const [age, setAge] = useState('20');
    // const ageAsNumber = Number(age);
    function search(formData) {
        const query = formData.get("query");
        alert(`You searched for '${query}'`);
    }

    return (
        <div className="search">
            <img className="zen-icon" src={Logo} alt="logo" />
            <h2>TESTINNGGGG MY PRETTIES</h2>

        </div>

    );
}

export default Search;
