import "../styles/search.css"
import Logo from "../assets/koiZen.svg"
import React, { useEffect } from 'react'
import { useState } from 'react';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome'
import { faMagnifyingGlass } from '@fortawesome/free-solid-svg-icons'
import { motion, useAnimationControls } from "framer-motion";
import { useNavigate } from 'react-router-dom';


function Search() {

    const [query, setQuery] = useState('');
    // const [age, setAge] = useState('20');
    // const ageAsNumber = Number(age);
    function search(formData) {
        const query = formData.get("query");
        alert(`You searched for '${query}'`);

    }
    const navigate = useNavigate();

    function handleClick() {
        navigate('/query');
    }


    return (
        <div className="search">
            <img className="zen-icon" src={Logo} alt="logo" />
            <motion.div whileHover={{ scale: 1.2 }} >
                <label className="search-area">
                    <FontAwesomeIcon icon={faMagnifyingGlass} />
                    <form action={search} onSubmit={handleClick}>
                        <input name="query" className="search-bar" value={query} defaultValue={'Search for a Zen page or type a URL'} onChange={e => setQuery(e.target.value)} />
                        {/* <button type="submit">Search</button> */}
                    </form>
                </label>
            </motion.div>
            <div>
                {query !== '' && <p>Your Query: {query}</p>}
            </div>
        </div>

    );
}

export default Search;
