import "../styles/search.css"
import Logo from "../assets/koiZen.svg"
import React, { useState } from 'react'



function Search() {
    return (
        <div className="search">
            <img className="zen-icon" src={Logo} alt="logo" />
            <div className="search-bar">
                <p className="search-placeholder">Enter your query here!</p>
            </div>
        </div>

    );
}

export default Search;

